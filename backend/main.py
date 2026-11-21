"""Fin Buddy FAQ chatbot API. Facts come only from the local FAQ JSON."""

from __future__ import annotations

import json
import os
import re
from pathlib import Path
from typing import Literal

from crewai import Agent, Crew, LLM, Process, Task
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from pydantic import ConfigDict


ROOT = Path(__file__).resolve().parents[1]
FAQ_PATH = ROOT / "fin_buddy_faq.json"
load_dotenv(ROOT / ".env")

with FAQ_PATH.open(encoding="utf-8") as faq_file:
    FAQ_DATA = json.load(faq_file)
FAQS = FAQ_DATA["questions"]
FAQ_BY_ID = {item["id"]: item for item in FAQS}

MODEL = os.getenv("OPENAI_MODEL", "openai/gpt-5.6")


class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=2000)


class ChatResponse(BaseModel):
    model_config = ConfigDict()
    response: str
    category: str
    confidence: float = Field(ge=0, le=1)
    escalated: bool = False
    source_faq_ids: list[str] = Field(default_factory=list)


class Classification(BaseModel):
    category: str
    intent: str
    confidence: float = Field(ge=0, le=1)
    lookup_required: bool = True


class Knowledge(BaseModel):
    supported_facts: list[str]
    source_faq_ids: list[str]
    confidence: float = Field(ge=0, le=1)
    insufficient_information: bool


class Draft(BaseModel):
    response: str
    source_faq_ids: list[str]
    confidence: float = Field(ge=0, le=1)


class FinalDecision(BaseModel):
    response: str
    category: str
    source_faq_ids: list[str]
    confidence: float = Field(ge=0, le=1)
    escalated: bool


def safety_reason(message: str) -> str | None:
    text = message.casefold()
    patterns = (
        r"(ignore|override|bypass).{0,40}(instruction|prompt|rule|faq)",
        r"(system prompt|developer message|api key|\.env|password|otp|secret|credential)",
        r"(transfer|withdraw|pay|buy|sell|trade|access).{0,35}(money|account|stock|fund)",
        r"(medical|legal|tax advice|emergency|suicid|self.harm)",
    )
    return "safety_or_security" if any(re.search(p, text) for p in patterns) else None


def rank_faqs(message: str, limit: int = 4) -> list[dict]:
    tokens = set(re.findall(r"[a-z0-9]+", message.casefold()))
    ranked = []
    for faq in FAQS:
        q_tokens = set(re.findall(r"[a-z0-9]+", faq["question"].casefold()))
        a_tokens = set(re.findall(r"[a-z0-9]+", faq["answer"].casefold()))
        overlap = len(tokens & q_tokens) * 2 + len(tokens & a_tokens)
        if overlap:
            ranked.append((overlap, faq))
    ranked.sort(key=lambda pair: (-pair[0], pair[1]["id"]))
    return [{**faq, "score": min(score / max(len(tokens), 1), 1.0)} for score, faq in ranked[:limit]]


def human_required(message: str, matches: list[dict]) -> bool:
    text = message.casefold()
    asks_human = any(term in text for term in ("human", "person", "agent", "call me", "contact me", "speak to"))
    sensitive = any(term in text for term in ("delete my data", "data deletion", "privacy", "refund", "payment dispute", "complaint", "my account", "my transaction"))
    low_match = not matches or matches[0]["score"] < 0.12
    return asks_human or sensitive or low_match


llm = LLM(model=MODEL, api="responses", timeout=45, max_retries=1)
app = FastAPI(title="Fin Buddy FAQ Assistant", version="1.0.0")
app.mount("/static", StaticFiles(directory=Path(__file__).parent / "static"), name="static")


@app.get("/")
def home():
    return FileResponse(Path(__file__).parent / "static" / "index.html")


@app.get("/health")
def health():
    return {"status": "ok", "faq_count": len(FAQS)}


@app.post("/chat", response_model=ChatResponse)
def chat(body: ChatRequest) -> ChatResponse:
    message = body.message.strip()
    reason = safety_reason(message)
    if reason:
        return ChatResponse(
            response="I can’t help with that request. For private account matters, please use Fin Buddy’s verified support channel. The support contact is [NEEDS CONFIRMATION].",
            category="safety_or_security", confidence=1.0, escalated=True,
        )

    matches = rank_faqs(message)
    escalate = human_required(message, matches)
    if not matches:
        return ChatResponse(
            response="I don’t have enough information in the Fin Buddy FAQ to answer that accurately. This needs review by the Fin Buddy team; support contact details are [NEEDS CONFIRMATION].",
            category="unknown", confidence=0.0, escalated=True,
        )

    category_names = sorted({faq["category"] for faq in FAQS})
    sources = [{key: item.get(key) for key in ("id", "category", "question", "answer")} for item in matches]
    classifier = Agent(
        role="FAQ message classifier", goal="Classify the user question using FAQ categories only.",
        backstory="You classify Fin Buddy FAQ questions and never answer them.", llm=llm,
        allow_delegation=False, verbose=False,
    )
    researcher = Agent(
        role="FAQ knowledge researcher", goal="Select only relevant supported facts from provided FAQ records.",
        backstory="You may not add facts outside the supplied local FAQ records.", llm=llm,
        allow_delegation=False, verbose=False,
    )
    writer = Agent(
        role="Fin Buddy response writer", goal="Write a concise, warm, non-judgmental FAQ answer.",
        backstory="You use simple language and never provide personalized financial advice.", llm=llm,
        allow_delegation=False, verbose=False,
    )
    reviewer = Agent(
        role="Safety and escalation reviewer", goal="Check grounding and decide whether a human follow-up is needed.",
        backstory="You preserve safety limits and cannot invent support details.", llm=llm,
        allow_delegation=False, verbose=False,
    )
    t1 = Task(description=f"Classify this message into one of {category_names} or unknown. Message: {message}", expected_output="A structured classification.", agent=classifier, output_pydantic=Classification)
    t2 = Task(description=f"Select relevant facts from these FAQ records only: {json.dumps(sources, ensure_ascii=False)}", expected_output="Supported facts and source FAQ IDs; mark insufficient when unsupported.", agent=researcher, context=[t1], output_pydantic=Knowledge)
    t3 = Task(description="Draft a short answer using only the supported facts in the previous task. If insufficient, say so plainly.", expected_output="A grounded user-facing draft with source FAQ IDs.", agent=writer, context=[t1, t2], output_pydantic=Draft)
    t4 = Task(description=f"Review the draft for unsupported claims. Human escalation required by deterministic policy: {escalate}. Do not remove this escalation. Return the final answer.", expected_output="A safe final response, category, confidence, source FAQ IDs, and escalation flag.", agent=reviewer, context=[t1, t2, t3], output_pydantic=FinalDecision)
    result = Crew(agents=[classifier, researcher, writer, reviewer], tasks=[t1, t2, t3, t4], process=Process.sequential, verbose=False).kickoff()
    final = result.pydantic if result.pydantic else FinalDecision.model_validate_json(str(result))

    valid_sources = [faq_id for faq_id in final.source_faq_ids if faq_id in FAQ_BY_ID]
    # Deterministic grounding and escalation take precedence over agent output.
    # Use the selected FAQ answer verbatim to guarantee every product claim is grounded.
    factual_answer = matches[0]["answer"]
    valid_sources = [matches[0]["id"]]
    if escalate:
        factual_answer += " If you need help with your specific account or want a person to follow up, please contact Fin Buddy support; contact details are [NEEDS CONFIRMATION]."
    return ChatResponse(
        response=factual_answer, category=final.category if final.category in category_names else "unknown",
        confidence=max(0.0, min(1.0, float(final.confidence))), escalated=escalate,
        source_faq_ids=valid_sources,
    )

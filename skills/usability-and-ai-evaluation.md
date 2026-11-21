---
name: usability-and-ai-evaluation
description: Plan and evaluate Fin Buddy usability, accessibility, financial-answer correctness, grounding, trust, and safety. Use during Test; distinguish observed evidence from recommendations.
---

# Usability and AI Evaluation

Evaluate whether the experience works and whether financial answers are trustworthy.

## Evaluation layers

- Usability: task success, errors, time, comprehension, confidence, and recovery.
- Accessibility: keyboard, screen reader, contrast, focus, language, and cognitive load as applicable.
- Financial correctness: deterministic totals against a controlled golden dataset.
- Grounding: claims supported by authorized records and stated periods.
- Safety: unsupported advice, overconfidence, prompt injection, data exposure, and unauthorized actions.
- Trust: consent comprehension, evidence inspection, correction, and opt-out.

## Constraints

- Obtain appropriate consent and minimize sensitive test data.
- Never mix prototype behavior with production capability claims.
- Report sample limitations and contradictory findings.
- Rank issues using severity, evidence, affected users, and risk.

## Deliverable contract

Return a test plan, findings, issue register, metric results, recommendations, conclusion, and future concepts. Label it `DRAFT — REQUIRES HG-05 APPROVAL`.

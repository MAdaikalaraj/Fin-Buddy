# Phase 02 — Provisional Product Definition

**Artifact state:** DRAFT_FOR_REVIEW — REQUIRES HG-02 APPROVAL  
**Evidence status:** No participant research exists. All user needs and behaviors are provisional unless identified as a documented BRD requirement or project-owner decision.

## Evidence taxonomy

- **Project fact:** Approved intent recorded in the BRD or human gate.
- **Desk observation:** Dated competitor/help-source pattern; not a Fin Buddy user finding.
- **Owner decision:** Explicit project-owner instruction, including authorization to proceed provisionally.
- **Assumption:** Proposed user behavior, need, emotion, preference, or adoption expectation.
- **Unknown/dependency:** Current capabilities, data availability, jurisdiction, language, accessibility target, baseline, or operational owner.
- **Prohibited claim:** No user behavior or need may be called validated, common, frequent, or proven.

## Prioritized need hypotheses

### P0 — Foundational

1. Understand a spending or budget result quickly while retaining drill-down evidence.
2. Find and correct source data behind an answer.
3. Know which data is authorized, used, current, and retained.
4. Receive clarification or a limitation when intent or data is insufficient.
5. Distinguish general education from personalized regulated advice.
6. Complete core tasks accessibly and in plain language.

### P1 — Value building

1. Explore a savings contribution using editable assumptions.
2. Receive opt-in, dismissible proactive insights with an explanation.

### P2 — Research dependent

1. Multilingual or voice interaction after language, accessibility, and privacy validation.

## Provisional problem statement

Adults who actively monitor recurring finances may have difficulty turning transaction, category, and budget data into a timely explanation they can verify. Fin Buddy should test whether a consent-based, read-only conversational layer can reduce this interpretation effort by showing deterministic results, contributing records, periods, assumptions, and limitations while supporting correction, accessibility, and clear advice boundaries.

## Provisional How Might We

How might we help a Fin Buddy user ask a direct money question, verify the answer against authorized records, correct source data or interpretation, and retain control over permissions and history without implying unsupported financial advice?

## MVP definition

### Must-use cases

- UC-01 monthly spending summary
- UC-02 budget Q&A
- UC-03 transaction search
- UC-04 general financial education

### Must-have cross-cutting capabilities

- Discoverable, accessible entry point
- Scoped consent, withdrawal, and denial path
- Visible period, accounts, filters, assumptions, freshness, and limitations
- Deterministic financial calculations and inspectable contributing records
- Data/category correction and recalculation
- Clarify, retry, feedback, and insufficient-data responses
- Chat retention/deletion controls and AI opt-out
- Privacy-preserving monitoring and safe escalation
- Read-only enforcement

### Should

- UC-05 savings calculator with editable assumptions
- UC-06 opt-in and dismissible insight cards

### Could after validation

- UC-07 multilingual and voice support

### Out of scope

Payments, transfers, investing/trading, loan or credit decisions, account changes, tax/legal or personalized regulated advice, unauthorized third-party data, and unsupported real-time claims.

A use case must not enter detailed design until its required data source, calculation service, freshness, and permission model are identified.

## Provisional success measures

- Core task success: BRD-proposed target ≥80% on three later-validated tasks.
- Calculation correctness: BRD-proposed target ≥99% on an approved golden dataset.
- Grounded answers: BRD-proposed target ≥95% of answerable data questions linked to matching authorized context.
- Evidence comprehension: proposed ≥80% identify period, records, and assumptions without help.
- Correction recovery: proposed ≥80% correct a category/filter and recognize recalculation.
- Consent/control comprehension: proposed ≥80% explain scope and can withdraw/delete during testing.
- Accessibility: critical flows meet the selected target and assistive-technology acceptance criteria.
- Safety/privacy: zero critical unauthorized-action or data-exposure incidents.
- Engagement: establish a baseline; engagement cannot compensate for correctness, privacy, accessibility, or safety failures.

All targets remain provisional until owners, denominators, sources, and measurement timing are approved.

## Unresolved questions

- Which proto-persona/problem is primary after research?
- What product capabilities and screens exist today?
- Which fields exist, from which systems, with what freshness and coverage?
- What are the launch market, currency, languages, jurisdiction, and accessibility target?
- What is the qualified boundary between education and regulated advice?
- Who owns consent, retention/deletion, accessibility, support escalation, incidents, and analytics?
- What evidence and correction interactions are technically feasible?
- How will untrusted transaction text and model/provider data use be controlled?

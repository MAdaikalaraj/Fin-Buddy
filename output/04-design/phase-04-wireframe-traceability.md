# Phase 04 — Wireframe Traceability and Coverage

**Artifact state:** DRAFT_FOR_REVIEW — HG-04 CHECKPOINT A

## Use-case coverage

| Use case | Frames |
| --- | --- |
| UC-01 Spending | WF-01, 03–15, 19, 24–29 |
| UC-02 Budget | WF-02–16, 20, 24–29 |
| UC-03 Transaction search | WF-02–15, 21, 24–29 |
| UC-04 Education | WF-02, 16, 18, 22, 28–29 |
| UC-05 Savings | WF-02–16, 23, 24–29 |

## BRD coverage

| Requirement | Frames |
| --- | --- |
| BR-01 Entry/accessibility | WF-01–02 plus accessibility annotations |
| BR-02 Consent/withdrawal | WF-03–06, 25–26 |
| BR-03 Records/calculation | WF-07–09, 12, 15, 19–23 |
| BR-04 Scope/assumptions/evidence | WF-03, 08–09, 19–23 |
| BR-05 No invention/limitations | WF-10, 13–17 |
| BR-06 Education/advice boundary | WF-16, 18, 22–23 |
| BR-07 Correction/feedback | WF-10–12, 27 |
| BR-08 Privacy/retention/deletion | WF-03–06, 24–28 |
| BR-09 Accessibility/comprehension | Accessibility annotations across WF-01–30 |
| BR-10 Monitoring/incidents | WF-27–28 with minimal-data annotations |

## Required transitions

1. Direct screen → context preview → consent state → deterministic retrieval → grounded answer.
2. General education → personal request → new context/consent; never silent scope expansion.
3. Partial consent → supported partial answer/limitation; new scope returns to consent.
4. Answer → evidence → source correction → confirmation → recalculation → updated answer.
5. Answer → intent clarification → rerun, separate from source correction.
6. Stale/partial/conflicting state → refresh/narrow/direct source/support → rerun or exit.
7. Calculation/evidence failure → retry/direct/support; no AI arithmetic substitute.
8. Restricted/untrusted state → safe alternative/support/exit; no forbidden action.
9. Permission revoke → retrieval stop → education/exit; deletion is separate.
10. Delete → pending → success/partial/failure/retention exception.
11. Feedback → disclosed minimum capture → receipt/failure → continue/exit.
12. Exit → originating direct screen with preserved visible context.

## Dependencies carried forward

- Existing product navigation and supported direct screens
- Data model, APIs, provider scopes, freshness, reconciliation, currency/timezone rules
- Calculation service ownership/versioning
- Category correction/write and undo behavior
- AI provider, grounding, content-safety, and prompt-injection controls
- Consent basis, retention/deletion semantics, and human-review disclosure
- Jurisdiction, languages/currencies, accessibility target
- Support, compliance, privacy, security, incident, and content-governance owners

No dependency is represented as a confirmed production capability.

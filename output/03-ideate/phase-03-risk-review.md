# Phase 03 — Fintech Risk Review

**Artifact state:** DRAFT_FOR_REVIEW — REQUIRES HG-03 APPROVAL

| Risk | Severity | Required HG-03 control |
| --- | --- | --- |
| Data access before scoped consent | Critical | Protected retrieval only after visible authorization; education-only denial path |
| Bundled or dark-pattern consent | High | Separate AI data use, insights, history, analytics, and future voice scopes |
| Excess data exposure | High | Task-specific minimum data and explicit non-accessed data |
| AI performs financial arithmetic | Critical | Deterministic services own retrieval and calculations |
| No inspectable evidence | Critical | Period, currency, filters, assumptions, freshness, breakdown, and records route |
| Unsafe/irreversible correction | High | Clarify scope, confirm writes, allow retry/cancel, no silent mutation |
| Prompt injection from retrieved text | Critical | Treat records as untrusted; fixed read-only tools; explicit malicious-content state |
| Regulated/high-impact advice | Critical | Classify, limit/refuse, provide neutral education and qualified route |
| Inaccessible non-happy-path states | High | Keyboard, screen reader, focus, labels, non-color cues, plain language across every state |
| Ambiguous deletion/withdrawal | High | Separate chat deletion, retained history, permission withdrawal, and account deletion |
| Support leaks sensitive context | High | Explain destination, shared data, consent, expected response, and unavailable fallback |
| AI becomes only route | Medium–High | Preserve direct access to records, budgets, permissions, and support |
| Stale/partial/conflicting data treated as current | Critical | Freshness/reconciliation states; qualify or stop answer; never fabricate |
| Feedback captures sensitive content | High | Minimal events, redaction, notice, access and retention rules |
| Unconfirmed capabilities presented as live | High | Mark proposed dependencies; prohibit unsupported real-time claims |
| Scope expands to financial execution | Critical | Keep all BRD-excluded actions outside approved paths |

HG-03 approval may authorize provisional low-fidelity design only. It cannot authorize publication, live-data testing, high-fidelity design, or `output/`.

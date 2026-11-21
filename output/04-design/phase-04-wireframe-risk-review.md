# Phase 04 — Low-Fidelity Fintech Risk Review

**Artifact state:** DRAFT_FOR_REVIEW — HG-04 CHECKPOINT A  
**Review basis:** `phase-04-low-fidelity-wireframes.md` and `phase-04-wireframe-traceability.md`

## Result

The Markdown structural wireframes are sufficient for Checkpoint A. They provide concrete frames, annotations, transitions, and BRD/use-case traceability. High-fidelity visuals are not required for this review.

| Area | Result | Basis |
| --- | --- | --- |
| Inspectable wireframes | Pass | WF-01–30 with layouts and annotations |
| Consent hierarchy | Pass | Preview, granular unchecked scopes, neutral allow/manage/not-now/deny, alternatives |
| Deterministic calculation/evidence | Pass | WF-08/09/15 separate math, explanation, evidence, and failure |
| Prompt injection | Pass | WF-17 renders untrusted record text inertly |
| Restricted advice | Pass | WF-16 provides neutral boundary and safe route |
| Accessibility | Pass with conditions | Full annotation layer; target and assistive-technology matrix unresolved |
| History/permission/deletion | Pass | WF-24–26 separate controls and outcomes |
| Direct non-chat routes | Pass | WF-19–23 plus persistent direct navigation |
| Data-quality recovery | Pass | WF-13–15 distinguish stale/partial/missing/conflicting/failure states |
| Excluded actions | Pass with conditions | Structural CTAs preserve read-only scope; high fidelity must not expand it |
| Sensitive-data minimization | Pass with conditions | Masking/minimum-data rules present; must survive high fidelity |
| Correction/recalculation | Pass | Intent clarification and source correction remain distinct |
| Support/feedback privacy | Pass with conditions | Structure is safe; destinations, owners, and response expectations unresolved |
| Proactive insights | Conditional | WF-30 is safe, but the explicit opt-in acquisition transition must be added |
| Prototype truthfulness | Pass | Provisional/synthetic/non-production labels are explicit |

## Binding actions for high fidelity

1. Add an explicit transition showing how the user opts into proactive insights before WF-30 appears.
2. Preserve neutral hierarchy for `Not now` and `Deny`.
3. Keep unresolved duration, retention, deletion exceptions, export, and account-data semantics as placeholders pending qualified review.
4. Assign or retain dependencies for Legal/Compliance, Privacy/Security, Accessibility, Data/AI, Support, and content governance.
5. Define the accessibility target and assistive-technology matrix before final HG-04 approval.
6. Preserve masking and minimization on Home, insights, notifications, feedback, and support payloads.
7. Keep deterministic values, AI explanation, limitations, and evidence visually/semantically distinct.
8. Do not introduce transfers, payments, investing, loans, credit decisions, budget/account changes, or autonomous execution.
9. Do not promise access/export, undo, retention exceptions, or support behavior until confirmed.
10. Carry all traceability states into the prototype, including malicious text, restricted advice, partial consent, deterministic failure, deletion exceptions, and unavailable support.

## Recommendation

`APPROVED_WITH_ACTIONS` for high-fidelity design only. This does not authorize production claims, participant/live-data testing, final HG-04 approval, publication, or `output/`.

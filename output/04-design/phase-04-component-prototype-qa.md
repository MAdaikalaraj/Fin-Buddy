# Phase 04 — Component, Navigation, and Prototype QA

**Artifact state:** DRAFT_FOR_REVIEW — HG-04 FINAL DECISION REQUIRED

## Consistency rules

1. Use stable labels: Ask Fin Buddy, View evidence, Correct data, Change question, Manage permissions, Delete conversation, Turn off insights, and destination-specific Open actions.
2. Keep general information, observation, scenario, and personalized advice distinct.
3. Show period, currency, account scope, filters, freshness, and material limitations before secondary narrative.
4. Values, formulas, assumptions, and exclusions must match across answer, evidence, and direct screen.
5. Back/Close/Exit behavior exists on every overlay/dialog and returns focus logically.
6. Direct navigation remains available except during an active blocking confirmation.
7. Education never requests personal-data permission; personalization begins through context/consent.
8. Avoid urgency, shame, moral judgment, guarantees, “safe to spend,” and unsupported causal language.
9. Avoid full identifiers or sensitive totals on Home, insight, and notification surfaces.
10. Errors state what is known, affected, unavailable, and recoverable without blaming the user.

## Direct-route parity

| Use case | Required parity |
| --- | --- |
| UC-01 | Same period/accounts/filters/currency, total/category delta, freshness, evidence, and correction result in chat and spending report |
| UC-02 | Same planned/actual/remaining/overrun formula and exclusions; assistant never edits canonical budget |
| UC-03 | Natural-language interpretation becomes visible direct filters; count/order/detail match |
| UC-04 | Same reviewed source/version and advice boundary; no permission needed |
| UC-05 | Same inputs/formula/rounding/currency; manual mode remains; no unconfirmed save-goal promise |

Any mismatch in deterministic value, context, correction result, or permission state is a blocking defect.

## Prototype primary routes

1. Contextual spending: direct report → context → consent → loading → answer → evidence → correction → recalculation → direct report/return.
2. Hub budget: hub → context → existing/partial permission → budget answer → evidence → direct budget → return.
3. Transaction: ambiguity → clarification → deterministic search → direct results → correction → dependent-value update.
4. Education: education without consent → optional personalization through consent; restricted request to safe boundary.
5. Savings: manual calculation → optional prefill consent → edit/recalculate → no save-goal promise.
6. Proactive insight: PI-00 invitation → explanation/scope/consent → receipt → card → evidence/dismiss/mute/opt-out.

## Mandatory branches

- Partial, denied, deferred, expired, withdrawn, and failed consent
- Stale, partial, disconnected, conflicting, and mixed-currency data
- Deterministic calculation/evidence mismatch without AI substitute
- No results/no budget/no baseline
- Untrusted transaction text rendered inertly
- Restricted advice and prohibited execution request
- History off/resume/delete pending/success/partial/failure/retention exception
- Permission revoke separate from deletion
- Feedback for incorrect number, unsafe advice, and privacy
- Support payload review, consent, receipt, decline, and unavailable fallback
- Timeout, offline, cancellation, safe exit, and exact return-to-origin

## Accessibility prototype annotations

- Complete keyboard path and visible focus
- Focus return for overlays and confirmations
- Polite announcements for loading, answer ready, recalculation, deletion, and errors
- Error summary plus field association
- Non-color status and text/table alternatives
- 200% mobile text zoom and 400% web reflow where applicable
- Reduced-motion behavior
- Accessible names for all icon controls

## Prototype limitations disclosure

The prototype uses synthetic data and simulated system responses. It does not demonstrate live accounts, production APIs, real-time freshness, implemented deterministic services, security/compliance certification, or validated usability. Unsupported dependencies remain annotated.

## Open blocking dependencies

- Accessibility target and test matrix
- Consent duration and legal basis
- Retention/deletion/export/account-data semantics
- Support destination, owner, payload, response expectation, and outage fallback
- Calculation ownership/versioning/reconciliation/freshness/currency/timezone
- Category correction, write scope, and undo/rollback
- Existing navigation and actual product capabilities
- Reviewed education source/version and advice-boundary owner
- Exposed-surface masking and privacy-minimized analytics schema

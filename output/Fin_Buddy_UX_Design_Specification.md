# Fin Buddy AI Assistant — UX Design Specification

**INTERNAL PROVISIONAL — SPECIFICATION AND SYNTHETIC EVALUATION ONLY**

**Sharing:** Internal only. External publication requires separate human review and authorization.

## 1. Purpose

Define a provisional, read-only Fin Buddy AI experience that helps users understand spending, budgets, transactions, savings scenarios, and general financial concepts while preserving consent, evidence visibility, correction, accessibility, privacy, and safe boundaries.

This document is derived from the discovery-draft BRD, competitive desk research, assumption-based synthesis, architecture work, annotated Markdown wireframes, and specification reviews. It is not based on completed participant research.

## 2. Evidence status

- Product requirements and exclusions are documented project intent.
- Competitor patterns are dated desk observations, not Fin Buddy user findings.
- User behaviors, needs, emotions, and preferences remain hypotheses.
- Profiles are proto-personas, not validated personas.
- Future journeys and product behaviors are proposed, not implemented.

## 3. Provisional problem statement

Adults who actively monitor recurring finances may have difficulty turning transaction, category, and budget data into a timely explanation they can verify. Fin Buddy should test whether a consent-based, read-only conversational layer can reduce this interpretation effort by showing deterministic results, contributing records, periods, assumptions, and limitations while supporting correction, accessibility, and clear advice boundaries.

## 4. MVP scope

### Must

- Monthly spending summary
- Budget Q&A
- Transaction search
- General financial education
- Discoverable accessible entry
- Scoped consent and withdrawal
- Deterministic calculation and evidence drill-down
- Data/category correction and recalculation
- Clarification, retry, feedback, deletion, permission, support, and safe exit
- Privacy-preserving monitoring requirements

### Should

- Savings calculator with editable assumptions
- Opt-in, dismissible proactive insight cards

### Could after validation

- Multilingual and voice support

### Excluded

Transfers, payments, investing/trading, loans, credit decisions, autonomous budget/account changes, personalized tax/legal/regulatory advice, unauthorized third-party data, and unsupported real-time claims.

## 5. Provisional proto-personas

### Routine Spending Reviewer

Hypothesized goal: understand where money went, why spending changed, and which transactions matter. Needs visible periods, contributing records, correctable categories, and clear stale/partial-data handling.

### Household Budget Coordinator

Hypothesized goal: understand remaining/overrun amounts and household category changes. Needs deterministic formulas, neutral language, correction, and scoped permission.

### Goal-Oriented Financial Planning Newcomer

Hypothesized goal: understand concepts and explore savings scenarios. Needs editable assumptions, transparent calculations, education/advice boundaries, and no-guarantee language.

All three profiles are low-confidence assumptions pending research.

## 6. Selected architecture

Use a dual-path hybrid:

- Direct finance screens remain primary.
- Contextual assistance explains the visible task or screen.
- A global **Ask Fin Buddy** hub supports broader and multi-turn questions.
- Every assistant task retains a direct non-chat route where the underlying product supports it.
- Context is visible and editable before data retrieval.

### Proposed navigation

- Home
- Transactions
- Budget
- Goals
- Ask Fin Buddy
- Settings: data, permissions, history, deletion, insight controls, privacy, accessibility/preferences
- Help and support

Actual current product navigation remains to be confirmed.

## 7. Deterministic and AI responsibilities

| Responsibility | Required owner |
| --- | --- |
| Consent and authorization | Deterministic policy/application service |
| Retrieval, filtering, and search | Authorized deterministic data services |
| Totals, comparisons, budget/savings math, rounding, currency | Versioned deterministic calculation service |
| Evidence, provenance, and freshness | Deterministic data services |
| Intent interpretation | AI may propose structured intent; ambiguity/high risk requires confirmation |
| Explanation | AI constrained to supplied results; cannot alter values or invent causality |
| General education | Approved knowledge source with policy outside the model |
| Corrections/writes | Explicit confirmed action through canonical application service |

Financial arithmetic must never fall back to a generated estimate when the deterministic service fails.

## 8. Core interaction pattern

1. Enter from a direct screen or assistant hub.
2. Preview period, accounts, filters, and required data.
3. Request scoped permission only when protected data is needed.
4. Retrieve authorized records and freshness information.
5. Calculate deterministically.
6. Present result, scope, freshness, material limitation, and grounded explanation.
7. Provide evidence without requiring a new AI query.
8. Separate `Change question` from `Correct data`.
9. Recalculate through trusted services after an approved correction.
10. Offer direct route, feedback, permission controls, support, and safe exit.

General education must work without personal financial-data permission.

## 9. Required states

- Consent: required, selected, granted, partial, denied, deferred, expired, withdrawn, provider failure
- Data: fresh, stale, partial, missing, syncing, disconnected, duplicate/conflicting, mixed currency/timezone
- Intent: recognized, ambiguous, unsupported, restricted, malicious/untrusted record text
- Calculation: success, missing baseline, invalid input, error, evidence mismatch, recalculation
- Answer: grounded, limited, insufficient, stale/partial, explanation unavailable
- Correction: preview, confirm, applying, receipt, failure, unsupported
- Privacy: history on/off, deletion pending/success/partial/failure, retention exception, permission revoke
- Support: offered, accepted, declined, unavailable, receipt, safe return
- Proactive insight: opt-in invitation, scope, receipt, card, dismiss, mute, tune, opt-out

## 10. Trust and safety requirements

- Optional permissions are off by default.
- `Not now` and `Deny` remain clearly available.
- Denial preserves education and direct routes.
- Data use is task-specific and minimized.
- Account identifiers are masked unless full display is necessary.
- Every personalized financial answer exposes period, currency, filters, assumptions, freshness, coverage, and contributing records.
- Transaction descriptions are inert untrusted text and cannot alter tools, permissions, or scope.
- Restricted advice receives a neutral limitation and safe education/support route.
- Proactive insights require a separate opt-in and cannot silently re-enable.
- Deleting history, withdrawing permission, and requesting account-data deletion are distinct actions with distinct receipts.

## 11. High-fidelity system direction

### Visual intent

Calm, neutral, information-first. Evidence, scope, freshness, limitations, and controls outrank decorative or engagement content.

### Provisional tokens

- Canvas `#F6F8FC`; surface `#FFFFFF`
- Primary text `#172033`; secondary text `#475569`
- Essential boundary `#64748B`; strong boundary `#475569`
- Primary action `#075CBD`; focus ring `#7C3AED`
- Success `#176B43`; warning `#8A4B00`; danger `#B42318`

Actual token combinations require automated and manual contrast testing and brand reconciliation.

### Accessibility intent

- WCAG 2.2 AA contrast intent
- 44×44 px minimum target; 48×48 preferred for primary mobile actions
- Keyboard/switch operability and visible focus
- Programmatic headings, labels, errors, status announcements, and focus return
- Non-color communication and table/text alternatives to charts
- 200% text zoom and applicable 400% reflow
- Reduced motion and no essential animation

No conformance claim is made.

## 12. Representative synthetic content boundaries

- Role: “Fin Buddy can explain your money using data you choose. It can’t move money or make financial decisions for you.”
- Privacy: “Don’t enter passwords, PINs, or full account numbers.”
- Spending fixture: “You spent ₹8,899 more from 1–15 November than from 1–31 October.” The largest observed difference is Electronics (+₹6,500), followed by Dining (+₹1,200). Do not convert these observations into unsupported causal language.
- Budget fixture: “You are ₹600 over your Groceries budget through 30 November.” “You’ve used 110% of this category budget with 15 days remaining.” State that this is a calculation, not permission or advice.
- Savings: show inputs, formula, exclusions, and no-guarantee label.
- Education: label general information and synthetic examples.
- Restricted advice: explain the boundary without moralizing or repeating a risky recommendation.
- Failure: explicitly state when Fin Buddy will not estimate a missing number.

## 13. Prototype requirements

Cover contextual spending, hub budget, transaction search, education, savings, proactive opt-in, consent lifecycle, data-quality failures, deterministic failures, restricted advice, malicious record text, privacy/deletion, feedback/support, accessibility behavior, and exact return-to-origin.

All prototype content must be labeled synthetic and simulated. No live data, production service, security/compliance certification, or validated usability may be implied.

## 14. Mandatory limitations

No participant research, rendered prototype evaluation, production implementation, accessibility testing, model/security evaluation, live financial data, legal/compliance approval, or product feasibility confirmation has occurred. This specification is internal and provisional.

## 15. Source index

- `input/Fin_Buddy_AI_Assistant_BRD.md`
- `output/02-define/phase-02-product-definition.md`
- `output/02-define/phase-02-proto-personas-empathy.md`
- `output/02-define/phase-02-journey-map.md`
- `output/03-ideate/phase-03-information-architecture.md`
- `output/03-ideate/phase-03-task-conversation-flows.md`
- `output/04-design/phase-04-low-fidelity-wireframes.md`
- `output/04-design/phase-04-high-fidelity-specification.md`
- `output/04-design/phase-04-component-prototype-qa.md`
- `output/04-design/phase-04-final-risk-review.md`
- `gates/HG-00-project-intake.md` through `gates/HG-05-test-review.md`

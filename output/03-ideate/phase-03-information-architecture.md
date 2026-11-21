# Phase 03 — Information Architecture

**Artifact state:** DRAFT_FOR_REVIEW — REQUIRES HG-03 APPROVAL  
**Evidence status:** Provisional and not user-validated  
**Selected concept:** Dual-path hybrid assistant

## Concept

Provide a global **Ask Fin Buddy** destination plus contextual assistance within direct finance screens. Core tasks, financial records, permissions, and support must remain available without chat.

## Proposed navigation

- **Home:** Direct summaries, optional insights, global Ask Fin Buddy entry
- **Transactions:** Search/filter, transaction details, category correction, recurring items if supported
- **Budget:** Overview, category details, remaining/overrun, direct controls if supported
- **Goals:** Goal details and direct savings calculator if data exists
- **Ask Fin Buddy:** New question, guided starters, current conversation, evidence, history
- **Settings:** Connected data, AI permissions, history/retention/deletion, opt-out, accessibility/preferences, privacy, support
- **Help:** Assistant limits, reviewed education, reporting, escalation

Existing product navigation and capabilities remain unconfirmed.

## Assistant structure

- **Ask:** Composer, guided starters, visible context, period/accounts
- **Answer:** Verified result, grounded explanation, evidence summary, freshness, limitations
- **Evidence:** Contributing records, filters, deterministic method, exclusions
- **Correct:** Category/filter/period/account correction or intent clarification
- **Manage:** Feedback, history, deletion, permissions, help, and exit

## Entry points

- Global labeled entry on Home or primary navigation
- “Explain this spending” on a spending summary
- “Ask about this budget” on budget/category detail
- “Find a transaction” in Transactions
- “Explain this term” near financial education
- “Plan this goal” on Goals where supported
- Optional opt-in/dismissible insight card showing period, source, and freshness
- Recovery links for incomplete data, errors, and disputes

No assistant entry may be the only route to core records or controls. Every answer should link to the equivalent direct screen with matching context.

## Direct alternatives

| Use case | Non-conversational route |
| --- | --- |
| UC-01 | Spending report with period/account/category filters and drill-down |
| UC-02 | Budget/category view with planned, actual, remaining/overrun formula |
| UC-03 | Transaction filter/search/list/detail |
| UC-04 | Reviewed glossary/help and qualified-support route |
| UC-05 | Form-based calculator with editable assumptions |
| Privacy | Persistent settings for permissions, history, deletion, and opt-out |
| Correction | Canonical transaction/category correction flow |
| Support | Status, reconnect/refresh, and support route where applicable |

## Deterministic/AI boundary

| Responsibility | Owner |
| --- | --- |
| Consent enforcement and authorization | Deterministic policy/application service |
| Intent extraction | AI may propose structured intent; ambiguity/high risk requires confirmation |
| Retrieval, filtering, and search | Authorized deterministic services |
| Totals, comparisons, budget/savings math, rounding, currency | Deterministic calculation service |
| Evidence set, provenance, freshness | Deterministic data services |
| Explanation | AI constrained to supplied results; cannot alter values or invent causality |
| General education | Approved knowledge source with advice boundary enforced outside the model |
| Correction/write | Explicit confirmed action through canonical application service |
| Feedback/history/deletion/support | Application services with receipts and retention behavior |

## Architectural rules

- Preview and allow editing of context before data use.
- Never silently expand from screen context to broader financial data.
- Keep direct UI paths primary where efficient.
- Preserve the user’s place when moving between chat and direct screens.
- Keep MVP read-only and exclude transfers, payments, investing, loans, credit decisions, and autonomous account changes.

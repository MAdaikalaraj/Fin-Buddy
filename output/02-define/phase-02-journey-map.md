# Phase 02 — Provisional Journey and Service Map

**Artifact state:** DRAFT_FOR_REVIEW — REQUIRES HG-02 APPROVAL  
**Evidence status:** BRD-derived concept and hypotheses; not observed or usability tested.

## Hypothesized current-state journey

| Stage | Provisional activity | Potential breakdown | Opportunity | Dependency |
| --- | --- | --- | --- | --- |
| Trigger | Notices a balance, budget, category, or goal concern | Trigger may arrive late or without context | Timely, non-alarming entry | Fresh reconciled data |
| Locate | Opens a transaction list, dashboard, budget, or other tool | Information may be fragmented | Preserve task context | Current product/IA audit |
| Filter/compare | Selects dates, categories, or accounts | Wrong period, hidden filters, inconsistent categories | Make scope visible | Categorization and date logic |
| Interpret | Attempts to explain a total or variance | Correlation may be presented as cause | Explain contributing records conservatively | Deterministic aggregation |
| Decide | Considers adjusting spending, budget, or savings | Limited context may cause overreaction or inaction | Offer education and scenarios | Advice-boundary policy |
| Verify | Searches records or another source | Summary may not trace to evidence | Link claims to records | Evidence lineage |

Actual screens, sequence, frequency, and breakdowns remain unverified.

## Proposed future-state journey

| Stage | Proposed experience | Trust moment | Failure/recovery | Backstage responsibility |
| --- | --- | --- | --- | --- |
| Enter | User chooses a clearly labeled Fin Buddy AI entry | Role and limits are clear | Clarify that it is not a human/professional adviser | Product/UX, accessibility |
| Authorize | Explain exact data and request scoped consent | Purpose, scope, retention, withdrawal | Denial/partial consent leads to reduced mode or safe exit | Consent ledger, privacy/legal |
| Ask | User asks or selects a contextual prompt | User controls wording/scope | Clarify ambiguous dates, accounts, categories | Conversation layer, injection controls |
| Retrieve/calculate | Fetch authorized records and calculate deterministically | Totals are not invented by AI | Disclose missing, stale, duplicated, unreconciled data | Read-only APIs, reconciliation, calculator |
| Explain | Show result, period, contributors, assumptions, uncertainty | Explanation is proportionate | Reframe unsupported causal claims as observations | Grounded generation, content policy |
| Inspect | Open categories and contributing transactions | Independent verification | Correct/report misclassification | Evidence links, categorization owner |
| Correct/follow up | Edit category/filter/assumption or clarify | Recalculation is visible | Disclose persistence/scope of correction | State, correction workflow, audit trail |
| Explore next step | Review budget or savings scenario | Education and advice are distinguishable | Limit and escalate restricted requests | Scenario engine, compliance, support |
| Manage data | Rate, delete history, withdraw permission, or opt out | Control persists after answer | Confirm effect and timing | Privacy controls, deletion, monitoring |
| Exit/return | Leave with an understood result or limitation | No pressure to act or expand access | Opt in/out of future insights | Preferences, minimal analytics, incidents |

## Required alternate paths

- Consent denied or withdrawn
- Missing, stale, or partial data
- Incorrect category or duplicated transaction
- Ambiguous question
- Insufficient evidence for an answer
- Unsafe or regulated request
- Accessibility barrier
- Privacy/deletion request
- Suspected fraud, harmful advice, service failure, or support escalation

Every future-state behavior remains proposed until engineering, data, privacy, compliance, accessibility, and support owners confirm it.

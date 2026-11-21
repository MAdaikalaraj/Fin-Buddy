# Phase 03 — Task and Conversation Flows

**Artifact state:** DRAFT_FOR_REVIEW — REQUIRES HG-03 APPROVAL  
**Scope:** Flow logic, not final interface or copy

## Shared response anatomy

1. Interpreted request and visible scope
2. Concise answer or limitation
3. Period, sources, filters, and freshness
4. Deterministic calculation or approved knowledge type
5. Supporting evidence
6. Assumptions and uncertainty
7. Inspect, correct, refine, direct UI, feedback, permission, help, or exit
8. Advice boundary where applicable

## UC-01 — Monthly spending summary

Entry → confirm period/accounts/currency/exclusions → consent check → authorized retrieval/freshness → deterministic totals and category deltas → grounded explanation → show evidence → correction/filter change → deterministic recalculation → direct report/feedback/exit.

Branches: no records, stale/partial/disconnected data, no comparison period, mixed currency, ambiguous period, calculation failure, evidence unavailable.

## UC-02 — Budget Q&A

Entry → resolve budget/category/period → clarify ambiguity → permission/freshness → deterministically calculate planned, actual, remaining/overrun → show formula and source records → correct/filter/recalculate → direct Budget/exit.

Branches: no budget, incorrect category, excluded transfers, stale income, unavailable forecast, unsafe personalized advice. The assistant never silently changes a budget.

## UC-03 — Transaction search

Direct search or Ask → AI proposes structured filters → confirm ambiguity → deterministic authorized search → show applied filters and direct results → open details → correct category through approved route → update dependent summaries → direct Transactions/exit.

Branches: zero results, multiple matches, hidden/excluded records, pending/duplicate/refund, unavailable account, unsupported query. Never invent a missing transaction.

## UC-04 — General financial education

Entry → classify general vs personalized/data-backed → general education without financial-data permission → disclose educational scope and reviewed source where available → glossary/support/exit. Personalized data triggers separate scoped permission; restricted/high-impact requests trigger limitation and qualified support.

## UC-05 — Savings scenario

Enter target/date/current amount and assumptions → consent only for optional data prefill; manual mode remains → deterministic contribution calculation → show formula/rounding/currency/timing → edit assumptions/recalculate → compare scenarios → direct goal/calculator/exit.

Saving or changing a goal is allowed only if a separately approved write capability exists and the user explicitly confirms it.

## Consent flow

1. Trigger only when personal data is required.
2. Explain purpose and requested scopes in plain language.
3. Show accounts, data types, use, freshness, and history/retention behavior.
4. Offer granular allow, manage, deny, and Not now with no preselected optional scope.
5. Record version, time, and scope; provide persistent permission access.
6. Re-prompt only for new or expired scope.
7. Denial preserves education and direct product routes.
8. Withdrawal stops retrieval and is distinguished from deletion.

## Secondary flows

- Visible context chips for follow-up scope
- Correct my data with confirmation and recalculation
- Clarify my question by editing interpreted intent
- Minimal-data feedback with human-review disclosure
- Inspect/revoke one or all permissions
- Delete a conversation with accurate pending/success/failure states
- Escalate using minimum diagnostic context and user consent
- Exit without losing the originating direct-task context

## Required state inventory

- First/returning use
- Consent required, selected, granted, partial, denied, deferred, expired, withdrawn, or provider failure
- Education-only mode
- Loading, timeout, offline, service unavailable, cancel
- Fresh, stale, partial, missing, duplicated/conflicting, syncing, mixed-currency, hidden/excluded data
- Recognized, ambiguous, unsupported, restricted, or malicious/prompt-injected intent/content
- Deterministic calculation success, failure, invalid input, missing baseline, recalculation
- Grounded, limited, insufficient, stale/partial, or explanation-unavailable answer
- Evidence drill-down, correction, retry, report, feedback
- History on/off, deletion pending/success/partial/failure, permission revoke, retention exception
- Support offered/accepted/declined/unavailable and safe return
- Proactive insight opt-in, dismiss, mute, opt-out
- Keyboard focus, screen-reader announcement, reduced motion, reflow, contrast, plain-language alternative, and associated errors

## Flow traceability fields

Every detailed flow must record BRD/use case, entry and consent state, minimum data/purpose, trusted service, AI boundary, evidence, correction/recovery, accessibility, privacy/retention, escalation owner, prototype assumption, and exclusion check.

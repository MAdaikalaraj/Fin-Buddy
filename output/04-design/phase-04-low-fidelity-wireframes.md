# Phase 04 — Annotated Low-Fidelity Wireframes

**Artifact state:** DRAFT_FOR_REVIEW — HG-04 CHECKPOINT A  
**Scope:** Structural wireframes only; no high-fidelity styling, final copy, production behavior, or usability claims  
**Design basis:** HG-03-approved dual-path hybrid

## Frame inventory

| ID | Frame | Required content/behavior |
| --- | --- | --- |
| WF-01 | App shell/Home | Direct navigation, labeled global Ask entry, optional/dismissible insight placeholder |
| WF-02 | Assistant hub | Role/read-only disclosure, guided starters, open input, history/permission/help links, direct alternatives |
| WF-03 | Context preview | Origin, period, accounts, filters, minimum data, edit/cancel before retrieval |
| WF-04 | Consent overview | Purpose, task-specific data, history/retention impact, education/direct alternative |
| WF-05 | Scope selection | Granular scopes, neutral Allow/Manage/Deny/Not now, no optional preselection |
| WF-06 | Consent outcomes | Granted, partial, denied, deferred, expired, withdrawn, provider failure, education-only route |
| WF-07 | Loading/cancel | Retrieval/calculation/explanation stages, cancel, timeout/offline/service unavailable |
| WF-08 | Grounded answer | Deterministic value, interpreted request, period/currency/accounts/filters, freshness, limitations, evidence/correct/direct/feedback/exit |
| WF-09 | Evidence | Method/formula, assumptions/exclusions, contributing records, filters, source/freshness, authoritative-record notice |
| WF-10 | Intent clarification | Editable interpretation of period/account/category/merchant/goal before rerun |
| WF-11 | Data correction | Canonical record/category edit, impact preview, confirm/cancel, write limitation |
| WF-12 | Recalculation | Before/after value, changed records/context, success/failure/retry/rollback if supported |
| WF-13 | Data quality | Distinct stale, partial, missing, syncing, disconnected, duplicate/conflicting, mixed-currency/timezone states |
| WF-14 | Empty/no result | No records, no budget/baseline, zero matches; editable filters/direct/manual route |
| WF-15 | Calculation/evidence failure | Deterministic error or mismatch; never replace with AI arithmetic |
| WF-16 | Restricted request | Advice boundary, prohibited action, safe education/qualified route, exit |
| WF-17 | Untrusted record text | Inert rendering of instruction-like transaction content; no scope/tool/action change |
| WF-18 | General education | Reviewed knowledge, synthetic example, no financial-data consent, safe transition to personalization |
| WF-19 | Direct spending report | Filters, total/category comparison, evidence, freshness, direct correction |
| WF-20 | Direct budget | Planned/actual/remaining/overrun, formula, source records, no silent edits |
| WF-21 | Direct transaction search | Filters, results/details, pending/refund/duplicate/hidden states, correction |
| WF-22 | Direct help/glossary | Reviewed education, limitations, qualified support |
| WF-23 | Direct savings calculator | Manual inputs, formula, rounding/timing/currency, edit/recalculate, optional prefill consent |
| WF-24 | History | History on/off, list/resume/delete, retention disclosure |
| WF-25 | Permissions/privacy | Current scopes/accounts, revoke one/all, AI/insight opt-out, data access/export where supported |
| WF-26 | Delete flow | Conversation vs history vs permission vs account data; pending/success/partial/failure/retention exception |
| WF-27 | Feedback | Structured reason, optional-text warning, human-review disclosure, privacy/unsafe/incorrect routes |
| WF-28 | Support | Issue, data to share, consent/minimization, response expectation, unavailable fallback, receipt |
| WF-29 | Exit/return | Preserve origin, filters, selected item; timeout/history handling per policy |
| WF-30 | Proactive insight | Explicit opt-in, dated/source/freshness, dismiss/mute/opt-out, explanation/evidence |

## WF-02 — Assistant hub

```text
┌─────────────────────────────────┐
│ [Back]  Fin Buddy AI      [Help]│
│─────────────────────────────────│
│ [Role + read-only disclosure]   │
│ [Permissions] [History]         │
│                                 │
│ Choose a task                   │
│ [Review spending]               │
│ [Check a budget]                │
│ [Find a transaction]            │
│ [Explore a savings scenario]    │
│ [Learn a financial concept]     │
│                                 │
│ [Question input]       [Submit] │
│ [Input/privacy explanation]     │
│─────────────────────────────────│
│ [Home] [Transactions] [Budget]  │
└─────────────────────────────────┘
```

- Direct navigation remains available.
- General education never triggers financial-data consent.
- Suggested tasks are labeled buttons, not the only method of entry.
- No real account content appears in the empty state.

## WF-03 — Context preview

```text
┌─────────────────────────────────┐
│ Origin: [screen/category/budget]│
│ Proposed context                │
│ Period: [value]          [Edit] │
│ Accounts: [masked scope] [Edit] │
│ Filters: [summary]       [Edit] │
│ Data needed: [minimum set]      │
│                                 │
│ [Continue] [Use manual mode]    │
│ [Cancel and return]             │
└─────────────────────────────────┘
```

- No retrieval occurs before context and authorization checks.
- Cancel returns to the exact originating state without permission change.
- Mask identifiers unless full display is essential.

## WF-05 — Granular consent

```text
┌─────────────────────────────────┐
│ Task: [selected task]           │
│ Purpose: [task-specific]        │
│                                 │
│ Requested data                  │
│ [ ] Transactions: [scope]       │
│ [ ] Categories                  │
│ [ ] Budget data (optional)      │
│                                 │
│ Duration: [approved options]    │
│ History/retention: [summary]    │
│ [View details / withdrawal]     │
│                                 │
│ [Allow selected] [Manage]       │
│ [Not now] [Deny and exit]       │
└─────────────────────────────────┘
```

- Optional scopes start unselected.
- Neutral visual hierarchy; denial remains useful through education/manual/direct routes.
- Permission and conversation retention are separate concepts.

## WF-08 — Grounded spending answer

```text
┌─────────────────────────────────┐
│ Spending comparison             │
│ [Concise observed result]       │
│ Period: [A vs B]         [Edit] │
│ Accounts: [masked]       [Edit] │
│ Freshness/coverage: [status]    │
│─────────────────────────────────│
│ Deterministic result            │
│ [total / difference]            │
│ AI explanation of supplied data │
│ [grounded observation only]     │
│ Material assumptions/limits     │
│─────────────────────────────────│
│ [View evidence]                 │
│ [Correct data] [Change question]│
│ [Open spending] [Feedback]      │
│ [Manage permission] [Exit]      │
└─────────────────────────────────┘
```

- Deterministic values are visually and semantically distinguished from generated explanation.
- Material limitations remain visible without opening evidence.
- Status is expressed with text, not color alone.

## WF-09 — Evidence

```text
┌─────────────────────────────────┐
│ Evidence for [answer]           │
│ Formula/method: [deterministic] │
│ Period/accounts/filters         │
│ Assumptions and exclusions      │
│ Freshness/source coverage       │
│─────────────────────────────────│
│ Contributing records            │
│ [date] [merchant] [amount]      │
│ [date] [merchant] [amount]      │
│ [date] [merchant] [amount]      │
│ [Filter/sort/load more]         │
│─────────────────────────────────│
│ [Open canonical transaction]    │
│ [Report/correct category]       │
│ [Return to answer]              │
└─────────────────────────────────┘
```

- Merchant/transaction descriptions are inert, untrusted text.
- Evidence remains reachable without asking another AI question.
- List position/count and dynamic loading are announced accessibly.

## WF-10 and WF-11 — Distinct clarification and correction

```text
Clarify interpreted question       Correct source data
┌────────────────────────────┐    ┌────────────────────────────┐
│ Period [edit]              │    │ Record [date/amount/name]  │
│ Accounts [edit]            │    │ Current category [value]   │
│ Category/merchant [edit]   │    │ Proposed category [select] │
│ Intent [structured choice] │    │ Scope [this record/rule*]  │
│ [Rerun] [Cancel]           │    │ Impact [before → after]    │
└────────────────────────────┘    │ [Confirm service] [Cancel] │
                                  └────────────────────────────┘
```

- Intent correction never silently edits transaction data.
- Data correction uses the canonical product service and explicit confirmation.
- `*` Future rules appear only if supported and separately approved.

## WF-13 and WF-15 — Data/calculation limitations

```text
┌─────────────────────────────────┐
│ [Specific status: stale/partial/│
│  conflicting/calculation failed]│
│ Last successful refresh: [time] │
│ Included: [sources]             │
│ Missing/affected: [sources/math]│
│ Result usability: [none/limited]│
│                                 │
│ [Retry/refresh] [Narrow scope]  │
│ [Inspect available records]     │
│ [Open direct source] [Support]  │
│ [Exit]                          │
└─────────────────────────────────┘
```

- No definitive result when missing data could materially change it.
- A failed deterministic calculation is never replaced with an AI estimate.
- Stale, partial, missing, and conflicting states use specific labels.

## WF-16 — Restricted request

```text
┌─────────────────────────────────┐
│ [Clear capability/advice limit] │
│ [Why the request is restricted] │
│ [General education, if safe]    │
│ [Qualified support route]       │
│                                 │
│ [Reframe question] [Get help]   │
│ [Return] [Exit]                 │
└─────────────────────────────────┘
```

- Neutral, non-alarmist, and non-moralizing.
- No investment pick, credit decision, tax/legal conclusion, guarantee, transfer, payment, or account change.

## WF-17 — Malicious/untrusted transaction text

```text
┌─────────────────────────────────┐
│ Transaction record              │
│ Date/amount/category            │
│ Description: [inert plain text] │
│ [Suspicious/malformed-data note]│
│                                 │
│ [Open canonical record]         │
│ [Report record text]            │
│ [Return to evidence]            │
└─────────────────────────────────┘
```

- Embedded instructions, links, markup, or secret requests cannot execute.
- Record text cannot expand permissions, tool calls, or calculation scope.
- Reporting does not expose internal security details.

## WF-18 — Education without consent

```text
┌─────────────────────────────────┐
│ General-information label       │
│ Concept summary                 │
│ Key points/trade-offs           │
│ Synthetic example label         │
│ Limitations / qualified help    │
│                                 │
│ [Related concept]               │
│ [Ask general question] [Exit]   │
└─────────────────────────────────┘
```

- No account permission is requested.
- Personalization begins only through a new context/permission preview.

## WF-20 — Budget answer/direct view

```text
┌─────────────────────────────────┐
│ Category + budget period [Edit] │
│ Planned / Actual / Remaining    │
│ Time remaining                  │
│ Formula + freshness             │
│ Included records / exclusions   │
│                                 │
│ [View evidence] [Correct data]  │
│ [Open direct budget]            │
│ [Explore scenario—not edit]     │
│ [Exit]                          │
└─────────────────────────────────┘
```

- The assistant never changes the budget.
- A scenario is visually distinct from canonical editing.

## WF-21 — Transaction search

```text
┌─────────────────────────────────┐
│ Merchant/text [field]           │
│ Date/amount/category/accounts   │
│ [Search] [Clear] [Exit]         │
│─────────────────────────────────│
│ Result count + applied filters  │
│ [record → canonical detail]     │
│ [record → canonical detail]     │
│ [Load more]                     │
└─────────────────────────────────┘
```

- Zero results shows scope, filters, freshness, and editable alternatives.
- Never claim a record does not exist outside authorized sources.

## WF-23 — Savings scenario

```text
┌─────────────────────────────────┐
│ Target amount/date              │
│ Starting amount [manual/source] │
│ Frequency + assumptions         │
│ [Calculate] [Cancel]            │
│─────────────────────────────────│
│ Deterministic contribution      │
│ Formula/inputs/rounding/currency│
│ Education/no-guarantee label    │
│ [Edit] [Compare scenario]       │
│ [Open goal] [Exit]              │
└─────────────────────────────────┘
```

- Manual mode remains available.
- Result is a scenario, not a recommendation or guarantee.

## WF-24–26 — History, permission, and deletion separation

```text
┌─────────────────────────────────┐
│ Data permissions                │
│ [scope/duration] [Change/Revoke]│
│ Conversation history            │
│ [on/off] [retention] [Manage]   │
│ [conversation] [Delete]         │
│ [Delete eligible history]       │
│ Account/app data                │
│ [Separate account-data route]   │
└─────────────────────────────────┘
```

- Each destructive action names exact scope, exceptions, time, and reversibility.
- Pending, success, partial, failure, and retention-exception receipts are distinct.
- Withdrawing permission stops retrieval but does not falsely imply historical deletion.

## WF-27–28 — Feedback and support

```text
Feedback                         Support
┌──────────────────────────┐    ┌────────────────────────────┐
│ Helpful? [Yes/No]        │    │ Issue type                 │
│ [Incorrect number]       │    │ Data proposed to share     │
│ [Unsafe advice]          │    │ [Edit/minimize]             │
│ [Privacy concern]        │    │ Expected response/fallback  │
│ Optional comment warning │    │ [Consent + create request]  │
│ [Submit] [Cancel]        │    │ [Decline] [Safe return]     │
└──────────────────────────┘    └────────────────────────────┘
```

- Feedback uses minimal diagnostic data and does not alter financial records.
- Support does not imply professional financial counseling.

## WF-30 — Proactive insight

```text
┌─────────────────────────────────┐
│ Optional insight                │
│ Period/source/freshness         │
│ Neutral observation             │
│ [Explain] [View evidence]       │
│ [Dismiss] [Mute] [Turn off]     │
└─────────────────────────────────┘
```

- Explicit opt-in, non-alarmist language, easy dismissal and opt-out.
- No urgency, shame, or sensitive detail on exposed overview surfaces.

## Accessibility annotation applied to all frames

- Logical headings, landmarks, reading order, and focus order
- Accessible names and associated instructions/errors
- Keyboard/switch access and visible focus
- Polite status announcements for retrieval and recalculation
- Managed focus for consent, deletion, and error dialogs
- Non-color-only states; plain-language alternatives to charts
- Zoom/reflow, scalable text, reduced motion, and touch-target intent
- Evidence-list position/count and dynamic-load announcements
- Synthetic/provisional labels in text

The target standard and assistive-technology test matrix remain human dependencies.

## Prototype coverage required after Checkpoint A

Contextual path: direct screen → context preview → consent → loading → grounded answer → evidence → correction → recalculation → return to origin.

Hub path: hub → guided setup → context → consent if needed → conversation → task answer/evidence → follow-up/direct UI → feedback → exit.

Branches: education without consent, partial permission, stale/partial data, deterministic failure, restricted advice, excluded action, untrusted record text, no results, history deletion, permission withdrawal, support, and safe exit.

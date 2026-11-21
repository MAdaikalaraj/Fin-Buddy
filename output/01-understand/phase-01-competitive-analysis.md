# Phase 01 — Competitive Experience Analysis

**Artifact state:** DRAFT_FOR_REVIEW — REQUIRES HG-01 APPROVAL  
**Method:** Official public product, help, privacy, and accessibility pages  
**Access date:** 2026-11-15 IST  
**Limitations:** No authenticated accounts were used. Region, plan, and release differences were not independently tested. Marketing statements are treated as claims, not observed functionality.

The supplied Fin Buddy Behance page was not retrievable through the research tool. Its screenshot and process are project-owner references, not evidence of current live functionality.

## Comparison

| Product | Observable patterns | Evidence and correction | Control/privacy | Limitations |
| --- | --- | --- | --- | --- |
| Monarch Money | Optional AI assistant uses financial context for spending, cash flow, net worth, subscriptions, and overspending. Current views can supply date/filter/account context. | AI may be inaccurate; users can rephrase, follow up, and provide feedback. | AI opt-out, conversation deletion, read-only boundaries, no payments/trading. | No authenticated verification; no explicit technical accessibility statement found in reviewed sources. |
| Rocket Money | Budget estimates income, bills, and categories from linked transactions; transaction search and category review are documented. | Users can view contributing transactions, edit figures, correct categories, and create rules. | Privacy access/deletion/correction rights and account deletion are documented. | No conversational AI observed in reviewed help; no explicit technical accessibility statement found. |
| Cleo | Conversational, plain-language guidance using spending and account context; category budgets and goals are described. | Users can recategorize, create categories, exclude transactions, hide accounts, and reconnect accounts. | Read-only Plaid access and account deletion are documented; support may route to humans. | No clear public evidence-drilldown pattern for AI answers found. “Accessible” marketing language is not a WCAG claim. |
| Google Wallet | Transaction search by business, amount, date/period, category, and refund; some data may be unavailable. | Bank statements are identified as authoritative when coverage is incomplete. | History, personalization, deletion, export, and retention controls are documented. | Not a budgeting or conversational-AI product; used as privacy, search, and accessibility analogue. |

## Sources

### Monarch Money

- https://help.monarch.com/hc/en-us/articles/360048393272-Getting-Started-with-Monarch
- https://help.monarch.com/hc/en-us/articles/16116906962452-About-Monarch-s-AI-Features

### Rocket Money

- https://help.rocketmoney.com/en/articles/2649810-creating-a-budget
- https://help.rocketmoney.com/en/articles/10770688-searching-my-transactions
- https://help.rocketmoney.com/en/articles/13778317-transaction-category-review
- https://help.rocketmoney.com/en/articles/8008211-rocket-money-privacy-rights
- https://help.rocketmoney.com/en/articles/934679-how-to-delete-your-rocket-money-account

### Cleo

- https://web.meetcleo.com/uk
- https://web.meetcleo.com/faqs/en/articles/3335175-why-is-cleo-showing-me-the-wrong-info
- https://web.meetcleo.com/faqs/en/articles/9104662-how-do-i-manage-my-accounts-in-cleo
- https://web.meetcleo.com/faqs/en/articles/1354571-how-do-i-delete-my-cleo-account
- https://web.meetcleo.com/page/privacy-policy

### Google Wallet

- https://support.google.com/wallet/answer/13623624
- https://support.google.com/wallet/answer/16703349
- https://support.google.com/googlepay/answer/9015738
- https://support.google.com/wallet/answer/16244062

## Inferences

- Trust is likely stronger when an estimate links to contributing transactions and remains editable.
- An AI layer can inherit current filters, dates, and accounts, but should make that context visible and editable.
- Correction should address both source data and AI interpretation.
- Read-only and “cannot move money” are useful MVP boundaries, but Fin Buddy must verify actual provider/API behavior.
- Sparse public accessibility documentation is not evidence that a product is inaccessible.

## Fin Buddy opportunities

1. Show period, accounts, filters, assumptions, and a “View contributing transactions” action for every data-backed answer.
2. Permit category correction and immediate recalculation.
3. Use explicit scoped consent before the first data-backed answer.
4. Combine connected-account controls, freshness, disconnect/hide, chat deletion/retention, and AI opt-out in one control area.
5. Provide “Correct my data” and “Clarify this answer” recovery paths.
6. Warn about stale, partial, or disconnected data and identify authoritative records.
7. Keep the assistant read-only and prohibit payments, trading, and transfers.
8. Adopt a declared accessibility target and test screen readers, keyboard use, contrast, zoom, reduced motion, and plain language.

## Remaining gaps

Authenticated product flows, Indian-market comparators, and the Behance case study still require human-access review. This document is desk research, not user research.

# Phase 05 — Synthetic Evaluation Results

**Artifact state:** DRAFT_FOR_REVIEW — REQUIRES HG-05 APPROVAL  
**Evaluation date:** 2026-11-15  
**Data:** Fictional transactions and budgets only

## Executed checks

Harness: `tests/verify-golden-dataset.ps1`  
Transactions: `tests/synthetic-transactions.csv`  
Budgets: `tests/synthetic-budgets.csv`

**Result:** 35 passed, 0 failed.

| Group | Verified assertions |
| --- | --- |
| AR-01/02 | October and November spending and category totals |
| AR-03 | Month difference and rounded percentage |
| AR-04 | Total/category budget variance |
| AR-05 | Merchant/category search count, IDs, and totals |
| AR-06 | Savings contribution scenarios |
| AR-07 | Category correction preserves total and changes category variances correctly |
| AR-08 | Excluding the untrusted-text record updates totals deterministically |
| AR-09 | Stale-through-date subtotal |
| AR-10 | Partial-account subtotal |
| AR-11 | Currency separation and explicitly stated-rate conversion |
| AR-12 | Malicious-looking description remains exact fixture text with numeric fields intact |

## Expected core results

- October INR spending: ₹31,799
- November INR spending: ₹40,698
- Difference: ₹8,899 / 27.99%
- November budget: ₹39,500; overrun ₹1,198
- Green Grocer November: two records / ₹6,600
- Savings: ₹48,000 remaining across six months = ₹8,000 per month
- After N08 Electronics→Groceries correction: total stays ₹40,698; Groceries ₹13,100; Electronics ₹0
- Through 12 November subtotal: ₹30,699
- Missing CARD-02 available subtotal: ₹33,198, never a complete total
- Mixed currency remains INR ₹40,698 and USD $20 unless an explicit deterministic rate is provided

## Structural test requirements not executed

- Grounding of generated answers to the fixture evidence
- Chat/direct/evidence parity in an interactive prototype
- Consent enforcement and permission persistence
- Prompt-injection isolation beyond treating fixture text as data
- Unsafe-advice and excluded-action model behavior
- Keyboard, screen-reader, contrast, zoom/reflow, motion, and responsive implementation
- Retention, deletion, export, support routing, notification delivery, or incident monitoring
- Production data services, reconciliation, calculation versioning, or authorization

No unexecuted item is marked passed.

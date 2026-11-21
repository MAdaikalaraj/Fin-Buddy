# Phase 05 — Specification-Based Usability Evaluation

**Artifact state:** DRAFT_FOR_REVIEW — REQUIRES HG-05 APPROVAL  
**Method:** Expert cognitive walkthrough and state/branch audit  
**Not performed:** Participant, rendered-prototype, assistive-technology, model, security, or production testing

## Rating meaning

- **Pass by specification:** Required behavior exists in the documents; implementation/usability is unproven.
- **Partial:** Required structure exists but material policy/dependency is unresolved.
- **Untested:** Requires an interactive/rendered or implemented system.

## Use-case results

| Use case | Specification result | Key remaining risk |
| --- | --- | --- |
| UC-01 Spending summary | Partial | Consent duration, data-completeness suppression, canonical correction unresolved; accessibility untested |
| UC-02 Budget Q&A | Partial | Pace/remaining language may imply permission to spend; incomplete-data policy unresolved |
| UC-03 Transaction search | Pass by specification | Matching/normalization/performance/accessibility untested |
| UC-04 Education | Partial | Jurisdiction-approved advice boundary and comprehension unresolved |
| UC-05 Savings scenario | Pass by specification | Assumption completeness and user interpretation untested |

## Critical branch results

| Branch | Result |
| --- | --- |
| Denied/partial consent | Pass by specification |
| Withdrawal | Partial; backend timing untested |
| History deletion | Partial; retention exceptions/timing unresolved |
| Stale/partial/conflicting data | Partial; materiality/suppression policy unresolved |
| Deterministic failure | Pass by specification; no AI substitute allowed |
| Restricted advice | Partial; jurisdictional policy unresolved |
| Excluded financial action | Pass by specification |
| Prompt-injected record text | Pass by specification; enforcement/security untested |
| Feedback/support/exit | Pass by specification; actual operations untested |
| Proactive insight opt-in | Partial; triggers/cadence/urgency policy unresolved |

## Accessibility conclusion

The specification defines contrast intent, non-color communication, target size, keyboard use, focus management, status announcements, form errors, zoom/reflow, reduced motion, direct controls, and text alternatives. Actual contrast, keyboard order, screen-reader behavior, zoom/reflow, responsive layout, target size, and comprehension remain untested. No accessibility conformance claim is permitted.

## Issue register

### S1 — High

1. Consent duration and history-retention policy unresolved.
2. Materiality/suppression rules for stale, partial, duplicate, and unreconciled data undefined.
3. Advice-boundary and qualified-support routes lack jurisdiction approval.
4. Prompt-injection protection exists only as design intent, not system enforcement.
5. End-to-end deletion and revocation cannot be verified.
6. Proactive insight thresholds, frequency, and urgency policy unresolved.
7. No rendered/implemented accessibility evidence.

### S2 — Medium

1. Canonical category correction, persistence, and undo unresolved.
2. Transaction matching/normalization unspecified.
3. Direct-product route availability assumed.
4. Financial result wording may imply affordability or causality.
5. Savings assumptions need a confirmed calculation model.
6. Privacy-minimized analytics/feedback schema undefined.
7. Long evidence/thread navigation remains an accessibility and comprehension risk.

### S3 — Low

1. Distinguish refresh time, posting date, and calculation time.
2. Localize permission and task labels without losing scope meaning.
3. Standardize Back, Close, Dashboard, and Return-to-origin behavior.

## Conclusion

The specification is coherent enough to support a rendered synthetic prototype and formal evaluation, but it is not evidence of tested usability, trust, accessibility, safety, security, compliance, or production readiness.

# Phase 01 — Fintech Research Risk Register

**Artifact state:** DRAFT_FOR_REVIEW — REQUIRES HG-01 APPROVAL  
**Reviewer:** Fintech Risk Reviewer  
**Decision authority:** Human HG-01 approver

| ID | Risk | Severity | Required mitigation | Proposed owner | HG-01 condition |
| --- | --- | --- | --- | --- | --- |
| R-01 | Research without meaningful consent, withdrawal, or retention rules | High | Plain-language consent, separate recording consent, withdrawal, access, retention, deletion, and escalation | UX Research + Privacy | Approve consent/data-handling plan before sessions |
| R-02 | Accidental disclosure of credentials or identifiable financial data | High | “Do not share” instruction, synthetic scenarios, moderator stop rule, immediate redaction | UX Research + Privacy | Add stop/redaction rules and deletion timeline |
| R-03 | Synthetic scenarios mistaken for real evidence | High | Label every scenario and keep an evidence taxonomy | UX Research + Product | Separate participant evidence, desk research, stakeholder input, and assumptions |
| R-04 | Prompts drift into personalized regulated advice | High | Test explanation and trust only; exclude investment, credit, tax, legal, and guaranteed-outcome advice | Product + Legal/Compliance | Qualified review of advice boundaries and escalation wording |
| R-05 | Accessibility excluded until late design | Medium–High | Inclusive recruitment, accessible materials, accommodations, explicit target | UX Research + Accessibility | Record accessibility target and limitations |
| R-06 | Excessive or indefinite research-data collection | High | Minimum-field inventory, pseudonyms, restricted access, approved storage and deletion | Privacy + UX Research | Data inventory with purpose, access, retention, and owner |
| R-07 | Prototype or research language implies nonexistent live capabilities | High | Visible synthetic/proposed disclaimers; distinguish current, proposed, and simulated behavior | Product + Data/AI | Remove unsupported capability claims |
| R-08 | Financial discussion causes distress or pressure to disclose | Medium–High | Optional questions, pause/withdraw, neutral language, stop criteria, support route | UX Research + Ethics owner | Moderator distress and withdrawal protocol |
| R-09 | Small or biased sample is overstated | High | Predefined analysis, contradiction log, bias and confidence reporting | UX Research + Product | Traceability and limitations required in findings |
| R-10 | Competitive review relies on marketing or inaccessible states | Medium | Record URL, date, platform, region, plan/account state, and access limitation | Competitive Analyst | Dated evidence and limitation fields |
| R-11 | Competitor designs or copy are reproduced | Medium | Paraphrase patterns, cite sources, avoid copying proprietary content | Competitive Analyst + Legal | Pattern-level synthesis only |
| R-12 | Malicious transaction text is trusted as instruction | Medium–High | Add a synthetic prompt-injection case and assign later control/evaluation ownership | Data/AI + Security | Record as unresolved risk; do not claim solved in discovery |

## Operating constraints

- Use synthetic financial scenarios by default.
- Do not connect production accounts or collect credentials.
- Do not test personalized regulated advice.
- Do not describe the assistant as implemented, live, or proven accurate.
- Keep raw notes and participant identifiers outside `output/`.
- Stop research if consent, privacy handling, or participant-safety procedures are not approved.

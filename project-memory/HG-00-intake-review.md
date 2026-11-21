# HG-00 Project Intake Review Package

**Artifact state:** DRAFT_FOR_REVIEW  
**Prepared:** 2026-11-15  
**Gate:** HG-00 — Project Intake  
**Coordinated by:** UX Workflow Orchestrator  
**Contributors:** UX Researcher, Product Definition Agent, Fintech Risk Reviewer  
**Human decision:** REQUIRED — not entered by agents

## Orchestrator recommendation

Choose `CHANGES_REQUIRED` unless the human approver deliberately authorizes a discovery-only start using `APPROVED_WITH_ACTIONS` and records the conditions in this package and `gates/HG-00-project-intake.md`.

Do not begin participant research involving personal or financial information, live-data work, detailed personas, product-definition artifacts, or later UX phases until their prerequisites are approved.

## Intake checklist assessment

| HG-00 item | Readiness | Evidence and gap |
| --- | --- | --- |
| BRD version and owner | Not ready | The input is marked `Discovery Draft`; no version, named owner, or approval authority is recorded. |
| Product type, screens, and capabilities | Not ready | `Fintech mobile application` is stated, but tracker vs wallet vs banking/broader product, current screens, connected accounts, and actual functions are unknown. |
| Users, geography, currency, and language | Not ready | User segments are proposed only. India/INR are illustrative; launch market, languages, accessibility target, and regulatory context are unconfirmed. |
| Research access, timeline, and constraints | Not ready | A 5–8 interview recommendation exists, but participant source, recruitment owner, method, schedule, incentives, tools, recording, and data-handling rules are undefined. |
| Data sources and accountable owners | Not ready | Required data types and safeguards are described, but actual availability, source systems, freshness, model/provider boundaries, and accountable owners are unconfirmed. |
| MVP boundaries and exclusions | Defined; acknowledgement required | UC-01–04 are Must, UC-05–06 Should, UC-07 Could, and autonomous financial actions are excluded. A human must approve or revise these boundaries. |

## Confirmed project-package facts

- The input is a discovery-draft BRD for a proposed AI assistant within Fin Buddy.
- The proposed MVP covers spending summaries, budget Q&A, transaction search, financial education, an optional savings calculator, and opt-in insights.
- The BRD requires meaningful consent, grounded answers, deterministic financial calculations where possible, evidence visibility, correction, privacy controls, accessibility, and incident monitoring.
- The BRD excludes autonomous transfers, payments, investing, loan applications, account changes, credit decisions, professional tax/legal advice, unauthorized third-party data, and unsupported real-time claims.
- No completed or approved user research is included in the project package.

These statements describe the current documents; they do not independently verify the existing product.

## Assumptions requiring human confirmation or research

- Fin Buddy is a consumer personal-finance application.
- Transactions, categories, budgets, recurring expenses, and savings-goal data exist and can be authorized for read-only use.
- The proposed user segments are relevant.
- India, INR, and Indian examples represent the intended launch context.
- Users experience the four hypothesized pain points and will value conversational access.
- Five to eight exploratory interviews are feasible.
- The linked case study represents the current or intended product experience.

## Severity-ranked intake risks

### Critical

1. Launch jurisdiction and applicable privacy, financial-services, consent, retention, and AI obligations are unknown.
2. Product type and current capabilities are unconfirmed, including whether real financial accounts or transactions are connected.
3. Financial-data sources, freshness, authorization scope, and accountable owners are unknown.

### High

1. Product, Engineering/Data, Security/Privacy, Legal/Compliance, Analytics, and UX Research owners are not assigned.
2. Research consent, recording, storage, access, redaction, retention, deletion, and incentive rules are undefined.
3. AI provider, data-sharing boundary, retrieval/calculation ownership, logging, prompt-injection controls, monitoring, and evaluation ownership remain assumptions.
4. The accessibility target and accountable reviewer are unset.

### Medium

1. Education-versus-regulated-advice boundaries need jurisdiction-specific human review.
2. Incident and support escalation ownership is not assigned.
3. MVP exclusions are documented but not human-acknowledged.

## Human decisions required

1. Name the HG-00 approver and confirm the BRD/product owner and version.
2. Confirm the product category and provide current screens, flows, prototype, or case-study assets; alternatively approve a greenfield-discovery assumption.
3. Confirm or deliberately defer the launch country/region, currency, languages, intended audience, and accessibility target.
4. Confirm the target user segments and provide existing research, analytics, or support evidence if available.
5. Authorize the discovery method, participant source, sample range, recruitment owner, timeline, incentives, tools, and constraints.
6. Approve research consent, recording, minimization, redaction, storage/access, retention, deletion, and a prohibition on collecting credentials or unnecessary account details.
7. Assign Product, UX Research, Engineering/Data, Security/Privacy, Legal/Compliance, Analytics, and Support owners.
8. Provide a preliminary data inventory covering transactions, balances, budgets, goals, chat history, derived insights, source systems, freshness, and use of synthetic vs real data.
9. Approve or revise MVP priorities and explicitly acknowledge excluded actions.
10. Assign success-metric owners and a baseline plan.

## Conditional discovery-only approval

If the human selects `APPROVED_WITH_ACTIONS`, Phase 01 should initially be limited to low-risk discovery under all of these conditions:

- Use synthetic scenarios and avoid live or production financial data.
- Do not collect credentials, full account details, or unnecessary personal financial information.
- Do not claim existing product capabilities that have not been verified.
- Do not create evidence-based personas until actual research is approved and completed; use clearly labeled assumptions only where necessary for planning.
- Do not present the assistant as providing regulated or personalized financial advice.
- Assign the critical owners and product/jurisdiction context before participant research involving financial information.
- Return all Phase 01 findings to HG-01 for human review.

## Gate hold

The workflow is paused at HG-00. No agent is authorized to mark the gate approved. Phase 01 may begin only after a human records an allowed decision in `gates/HG-00-project-intake.md`. Nothing is authorized for `output/`.

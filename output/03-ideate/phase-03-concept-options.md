# Phase 03 — Interaction Concept Options

**Artifact state:** DRAFT_FOR_REVIEW — REQUIRES HG-03 APPROVAL  
**Scope:** Ideation only; no wireframes or final UI copy

## A — Assistant-first hub

Dedicated conversation destination with task starters, history, and controls.

- Strengths: consistent mental model, multi-turn exploration, centralized controls.
- Risks: duplicates direct navigation, loses originating context, may imply chat is always preferred.
- Best for: exploratory questions and cross-task interpretation.

## B — Contextual assistant layer

Entry points live within transaction, budget, category, and goal views.

- Strengths: preserves context, reduces prompting, keeps direct controls primary.
- Risks: fragmented experience, unclear inherited scope, limited space for follow-up.
- Best for: questions about a visible period, category, budget, transaction, or goal.

## C — Dual-path hybrid — recommended provisionally

Direct interfaces remain primary. Contextual explanations and a global hub share history, permission, evidence, and correction rules.

- Strengths: supports both low-effort contextual questions and multi-turn exploration while preserving direct routes.
- Risks: highest consistency/state burden; users may be uncertain where history or correction lives.
- Requirement: shared context must be visible, editable, and consistent across entry points.

## Trust patterns

- Context preview before retrieval
- Scoped consent and permission receipt
- Data freshness and coverage disclosure
- Deterministic calculation disclosure
- Progressive evidence from summary to records
- Editable assumptions and filters
- Limitation/uncertainty treatment without false precision
- Visible read-only boundary
- Correction impact preview
- Persistent history/deletion/permission controls
- Education/observation/scenario/advice distinction

## Key trade-offs

| Decision | Benefit | Risk | Provisional direction |
| --- | --- | --- | --- |
| Dual entry | Context plus exploration | More complexity | Test both in low fidelity |
| Guided starters + open input | Discoverability and flexibility | Can bias expectations | Optional starters |
| Concise answer + expandable evidence | Speed and trust | Hidden limitations may be missed | Keep material limitations visible |
| Session vs persistent permission | Minimization vs convenience | Consent fatigue or overreach | Test clearly tiered scopes |
| Persistent history | Continuity | Sensitive-data exposure | Minimum/default retention needs privacy decision |
| Correction in chat | Fast recovery | Duplicates source-of-truth controls | Use canonical correction service |
| Proactive insights | Awareness | Intrusion/anxiety | Opt-in, dismissible, separately tested |
| AI explanation | Comprehension | Unsupported causality | Grounded observations only |

## Accessibility concept requirements

- Labeled direct controls must exist alongside free text.
- Focus and announcements must work for messages, dialogs, errors, and recalculation.
- Status cannot rely on color alone.
- Evidence and assumptions must support zoom/reflow and plain-language alternatives.
- Suggested prompts cannot be the only discovery mechanism.
- Voice/multilingual support remains deferred pending separate quality/privacy/accessibility approval.

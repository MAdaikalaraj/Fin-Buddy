# Fin Buddy UX Workflow

## Objective

Run an evidence-based UX process for the Fin Buddy AI Assistant through Understand, Define, Ideate, Design, and Test, with human control at every material decision.

## Source of truth

- Business requirements: `input/Fin_Buddy_AI_Assistant_BRD.md`
- Phase contracts: `output/*/PHASE.md`
- Human decisions: `gates/HG-*.md`
- Reusable methods: `skills/*.md`
- Role boundaries: `agents/*.md`

## Sequence

1. HG-00 Project Intake
2. Phase 01 Understand → HG-01
3. Phase 02 Define → HG-02
4. Phase 03 Ideate → HG-03
5. Phase 04 Design → HG-04 wireframe checkpoint → HG-04 final decision
6. Phase 05 Test → HG-05 output authorization

Phases may iterate backward when evidence invalidates an earlier decision. A later phase must not silently overwrite an approved assumption, requirement, or design decision; record the change and return it to the relevant human gate.

## Gate policy

The allowed human decisions are:

- `APPROVED`: proceed within the approved scope.
- `APPROVED_WITH_ACTIONS`: proceed while tracking the named actions and deadline.
- `CHANGES_REQUIRED`: stop progression, revise, and resubmit.
- `BLOCKED`: stop until the stated dependency or decision is resolved.

Agents may prepare recommendations and checklists but may not enter a decision on behalf of a human.

## Artifact states

Use these states in artifact headers or metadata:

- `WORKING`: incomplete internal material.
- `DRAFT_FOR_REVIEW`: ready for a human gate.
- `APPROVED`: approved at the named gate but not necessarily authorized for output.
- `OUTPUT_AUTHORIZED`: specifically named in HG-05 output authorization.

## Output protection

`output/` is a publication boundary, not a working directory.

- Keep research notes, synthesis, design drafts, prototypes, and test drafts in their phase work areas.
- Before writing to `output/`, verify an HG-05 approving decision, the named human approver, and an exact authorized-artifact list.
- If any field is missing or ambiguous, stop and request human review.
- Never infer output authorization from phase approval, stakeholder comments, or completion of testing.

## Traceability

Each reviewable artifact should identify:

- BRD requirements or hypotheses addressed
- source evidence and date
- responsible agent or owner
- assumptions and confidence
- unresolved risks and dependencies
- gate and decision status

## Fin Buddy safeguards

- Financial numbers must come from trusted records and deterministic calculations where possible.
- AI explanations must expose period, assumptions, uncertainty, and supporting records.
- Personal and financial data must be minimized and access-controlled.
- General education must be distinguishable from personalized regulated advice.
- No autonomous transfers, investing, credit decisions, or other BRD-excluded actions are allowed in the MVP workflow.

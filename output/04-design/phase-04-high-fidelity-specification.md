# Phase 04 — High-Fidelity Design Specification

**Artifact state:** DRAFT_FOR_REVIEW — HG-04 FINAL DECISION REQUIRED  
**Scope:** Provisional production-oriented UI, content, component, and interaction specification  
**Not delivered:** No rendered visual artifact, Figma file, finalized brand system, production library, or validated usability result exists.

## Visual direction

Use a calm, neutral, information-first system. Financial totals and warnings must feel precise without becoming alarming. Scope, freshness, evidence, limitations, and controls receive stronger hierarchy than decorative or engagement elements.

## Provisional semantic tokens

| Token | Value | Use |
| --- | --- | --- |
| `bg-canvas` | `#F6F8FC` | App background |
| `bg-surface` | `#FFFFFF` | Cards, panels, dialogs |
| `bg-subtle` | `#EEF2F7` | Grouped secondary regions |
| `text-primary` | `#172033` | Primary text |
| `text-secondary` | `#475569` | Supporting text |
| `text-disabled` | `#64748B` | Disabled text where suitable |
| `border-default` | `#64748B` | Essential input/control boundaries; provisional contrast against white is approximately 4.76:1 |
| `border-strong` | `#475569` | Selected/important boundaries |
| `action-primary` | `#075CBD` | Primary action |
| `action-hover` | `#064B9A` | Hover |
| `action-pressed` | `#043B7A` | Pressed |
| `focus-ring` | `#7C3AED` | Independent focus indication |
| `status-info` | `#075CBD` | Information |
| `status-success` | `#176B43` | Completion |
| `status-warning` | `#8A4B00` | Stale/partial/attention |
| `status-danger` | `#B42318` | Destructive/critical failure |
| `bg-info` | `#EAF3FF` | Info surface |
| `bg-success` | `#E9F8F0` | Success surface |
| `bg-warning` | `#FFF4DD` | Warning surface |
| `bg-danger` | `#FDECEC` | Error surface |

These are starting points pending brand reconciliation and automated/manual contrast testing.

## Contrast and accessibility intent

- WCAG 2.2 AA intent: 4.5:1 normal text; 3:1 large text and meaningful graphics/component boundaries.
- Focus indicator: at least 2 CSS-pixel equivalent and visible against control and surrounding surface.
- Never encode budget status, deltas, freshness, uncertainty, or severity with color alone.
- Charts require direct labels, shapes/patterns, summaries, and table alternatives.
- Minimum interactive target: 44×44 px; prefer 48×48 px for primary mobile actions.
- Support 200% text zoom and 400% page zoom/reflow without loss of function.

## Typography and spacing

Use a licensed/system sans-serif with distinct numerals, tabular figures, INR support, and reliable multilingual glyphs.

| Style | Size/line height | Weight |
| --- | --- | --- |
| Display | 32/40 | 650–700 |
| Heading 1 | 24/32 | 650–700 |
| Heading 2 | 20/28 | 600–650 |
| Heading 3 | 18/26 | 600 |
| Body | 16/24 | 400 |
| Body strong | 16/24 | 600 |
| Small | 14/20 | 400 |
| Caption | 12/18 | 500 |
| Large number | 28/36 | 650 |

Use a 4 px grid: 4, 8, 12, 16, 20, 24, 32, 40, 48. Default mobile page padding is 16 px; larger screens use 24–32 px.

## Component system

### Navigation/header

Back, close, title, context subtitle, help. Back remains within the assistant; close returns to the originating product state. Direct destinations remain reachable.

### Buttons

Primary, secondary, tertiary, destructive, and labeled icon variants. States: default, hover, focus, pressed, loading, disabled. One dominant primary action per decision. `Allow`, `Not now`, and `Deny` remain legible and neutrally presented.

### Structured task tile

Icon, task name, purpose, and optional data-required label. Tasks: Review spending, Check a budget, Find a transaction, Explore a savings scenario, Learn a financial concept.

### Composer

Labeled multiline input, visible context, submit, and privacy hint. Typing does not imply data consent. Warn against passwords, PINs, and full account numbers.

### Context panel

Origin, period, masked accounts, filters, category/budget/goal, and edit/remove. Material scope never hides only inside a chip.

### Consent scope row

Data type, exact scope, purpose, duration, detail. Required and optional scopes are distinct; optional scopes are off by default; retention is separate.

### Status banner

Info/success/warning/error variants with icon, heading, text, affected scope, and safe recovery. Material stale/partial warnings cannot be dismissed while they affect the answer.

### Deterministic result block

Financial result, formula/method, period, currency, freshness, and source. States: initial, recalculating, updated, unavailable. It is visually and semantically separate from AI explanation.

### AI explanation block

Grounded observation, limitation, education, or restricted response. It cannot outrank material limitations or alter deterministic values.

### Evidence list

Date, inert merchant/description text, category, amount, status, canonical open/correct actions. Dynamic loading announces count and position.

### Clarification form

Edits interpreted period/account/category/merchant/intent and reruns without changing source records.

### Correction form

Shows exact record, current/proposed value, scope, impact, confirm/cancel, recalculation, receipt, and failure. Uses canonical service; undo only if supported.

### History/privacy/deletion controls

Conversation history, permission, proactive-insight preference, eligible-history deletion, account-data request, and export remain distinct. Each destructive action names scope, timing, reversibility, and exceptions.

### Feedback/support

Structured reasons first, optional warning-protected text, human-review disclosure, minimal telemetry, payload review/minimization, consent, response expectation, receipt, decline, and fallback.

## Representative screen content

### Assistant hub

- Title: “Ask Fin Buddy”
- Role: “Fin Buddy can explain your money using data you choose. It can’t move money or make financial decisions for you.”
- Input: “What would you like to understand?”
- Hint: “Don’t enter passwords, PINs, or full account numbers.”

General education begins without financial permission. Financial task tiles disclose that selected financial data is required.

### Spending answer

- Result: “You spent ₹4,200 more in November than in October.”
- Observation: “The largest observed differences were Dining and Transport.”
- Scope: selected masked account, record count, period, and refresh time.
- Limitation example: “Two transactions are uncategorized and are included under Other.”
- Actions: See how this was calculated; Correct a category; Change question; Open spending; Feedback; Exit.

Do not claim that a category caused the change.

### Budget answer

- “₹2,300 remains in your Food budget through 30 November.”
- “You’ve used 77% of this budget with 15 days remaining.”
- Boundary: “This is a calculation from your selected budget and transactions, not a recommendation.”

Scenario exploration never edits the canonical budget.

### Transaction search

Show count and applied filters. For zero results: “No matches were found in the selected accounts and dates.” Never imply absence outside authorized sources.

### Savings scenario

- “To reach ₹60,000 by 31 May 2027, the calculated contribution is ₹10,000 per month.”
- Show inputs, formula, rounding, currency, exclusions, and no-guarantee label.
- Equal-weight alternatives; no “best” option.

### Education and restricted advice

Education label: “General information — this explanation doesn’t use your account data.”

Restricted example: “I can explain how investment risk works, but I can’t choose an investment or promise a return for you.” Offer safe education, qualified support, reframe, and exit.

### Data-quality failure

- Stale: last successful update and affected scope.
- Partial: identify unavailable source and state that a complete total cannot be calculated.
- Calculation failure: “The calculation couldn’t be completed. Fin Buddy won’t estimate the missing amount.”

## Proactive insight opt-in PI-00–PI-06

Insights are disabled by default.

1. **PI-00 Invitation:** Non-personalized invitation from Settings or after a successful relevant task; never during denial, error, privacy complaint, restricted state, or distress.
2. **PI-01 Explanation:** Purpose, observation-not-advice boundary, minimum data, cadence/surfaces, privacy, retention, AI involvement, and turn-off route.
3. **PI-02 Scope:** Accounts/categories/types/frequency/quiet hours/channels with optional values off by default.
4. **PI-03 Consent:** Exact selected data and behavior; Turn on selected, Review settings, Not now, No thanks. Notification permission is separate.
5. **PI-04 Receipt:** Scope, cadence, channels, time, Manage and Turn off. WF-30 may appear only after this receipt.
6. **PI-05/06 Card and control:** Period/source/freshness, neutral observation, evidence, dismiss, mute, tune, report, and global opt-out.

Permission expiration or withdrawal suppresses future personalized insights without silent re-enable.

## Responsive behavior

- Mobile: single column; contextual assistant becomes full-height; evidence rows stack; no horizontal scrolling for core meaning.
- Tablet: 4/8 or 5/7 context/answer split where reading/focus order remains logical.
- Desktop: 1120–1200 px maximum primary width; 640–760 px answer column; optional side-by-side source and assistant.
- Rotation/resizing preserves inputs, position, selected evidence, and privacy state.

## Motion restrictions

- Honor reduced motion; no essential status depends on animation.
- 150–200 ms simple opacity/position transitions only.
- No parallax, bounce, pulsing financial amounts, celebratory savings motion, or alarmist insight animation.
- Loading uses accessible text; skeletons never resemble completed financial data.
- Recalculation uses restrained highlighting and an announcement.
- Do not auto-scroll if the user is reviewing earlier content; offer a new-response control.

## Remaining decisions

- Reconcile tokens with the actual brand and test contrast.
- Confirm supported platforms and breakpoints.
- Approve consent, retention, deletion, permission, and support language.
- Confirm canonical category correction and undo.
- Approve jurisdiction-specific advice boundaries.
- Approve insight thresholds, cadence, quiet hours, and notification policy.
- Complete content, localization, accessibility, privacy/security, legal, and engineering reviews.
- Define privacy-minimized analytics events.

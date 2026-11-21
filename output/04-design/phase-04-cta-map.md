# Phase 04 — CTA Scope and Action Map

**Artifact state:** DRAFT_FOR_REVIEW — HG-04 FINAL DECISION REQUIRED

| CTA | Destination/service | Data or write effect | Confirmation | Scope status |
| --- | --- | --- | --- | --- |
| Ask Fin Buddy | Assistant hub/context | None until consented retrieval | No | Allowed |
| Review spending | Context/consent flow | Read authorized transactions | Consent if needed | Allowed |
| Check a budget | Context/consent flow | Read budget and transactions | Consent if needed | Allowed |
| Find a transaction | Deterministic search | Read authorized records | Consent if needed | Allowed |
| Learn a financial concept | Reviewed education | No personal data | No | Allowed |
| Explore savings scenario | Deterministic calculator | Manual/authorized read only | Consent only for prefill | Allowed |
| Allow selected | Consent service | Grants named scopes | Explicit action | Allowed |
| Not now / Deny | Consent flow | No grant | No | Required alternative |
| View evidence | Evidence service | Read contributing records | No | Allowed |
| Change question | Intent form | Reruns structured query; no source write | Submit | Allowed |
| Correct data | Canonical correction service | Explicit record/category write if supported | Impact preview + confirm | Conditional allowed |
| Open spending/budget/transactions/goal | Direct product screen | No assistant write | No | Allowed |
| Give feedback | Feedback service | Minimal disclosed diagnostic event | Submit | Allowed |
| Report unsafe/privacy issue | Support/escalation | Minimum reviewed payload | Consent before handoff | Allowed |
| Withdraw permission | Permission service | Stops future retrieval | Exact-scope confirm | Allowed |
| Delete conversation | History service | Deletes named eligible conversation | Destructive confirm | Allowed |
| Delete eligible history | History service | Deletes eligible retained history | Destructive confirm | Allowed |
| Account-data request | Separate privacy route | Depends on confirmed service | Separate confirm/process | Unresolved; simulated only |
| Turn on insights | Insight preference/consent | Grants selected insight scopes | PI-03 explicit confirm | Allowed after PI flow |
| Dismiss insight | Preference service | Hides one card | No | Allowed |
| Mute/pause insights | Preference service | Pauses named type/duration | Confirm selection | Allowed |
| Turn off insights | Preference service | Stops future personalized insights | Confirm + receipt | Allowed |
| Retry/refresh | Data service | Repeats authorized retrieval | No new grant | Allowed |
| Exit/close | Navigation | No financial or permission change | Warn only if approved unsaved text would be lost | Allowed |
| Transfer/pay/invest/apply/change account | None | Prohibited execution | N/A | Excluded |
| Edit canonical budget from assistant | None | Prohibited silent write | N/A | Excluded; direct route only if product supports it |

Every instantiated prototype CTA must map to this table or be reviewed before testing. No CTA may acquire broader scope or perform an unlisted write.

# Synthetic Evaluation Fixtures

These fixtures contain fictional records only. They support deterministic arithmetic, filtering, correction, exclusion, stale/partial-data, mixed-currency, and untrusted-record-text checks.

Run from the project root:

```powershell
powershell -ExecutionPolicy Bypass -File .\tests\verify-golden-dataset.ps1
```

A passing harness does not validate a production financial service, model grounding, consent enforcement, security, accessibility, usability, retention, deletion, or compliance.

# Recruiter proof guide — October 2026

## Start here

[Three case studies](recruiter-case-studies.html) → [Interactive Control Room](control-room/) → [Evidence index](evidence.md).

| Role | Relevant evidence | What is demonstrated | Limitation |
|---|---|---|---|
| AI implementation associate | [Workflow case study](recruiter-case-studies.html#implementation) | Approval and verification stages in a browser simulation | No live AI provider or customer deployment |
| Customer implementation / success | [Onboarding case study](recruiter-case-studies.html#onboarding) | Deterministic consent, approval, retry and escalation rules | Fictional inputs; no CRM or real customer |
| Automation / solutions support | [Oversight case study](recruiter-case-studies.html#oversight) | Security failure-mode investigation and release criteria | Private assessment not independently reproduced here |

## Interview-ready explanation

**Situation:** A workflow that says “done” without evidence is difficult to trust.

**Task:** Make the decision points understandable and testable.

**Action:** Separate authorization, simulated execution, evidence, and verification; provide reproducible examples and document the limitations.

**Result:** Public inspectable demonstrations and a documented testing approach. No production impact or customer outcome is claimed.

## Reviewer verification

1. Open the [case study hub](recruiter-case-studies.html).
2. Follow the Control Room link and test the human rejection path.
3. Review the [Python scenario source](https://github.com/AshtonCodes316/AshtonCodes316/tree/main/examples/implementation-simulator) and [CI](https://github.com/AshtonCodes316/AshtonCodes316/actions).
4. Compare claims against the [evidence index](evidence.md) and [project status](project-status.md).

Do not treat a GitHub Actions green check as proof of production safety or external integration.

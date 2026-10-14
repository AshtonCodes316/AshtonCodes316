# Engineering case study — customer implementation workflow simulation

**Artifact:** [Public Python implementation simulator](../examples/implementation-simulator/README.md) · [Scenario matrix source](../examples/implementation-simulator/scenarios.py) · [CI workflow](../.github/workflows/implementation-simulator.yml)

## The problem

Customer onboarding and AI implementation work often depends on permission, human approval, and reliable handling of unavailable integrations. A workflow that treats every request as ready can hide missing consent or failed dependencies. This example models those decisions with fictional inputs and **no real integrations**.

## Design choices

- **Consent before approval:** The model blocks when consent is absent, even if approval or integration health appears favorable.
- **Approval before execution readiness:** No approved request means no simulated completion.
- **Bounded retry and escalation:** An unhealthy integration produces a retry recommendation below two attempts; at two or more, it recommends human investigation. It never actually retries or contacts a service.
- **Deterministic evidence:** The simulation emits canonical JSON evidence and a SHA-256 digest. This is a reproducibility aid, **not** an authenticated audit trail.
- **Explicit simulation boundary:** A successful status is `SIMULATED_COMPLETE`, not production deployment success.

## How to reproduce

```bash
cd examples/implementation-simulator
python3 -m unittest discover -v
python3 scenarios.py
```

The matrix enumerates 2 consent values × 2 approval values × 2 integration-health values × 3 attempt counts = **24 fictional scenarios**. The expected distribution is 12 consent blocks, 6 approval blocks, 2 retry recommendations, 1 escalation, and 3 simulated completions. Five additional tests check the matrix's coverage, counts, absence of external calls, and reproducibility. Treat these as **expected assertions** until confirmed by CI; the workflow history is the authoritative test outcome.

## Why it matters for implementation roles

This small example illustrates how to translate ambiguous onboarding requirements into testable business rules, preserve human review gates, document failure behavior, and produce a reviewer-friendly verification path.

## Evidence boundaries

This is a portfolio teaching example, not a customer case study. It does **not** demonstrate a real CRM, production API, actual consent management, deployed AI, operational retries, SLA compliance, customer satisfaction, or financial impact. It uses fictional data and cannot substantiate real-world performance or business outcomes.

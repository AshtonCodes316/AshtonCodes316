# Customer Implementation Simulator — public evidence

A fictional, deterministic Python example of an onboarding implementation workflow. **Not a deployed customer integration, an AI model, or the private Master Key runtime.** Standard library only; no API keys, network access, spending, or customer data.

## Try it

```bash
cd examples/implementation-simulator
python3 simulator.py
python3 -m unittest discover -v
```

## State machine

| Condition (checked in order) | Simulated status | Next action |
|---|---|---|
| Missing consent | BLOCKED_CONSENT | Request consent |
| Missing approval | BLOCKED_APPROVAL | Request approval |
| Unhealthy integration, fewer than two attempts | RETRY_PENDING | Retry after review |
| Unhealthy integration, two or more attempts | ESCALATED | Human investigation |
| All gates pass | SIMULATED_COMPLETE | Review receipt |

The fixed order ensures consent and approval checks take precedence over simulated execution. No retries or external calls actually occur. A SHA-256 hash binds the fictional evidence payload; it is **not** a digital signature or tamper-proof audit.

## Inspect the proof

Read [the tests](test_simulator.py) and [the workflow](../../.github/workflows/implementation-simulator.yml). CI outcomes must be verified from [GitHub Actions runs](https://github.com/AshtonCodes316/AshtonCodes316/actions/workflows/implementation-simulator.yml), not assumed from this README.

## Exhaustive scenario coverage

[Run the 24-case scenario matrix](scenarios.py) · [Five matrix tests](test_scenarios.py) · [Engineering case study](../../docs/implementation-simulator-case-study.md). Matrix output is a deterministic **simulation**, not measured customer outcomes.

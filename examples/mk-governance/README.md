# MK governance — public standalone demonstration

**Status:** Runnable educational example. This is **not** the private Master Key runtime, and no real AI worker is connected.

This small Python example illustrates human approval gates, fail-closed behavior when no worker is qualified, and a deterministic SHA-256 evidence receipt. It uses fictional mission data and Python's standard library only.

## Run

From this directory with Python 3.10+:

```bash
python demo.py
python -m unittest -v
```

## Local verification (October 12, 2026)

The example was executed in a separate local working environment: **4 tests passed at that checkpoint**, zero failures. The example output reported `BLOCKED_NO_QUALIFIED_WORKER`, `real_worker_called: false`, and a SHA-256 receipt. These results are for **this public standalone example only**, not the private MK test suite.

## Independently inspectable CI

[GitHub Actions verification runs](https://github.com/AshtonCodes316/AshtonCodes316/actions/workflows/public-proof.yml) · [Public Proof Lab and verification rubric](../../docs/public-proof-lab.md)

CI status is determined by the linked runs for each commit; this document does not imply the private MK system passed CI.

## Expanded verification suite

The current test file contains **10 independent test methods** covering all four approval/worker-availability combinations, approval precedence, no-dispatch behavior, reproducible receipt hashes, and evidence integrity. The current CI result must be checked before treating this expansion as passed.

## Boundaries

- No external models, network calls, live workers, or paid APIs.
- `READY_FOR_DISPATCH` is a simulated state label; it does not dispatch anything.
- Hashing evidence is not a digital signature, tamper-proof audit log, or independent verification.
- The private MK implementation is not included or implied to have been tested here.

[Back to MK case study](../../docs/master-key.md) · [Main profile](../README.md)

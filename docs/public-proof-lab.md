# Public Proof Lab — independently inspectable evidence

This page documents a small **standalone educational** governance example, not the private Master Key runtime.

## Reproduce

```bash
cd examples/mk-governance
python3 -m unittest discover -v
python3 demo.py
```

The public `test_demo.py` currently defines **10 `unittest` test methods**. They cover approval requirements and denial precedence; fail-closed behavior without an available worker; all four boolean approval/availability combinations; deterministic and canonical SHA-256 receipt hashing; distinct decision receipts; confirmation that no real worker is called; and a fixed fictional mission. These are tests of a small educational simulation, **not** tests of private MK or a live AI service.

## CI evidence

[Inspect GitHub Actions runs](https://github.com/AshtonCodes316/AshtonCodes316/actions/workflows/public-proof.yml)

The workflow runs the standard-library tests on changes to the demo and on manual dispatch. **A workflow file alone is not evidence that a run passed.** Consult the linked run history and commit SHA for results.

## Truth boundaries

- The demo uses fictional inputs; it performs no AI inference, tool dispatch, network call, or spend.
- `READY_FOR_DISPATCH` is only a simulated label.
- A SHA-256 digest is a reproducibility aid, not an attestation, signature, or tamper-proof audit trail.
- This workflow validates the public demo only; it does not qualify the proprietary MK system.
- Private repositories, credentials, and proprietary artifacts are intentionally excluded.

## Verification rubric

1. Check the workflow result for the specific commit.
2. Read the code and tests, not only the badge.
3. Re-run locally without external dependencies.
4. Compare the stated limitations against the implementation.

[Back to profile](../README.md) · [Demo source](../examples/mk-governance/README.md)

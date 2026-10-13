# Master Key — Engineering Case Study

**AI orchestration · permission-aware automation · verification · Python**

[Back to profile](../README.md) · [MK overview](master-key.md) · [Architecture](mk-architecture.md)

## The challenge

An AI system can produce a convincing answer without proving that the underlying task succeeded. Master Key explores an operator-controlled workflow that separates **requests, authorization, execution, evidence, verification, and final approval**.

## My approach

| Design decision | Why it matters |
|---|---|
| Represent work as missions with explicit states | Operators can see progress and failures rather than infer them from chat messages. |
| Check permissions before actions | Delegated work must remain within its approved scope. |
| Keep spending approval separate | Authorizing a mission should not automatically authorize a paid provider. |
| Record evidence and review outcomes | Worker output is not automatically proof of success. |
| Test database persistence and restart behavior | Important mission and organization state must survive ordinary restarts. |

These are project design and implementation areas, **not claims that every external integration is live**.

## A concrete debugging example — October 12, 2026

I used a detached, disposable Windows Git worktree to check security and persistence behavior without changing my original development checkout.

**Environment:** Windows, Python 3.12.10, pytest 9.1.1; source commit `f45598a3330e53d9216ba4061f6c8a99d2106eeb`.

**What the initial targeted tests exposed:**

1. Four security/domain schema assertions still expected schema version **26**, while the checked-out implementation reported **35**.
2. An autouse test fixture forced repository runtime mode, conflicting with SQLite tests intended to verify an explicit runtime directory.
3. A restart durability test referenced fixtures defined in another test module, where pytest did not make them available automatically.

**What I changed:** Only five test files in the disposable worktree: four schema assertions, one SQLite fixture environment override, and imports of existing restart-test fixtures. I did **not** change production code. The original checkout was not modified as part of this verification.

**Final targeted runs:**

| Test area | Result |
|---|---:|
| Four security modules | **146 passed** |
| Eight domain/persistence modules | **174 passed, 1 skipped** |
| Combined test executions | **320 passed, 1 skipped** |

The domain/persistence command was:

```bash
python -m pytest tests/test_domain.py tests/test_m03_domain.py tests/test_m04_domain.py tests/test_m04_persistence.py tests/test_m05_domain.py tests/test_m05_persistence.py tests/test_m06_domain.py tests/test_sqlite_persistence_hardening.py -q --tb=short
```

**Interpretation:** The corrected, targeted test batches passed locally. This is **not** an untouched-commit result, independent security audit, production reliability claim, or execution of the full **3,834 collected tests**. The test-only patch and sanitized logs have not yet been published.

## What I learned

A failing test does not automatically mean the implementation is broken. In this case, investigation distinguished stale expectations and fixture configuration from production failures. Equally, making a test pass does not establish production readiness: it establishes a bounded result under documented conditions.

## What I would do next

- Publish a sanitized patch and repeatable test instructions.
- Run broader orchestration/integration tests under controlled network and credential restrictions.
- Produce a short screen recording with fictional data and real, labeled test output.
- Qualify real callable AI workers separately from architecture and local tests.

## Career relevance

This work connects software testing to the operational skills required in **AI implementation, workflow automation, technical solutions, and technical customer success**: defining requirements, investigating failures, documenting constraints, and communicating what has actually been verified.

[Evidence index](evidence.md) · [90-second demo storyboard](mk-demo-storyboard.md)

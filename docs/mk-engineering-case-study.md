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


## Authorization regression investigation — October 2026 (XMAS-29)

**Status: reported in a local, isolated assessment; not independently reproduced from this public repository.** This is an engineering investigation, **not** a production security certification. The underlying MK source and test artifacts remain private and the reported evidence package has not been published here.

### The problem

A human approval boundary is only useful when an approval cannot be reused to authorize a materially different command. The investigation targeted mixed authorized/unauthorized requests, scope escalation after edits, unknown product identifiers, ambiguous autopilot instructions, and cancellation messages that accidentally create new work.

### The test design

A 66-case authorization acceptance suite was run against a reference policy gate (positive control), five deliberately insecure policy variants (negative controls), the canonical MK revision, and a separate A7 routing candidate. Four positive-control cases checked that harmless authorized work could still proceed; the negative controls checked that the suite detects intentionally removed protections.

| Reported test target | Result | What it means |
|---|---:|---|
| Reference gate, both trees | **66/66** | The proposed acceptance behavior was achievable in the isolated reference setup. |
| Five deliberately insecure variants | **All targeted control groups detected** | The suite identified the intentionally weakened policies. |
| Canonical MK at `0bae02db` | **7/66** | Most required authorization behavior did not pass. |
| MK with isolated A7 at `0a898cc2` | **16/66** | Routing improved, but authorization safety remained insufficient. |

### Findings and engineering decisions

- **Edit escalation:** 7/7 reported cases failed. Changes adding deployment, spending, additional product scope, trading, or removal of negation could receive GO without the required re-authorization.
- **Scope normalization:** 7/7 variants failed; unregistered product identifiers could pass as raw strings through Unicode or whitespace variants.
- **Mixed authority requests:** mixed GO and launch categories each reported 0/8 passes.
- **Routing improvements:** the isolated A7 candidate passed alias collisions (4/4), multi-product handling (2/2), and exclusions (3/3).
- **Controls already observed:** parent-version approval replay and repeated GO were refused in the tested candidate.

**Recommended remediation:** Bind approval to immutable command content, version, normalized registered scope, and authority; reject mixed-authority requests as a whole; ensure cancellation cannot spawn work; fail closed on unknown intent; and extend locked-intent vocabulary to financial trading. Require a fresh approval after meaningful edits.

### Release gate and current limits

A7 was **not integrated** into canonical MK at the time of the report; A8/A9 were **not delivered**; MUSE was unavailable. The acceptance target is 66/66 against real MK, plus existing routing and security regressions and independent implementation review. **No passing production authorization claim is made.** The XMAS-29 package was reported to exist in a local scratchpad, not confirmed delivered to Cursor or publicly reproduced. This section is based on the supplied assessment, not on a fresh independent test run.

### Why this matters to employers

The work illustrates requirements decomposition, test calibration, negative controls, root-cause prioritization, and responsible release decisions. Rather than treating a polished demo as evidence of safety, it identifies precisely what must be fixed and re-tested before deployment.

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

# The Master Key (MK)

**AI orchestration · human approval gates · mission verification · auditable automation**

[← Back to profile](../README.md) · [Portfolio](portfolio.md) · [Evidence index](evidence.md) · [Architecture diagram](mk-architecture.md) · [90-second demo storyboard](mk-demo-storyboard.md)

## The problem

AI automation is easy to demonstrate and much harder to govern. When multiple tools or workers contribute to a task, an operator needs to know what was requested, what actually ran, which evidence supports the result, and when human approval is required.

## The approach

Master Key is a founder-directed system under development for coordinating missions, tools, workers, verification, and review. The architecture emphasizes explicit boundaries rather than unrestricted autonomous action.

```text
Founder defines mission
        ↓
Scope + permissions + approval gates
        ↓
Dispatch to qualified worker (when available)
        ↓
Collect outputs and evidence
        ↓
Verify claims and record outcome
        ↓
Founder reviews consequential next steps
```

*This is an architecture overview, not evidence that every stage is currently connected to a live AI worker.*

## Engineering priorities

| Area | Purpose |
|---|---|
| Mission lifecycle | Make task status and handoffs explicit |
| Worker qualification | Distinguish callable workers from proposed integrations |
| Evidence and audit trail | Separate a worker's claims from independently checked results |
| Permission boundaries | Keep high-impact operations behind explicit approval |
| Failure handling | Make blocked, failed, and incomplete missions visible |
| Cost controls | Avoid silently activating paid services |

## Current status and limitations

**In development; private source.** The project has documented orchestration, governance, and testing work. An earlier local qualification reported **zero qualified programmatic AI workers** in its tested environment. A later disposable qualification demonstrated one **temporarily enrolled local AI worker**, as described below, but this does **not** establish a production-enrolled or independently verified AI workforce. Worker authentication, cancellation, expiry, and cost controls require environment-specific qualification before activation. Therefore this page **does not claim a running autonomous AI workforce, production deployment, or live 24/7 operation**.

### Local verification checkpoint — October 12, 2026

A **disposable, detached Windows worktree** at commit `f45598a3330e53d9216ba4061f6c8a99d2106eeb` was tested using Python 3.12.10 and pytest 9.1.1.

| Targeted test batch | Outcome |
|---|---|
| Security modules (4) | **146 passed** |
| Domain and persistence modules (8) | **174 passed, 1 skipped** |
| Total across those two batches | **320 passing test executions, 1 skip** |

**Verification scope:** These are self-run, local pytest results, **not** an independent audit, a CI result, or a run of the full 3,834 collected tests. The worktree contained **five test-file-only adjustments**: four outdated schema-version assertions changed from 26 to 35, a temporary runtime-fixture override for SQLite hardening tests, and fixture imports for restart durability. No production files were changed. Results **do not represent the pristine commit** and do not demonstrate live provider integration, continuous autonomy, or production readiness.

**Reproduction:** The domain/persistence batch was run with `python -m pytest tests/test_domain.py tests/test_m03_domain.py tests/test_m04_domain.py tests/test_m04_persistence.py tests/test_m05_domain.py tests/test_m05_persistence.py tests/test_m06_domain.py tests/test_sqlite_persistence_hardening.py -q --tb=short`. The four-module security batch was also run in the adjusted worktree. Exact test-only patches and sanitized logs still need publication for independent reproduction.

## October 2026 local AI worker qualification — reported checkpoint

Following the earlier no-worker assessment, the private MK project reported a **bounded local-model integration test** using Ollama 0.40.3 and Qwen2.5-Coder 7B on an RTX 5070 Laptop GPU. Three AI-assisted code-review missions executed through a governed adapter. The reported qualification harness passed **12/12 scenarios** and targeted regression checks passed **613/613**. Reported generation speed was approximately **53–62 tokens/second**, with **$0.00 in paid API calls** and the Wallet Lock engaged.

**What this establishes:** A local model was invoked through the orchestration pipeline in a disposable qualification environment, with authenticated result handling, packet checks, cancellation and timeout tests, and signed receipts.

**What it does not establish:** The model's code-review findings were mostly false or trivial. This is **not** evidence of reliable automated code review, an independently audited security boundary, production worker enrollment, unattended autonomy, or customer outcomes. The adapter was **uncommitted at the reported checkpoint**, the local runtime was stopped afterward, and no production signing key or worker was enrolled. All checks were performed by the development agent and repository tests; **no independent reviewer** participated.

**Recruiter relevance:** This is an example of integration testing, honest evaluation of model quality, security-conscious workflow design, and recognizing when a technically successful AI pipeline is not yet useful for its intended task. Private evidence is not reproduced in this public repository.

## What this project demonstrates

- Translating an ambitious automation goal into explicit operational states and safety boundaries.
- Designing around verifiable outputs and human control instead of relying on AI-generated assertions.
- Recognizing and documenting blockers before claiming a capability is live.

## Next public evidence milestones

1. Publish a sanitized mission lifecycle diagram and sample packet with fictional data.
2. Share a reproducible, non-sensitive demonstration of a bounded workflow.
3. Publish the exact test-only patch and sanitized logs for the dated local verification checkpoint.
4. Clearly distinguish simulated workers, rule-based workers, and real callable AI workers.

**Disclosure:** Public case study only. Internal source code, secrets, and sensitive operational details remain private.

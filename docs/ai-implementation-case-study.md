# AI Implementation Case Study — A local AI worker that passed the pipeline but failed the quality bar

**Audience:** AI Implementation Specialist · Automation Associate · AI Enablement · Technical Customer Success

[Back to GitHub profile](../README.md) · [Recruiter quick start](recruiter.md) · [Master Key overview](master-key.md) · [Public workflow demo](https://ashtoncodes316.github.io/AshtonCodes316/control-room/)

> **60-second takeaway:** I tested a local AI model inside a governed task workflow. The integration and security checks passed, but most of the model's code-review findings were wrong or trivial. The correct engineering decision was **not to promote it as a dependable reviewer**. This is a private-project, self-reported qualification, not an independent audit or customer deployment.

## The business problem

Teams want to use AI for repetitive technical and operational tasks. But making an AI model callable is only the beginning: the system also needs to know *who* performed the work, *what* was authorized, *whether* the response arrived in time, *what* it cost, and *whether* the answer was actually useful.

Master Key (MK) is a private AI orchestration project exploring these controls.

## My approach: requirements → implementation → validation

| Requirement | Reported implementation or check | Why a business team cares |
|---|---|---|
| Avoid unexpected vendor charges | Local Ollama model; Wallet Lock remained LOCKED; no paid API calls | Predictable approval and cost boundaries |
| Keep model execution local | Ollama 0.40.3 bound to 127.0.0.1, cloud features disabled for the test | Reduces exposure from external inference calls, without claiming full host isolation |
| Attribute worker results | Worker signatures, credential enrollment, packet binding | Helps reject unsigned or misattributed outputs |
| Handle failures | Cancellation, packet expiry, timeout, late-result rejection | Prevents stale work from silently counting as success |
| Preserve evidence | Signed receipts, citation checks, separate-process integrity checks | Makes it easier to inspect what happened |
| Check answer quality | Three source-code review missions with manual examination of findings | Prevents confusing technical success with task success |

**Workflow:**

```text
Human-scoped task
  → signed packet / expiry / approved lane
  → local AI generation
  → authenticated result and citation checks
  → human evaluation of usefulness
  → accept, reject, or hold for improvement
```

## What was tested

The reported October 2026 XMAS-02C qualification used **Qwen2.5-Coder 7B, Q4_K_M**, running through Ollama on an NVIDIA RTX 5070 Laptop GPU.

- **12/12** local-model qualification scenarios passed.
- **613/613** targeted regression tests passed in the reported final run.
- Three real local-model code-review tasks completed through the adapter.
- Observed generation speed was roughly **53–62 tokens/second** on the three tasks.
- The reported paid API cost was **$0.00**; this is not a measurement of electricity or hardware cost.
- The runtime was stopped after testing. The adapter was **not committed or production-enrolled at this checkpoint**.

**Important:** These numbers come from a developer/agent-produced private report and repository tests. They are not independently reproduced by this public portfolio.

## The unexpected result: quality was inadequate

| Trial | Model response | Evaluation reported in the project |
|---|---|---|
| Review of `router.py` | Five findings | Four false; one trivial missing docstring |
| Review of `osident.py` | No findings | No evidence the file was defect-free |
| Review of `cng.py` | One finding retained, one dropped | Retained finding restated a docstring; dropped finding cited nonexistent code |

The citation checker detected one fabricated quote and adjusted two line numbers. **Accurate quotations and signed results do not prove accurate reasoning.**

**Decision:** Treat the local model as an integration proof of concept, **not** a qualified independent code reviewer. A future release would need a representative evaluation set, measured precision/recall or another task-appropriate quality metric, human review, and a genuinely independent security assessment.

## How to see the approach in public

The private MK runtime is not published. These **separate, deterministic educational examples** demonstrate related workflow concepts using fictional inputs:

1. [Interactive Control Room](https://ashtoncodes316.github.io/AshtonCodes316/control-room/) — step through human approval and rejection.
2. [Customer onboarding Workflow Studio](https://ashtoncodes316.github.io/AshtonCodes316/workflow-studio/) — inspect blockers and handoffs.
3. [Runnable governance example](../examples/mk-governance/README.md) — review code and automated tests.
4. [Public Proof Lab](public-proof-lab.md) — inspect evidence scope and CI links.

None of these public demos invokes the private Ollama worker or proves production security.

## A 60-second recruiter walkthrough

**0–15 seconds — Problem:** “AI automation needs more than a working model call. Teams need approvals, traceable results, and clear failure handling.”

**15–30 seconds — Show:** Open the [Control Room](https://ashtoncodes316.github.io/AshtonCodes316/control-room/) and walk through a simulated approval and rejection.

**30–45 seconds — Explain the technical work:** “In my private Master Key project, I tested a local AI worker with signed task results, cancellation, expiry, and evidence checks. Twelve qualification scenarios passed.”

**45–60 seconds — Explain judgment:** “The model still made mostly incorrect code-review claims, so I didn't treat it as a reliable reviewer. I care about validating usefulness, not just getting a green test result.”

*This is a written demonstration script, not a recorded video.*

## What I would contribute in an entry-level role

- Translate customer or operations needs into clear workflow requirements and acceptance checks.
- Support AI and SaaS implementation with documented approvals, exceptions, and handoffs.
- Test both happy paths and failure paths before rollout.
- Explain technical limitations in plain language to customers and stakeholders.
- Help track quality and adoption without inventing productivity or revenue results.

## Limitations and next steps

The model and MK orchestration ran under the same Windows user, so this is not an independent trust boundary. A process with that user's privileges could access relevant credentials. There was no production worker enrollment, independent review, unattended operation authorization, customer integration, or demonstrated return on investment. Source code and private evidence remain unpublished.

**Next engineering milestone:** Create a sanitized evaluation dataset, compare model outputs against a human-checked answer key, test a stronger or task-specific model, and publish reproducible evidence before claiming reliable AI-assisted review.

---

**Contact:** [LinkedIn](https://www.linkedin.com/in/ashton-simmons-406793393/) · [GitHub profile](../README.md) · [Recruiter guide](recruiter.md)

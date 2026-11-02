# Demonstration readiness — public evidence versus next proof

**Reviewed November 2, 2026.** This is a documentation inventory, not a new execution of the private projects. Public CI results below are dated and must be checked at the linked commit; the private project statements remain self-reported unless separately reproduced.

## Ready to show a recruiter now

| Public example | What can be inspected | Evidence and limits |
|---|---|---|
| [Guided portfolio demo](guided-demo/) | Six-chapter interactive browser presentation | [Portfolio browser CI](https://github.com/AshtonCodes316/AshtonCodes316/actions/workflows/portfolio-screenshots.yml) checks pages at desktop/mobile widths. **Not a recorded video or live AI worker.** |
| [Control Room](control-room/) | Simulated human approval/rejection and evidence export | Static, deterministic browser scenario using fictional data; **not private MK or an authenticated production approval system**. |
| [Governance proof example](../examples/mk-governance/README.md) | Standalone Python code and ten test methods | [Public governance CI](https://github.com/AshtonCodes316/AshtonCodes316/actions/workflows/public-proof.yml); **not the private MK runtime**. |
| [Customer implementation simulator](../examples/implementation-simulator/README.md) | Runnable fictional onboarding scenarios and tests | [Simulator CI](https://github.com/AshtonCodes316/AshtonCodes316/actions/workflows/implementation-simulator.yml); **no actual customer, CRM integration, or business outcome**. |
| [Automation Lab](automation-lab/), [Workflow Studio](workflow-studio/), [Implementation Dashboard](implementation-dashboard/) | Browser-only workflow simulations | Automated browser CI checks page loading, JavaScript errors, overflow, and internal links. Founder-reported scenario walkthroughs are **not independently verified end-to-end**. |

**Latest independently checked public browser and Pages checkpoint before this review:** [browser PASS](https://github.com/AshtonCodes316/AshtonCodes316/actions/runs/40346362393) and [Pages PASS](https://github.com/AshtonCodes316/AshtonCodes316/actions/runs/40346363236), both October 26, 2026, commit `d3b87529`. New documentation commits need separate status verification. A green browser run is not a screen-reader audit, physical-phone test, or production security certification.

## Private projects — what is still needed

| Project | Current documented maturity | Next safe public proof |
|---|---|---|
| Master Key | Private architecture and **self-reported targeted** local testing; separate public simulations | Founder-approved, sanitized local recording with commit, commands, scope, and test output; independent security verification before production claims |
| TipFlow | Documented local Streamlit/SQLite prototype, **not** a public deployed service | Redacted walkthrough of actual prototype with fictional data and verified screenshots |
| Bubba Bucks | Documented research ingestion and validation tooling; no trading claim | Offline synthetic-data example with repeatable commands and dated results |
| TourneyNest | Architecture checkpoints; device testing deferred | Simulator/device evidence and sanitized UI screenshots |
| ApplyForge | Local-first workflow concept and development notes | Fictional-data, repeatable public workflow example |
| Merriwisp | Private repository; scope not publicly verified | Approved scope and implementation review before adding features or screenshots |

## Fastest credible next deliverable

The [90-second recruiter walkthrough](90-second-walkthrough.md) is **a script, not a video**. A genuine recording of the published Control Room rejection path, the public Python simulator and their limitations would improve interview readiness. Capture only real on-screen behavior, redact private information, and check narration, captions, links, and duration before publication.

## Evidence standard

For a claim labeled verified, provide the source or commit SHA, environment, exact commands, exit codes, observed results, scope, limitations, and publication approval. Keep private code, credentials, internal architecture details, and personal records out of public artifacts. A demo or passing test is never evidence of live AI integration, revenue, customers, or independent security certification.

[Recruiter quick start](recruiter.md) · [Project maturity](project-status.md) · [Evidence index](evidence.md) · [Portfolio quality report](portfolio-quality-report.md)

# Implementation Dashboard — Interactive Portfolio Demo #3

A browser-only, deterministic simulation of customer implementation milestone tracking, blocker detection, owner assignment, and a human approval gate.

**Expected GitHub Pages link:** https://ashtoncodes316.github.io/AshtonCodes316/implementation-dashboard/

The source is committed to the public profile repository's `docs` folder. GitHub Pages is configured for `main` / `docs`, but this new URL and functionality have **not yet been independently verified**.

## Guided smoke test

1. Open the demo and click **Evaluate account** with the defaults. Expect **BLOCKED — MILESTONES OPEN**.
2. Assign an implementation owner and mark all five milestones complete.
3. Click **Evaluate account** again. Expect **READY FOR APPROVAL**.
4. Leave go-live approval off and click **Check go-live gate**. Expect `BLOCKED_HUMAN_APPROVAL`.
5. Select Approved and check the gate again. Expect `GO_LIVE_REVIEW_ELIGIBLE`.
6. Download the JSON receipt and inspect the simulated inputs and decision.

## Why this matters to an implementation role

- Visualizes milestone completion and blockers.
- Maps outstanding tasks to a next-action list.
- Keeps human sign-off separate from technical readiness.
- Records decisions in a transparent local JSON receipt.
- Demonstrates an operator-oriented user interface.

## Truth boundaries

This is **not** an AI model, a live CRM integration, a production customer implementation tool, or the private Master Key runtime. All accounts are fictional, and milestone completion and approval are selected by the visitor; they are not authenticated or externally verified. No customer onboarding or go-live deployment is performed. No customer success metrics or business results are claimed.

A browser-generated SHA-256 checksum is not a digital signature or independent audit. Never enter real customer details, credentials, or sensitive information.

[Automation Lab](https://ashtoncodes316.github.io/AshtonCodes316/automation-lab/) · [Workflow Studio](https://ashtoncodes316.github.io/AshtonCodes316/workflow-studio/) · [Recruiter quick start](../recruiter.md)

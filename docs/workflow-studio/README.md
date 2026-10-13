# Workflow Studio — Customer Onboarding Simulator

**Interactive public portfolio project #2.** A static, rule-based customer onboarding readiness and handoff simulator.

## Try it

**GitHub Pages URL (expected when the site rebuilds):** https://ashtoncodes316.github.io/AshtonCodes316/workflow-studio/

The page is published from the existing `main` / `docs` GitHub Pages configuration. This link has **not yet been independently verified live**.

## Demo walkthrough

1. Open the page. With the default sample inputs, click **Evaluate readiness**. Expect **BLOCKED — ACTION REQUIRED**.
2. Change **Requirements confirmed** to Yes, **Required access approved** to Yes, and **Implementation owner** to a simulated role.
3. Click **Evaluate readiness** again. Expect **READY FOR REVIEW**.
4. Leave human sign-off unapproved and click **Prepare handoff receipt**. Expect **BLOCKED_HUMAN_SIGNOFF** in the receipt.
5. Choose approved sign-off, click **Prepare handoff receipt**, and expect **HANDOFF_RECEIPT_PREPARED**.
6. Download the JSON receipt and inspect the local evidence fields.

## What it demonstrates

- Requirements gathering and intake validation
- Fail-closed readiness checks and exception explanations
- Simulated ownership and human sign-off
- Transparent decision trails and downloadable JSON evidence
- Simple, dependency-free HTML/CSS/JavaScript

## What it does NOT do

No real customer data, live onboarding, CRM, API, AI model, message dispatch, authentication, or paid service. The role and approval fields are **simulated** and not a security control for a real business. No actual customer results or measured productivity gains are claimed.

The browser computes a SHA-256 checksum on secure origins where Web Crypto is available. The checksum is not a signature, proof of origin, or independent verification. Use fictional information only.

[Live Automation Lab](https://ashtoncodes316.github.io/AshtonCodes316/automation-lab/) · [Recruiter page](../recruiter.md) · [Business applications](../business-automation.md)

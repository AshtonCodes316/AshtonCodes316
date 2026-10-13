# Automation Lab — Interactive Browser Demo

A **static, browser-only** interactive portfolio example of an approval-gated support workflow.

## What you can try

1. Enter a **fictional** support request.
2. Leave approval off and run it: expect `BLOCKED_APPROVAL`.
3. Turn approval on and worker availability off: expect `BLOCKED_WORKER_UNAVAILABLE`.
4. Turn both on: expect `DRAFT_READY_FOR_HUMAN_REVIEW`.
5. Inspect and download the JSON evidence receipt. On a secure origin (HTTPS or localhost), the browser can also compute a SHA-256 digest.

**No AI model, external worker, CRM, help desk, or network API is called.** The classifier is a deliberately simple keyword heuristic. Nothing is submitted or sent. The user-entered text appears in the local receipt, so **do not enter sensitive information**.

## Live demonstration

[**Launch Automation Lab on GitHub Pages →**](https://ashtoncodes316.github.io/AshtonCodes316/automation-lab/)

The founder confirmed on October 12, 2026 that the site opened and the approval-blocked and approved-draft scenarios worked. This is user-reported verification, not an independent automated browser test. Deployment availability can change.

## Run locally

Open `index.html` in a modern browser. For SHA-256 support, serve the directory on localhost (for example, `python -m http.server 8000`) and visit the local page. Alternatively, host it as static files on GitHub Pages **if Pages is configured**. Merely committing these files does not mean the demo is deployed to a public URL.

## Review checklist

- Blank input does not produce a receipt.
- Unapproved request blocks even when worker is available.
- Approved request blocks if worker is unavailable.
- Only approved + available produces a **draft for review**, never a sent response.
- User text is rendered with `textContent`, not HTML.
- Receipt download remains disabled until a run succeeds.

## Relation to Master Key

This is a **new public educational prototype**, not a copy of or proof about the private Master Key system. It demonstrates ideas such as explicit approval, fail-closed handling, decision trails, and evidence formatting. It is **not** a live AI implementation or customer deployment.

[Recruiter page](../recruiter.md) · [MK engineering case study](../mk-engineering-case-study.md)

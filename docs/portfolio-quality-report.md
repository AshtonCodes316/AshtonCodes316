# Portfolio Quality Report — automated verification scope

**Updated:** October 17, 2026  
**Status:** Browser suite, axe-core audit, and GitHub Pages deployment **PASS** at commit `66ec237c` (October 17, 2026). Keyboard-navigation and touch-target evidence collection were subsequently added; their new run is pending. Manual accessibility and physical-device verification remain outstanding.

## What the existing browser suite checks

The portfolio already uses a Python/Playwright screenshot runner (`scripts/capture_portfolio.py`) and the GitHub Actions workflow `.github/workflows/portfolio-screenshots.yml`. The current workflow is configured to run on pushes to `main`, pull requests affecting the site/tests, and manual dispatch.

| Check | Coverage | Current evidence status |
|---|---|---|
| Render screenshots | 1440 × 900 desktop; 390 × 844 mobile | Automated; successful run confirmed at commit a3b19d3c |
| HTTP response | Each enumerated page must return HTTP 200 | Automated; successful run confirmed at commit a3b19d3c |
| JavaScript runtime errors | Browser `pageerror` capture | Automated; successful run confirmed at commit a3b19d3c |
| Horizontal overflow | Document scroll width versus viewport width | Automated; successful run confirmed at commit a3b19d3c |
| Internal broken links | HTTP status for same-origin links on enumerated pages | Automated; successful run confirmed at commit a3b19d3c |
| Interactive tour | Next, previous, restart, last-chapter stop | Automated; successful run confirmed at commit a3b19d3c |
| AI case-study architecture | Five stages, selection and explanation | Automated; successful run confirmed at commit a3b19d3c |
| Recruiter landing pages | One H1, guided-demo navigation | Automated; successful run confirmed at commit a3b19d3c |
| Accessibility smoke checks | Named visible links/buttons, image alt presence, duplicate IDs, exactly one H1 and main | Automated for five new experiences; successful run confirmed at commit a3b19d3c |

**Scope:** These are basic programmatic checks, not a comprehensive WCAG 2.2 AA audit. They do not establish screen-reader compatibility, keyboard usability for every widget, color contrast compliance, real-device performance, or cross-browser support.

## Confirmed browser-test and deployment evidence

- [Browser + accessibility workflow PASS — commit 66ec237c](https://github.com/AshtonCodes316/AshtonCodes316/actions/runs/39076268168).
- [GitHub Pages deployment PASS — commit 66ec237c](https://github.com/AshtonCodes316/AshtonCodes316/actions/runs/39076269087).

- [Browser + axe-core accessibility workflow PASS — commit ba268edf](https://github.com/AshtonCodes316/AshtonCodes316/actions/runs/39076058122).
- [GitHub Pages deployment PASS — commit ba268edf](https://github.com/AshtonCodes316/AshtonCodes316/actions/runs/39076058252).

- [Successful GitHub Actions run for commit a3b19d3c](https://github.com/AshtonCodes316/AshtonCodes316/actions/runs/39051527779) — completed successfully on October 17, 2026.
- [Successful GitHub Actions run for commit 8f67c593](https://github.com/AshtonCodes316/AshtonCodes316/actions/runs/39051516228) — includes accessibility smoke checks.
- [Successful GitHub Actions run for commit 5839b9f4](https://github.com/AshtonCodes316/AshtonCodes316/actions/runs/39051363565) — browser suite on push.
- **Verified:** The axe-core audit passed on `ba268edf` after correcting the guided tour's ARIA progress indicator. This confirms zero *blocking automated violations* in that run; any axe `incomplete` items still require human review.

## Keyboard and mobile target evidence

The browser test suite now exercises the guided demo with actual ArrowRight and ArrowLeft key presses while the tour is focused, checks that its accessible progress value updates, and records visible mobile links/buttons smaller than 24 pixels in either dimension to per-page JSON files. **This evidence collection does not by itself establish a WCAG touch-target failure**: spacing and exceptions require human review. The newly expanded suite has not yet been verified passing.

## Dedicated accessibility audit

The `scripts/audit_portfolio_accessibility.py` runner loads pinned axe-core 4.10.3 in Chromium against local pages, checks WCAG 2.0/2.1/2.2 A/AA-tagged rules at desktop and mobile viewports, and writes `browser-evidence/axe-accessibility-report.json`. The GitHub Actions job is configured to fail if any violations are reported. The check passed in the GitHub Actions run linked above; manual review remains necessary.

## Pages added to automated coverage

- [Guided portfolio tour](guided-demo/)
- [AI implementation interactive case study](ai-implementation/)
- [AI implementation recruiter page](ai-implementation-careers/)
- [Automation operations recruiter page](automation-operations/)
- [Technical customer success recruiter page](technical-customer-success/)

Existing pages remain in the same suite. The case-study hub assertion was updated from three to four sections after a fourth case study was added.

## How to verify

1. Open [GitHub Actions — Portfolio browser screenshots](https://github.com/AshtonCodes316/AshtonCodes316/actions/workflows/portfolio-screenshots.yml).
2. Select the newest run for `main`. If no run exists, use **Run workflow**.
3. Verify the `capture` job completed successfully; inspect any failure logs.
4. Download the `portfolio-browser-evidence` artifact and inspect screenshots and `report.json`.
5. Open the [guided tour](guided-demo/) and [AI case study](ai-implementation/) on a physical phone, check tap targets, readability, and navigation.
6. Only after verification, record the actual run URL, SHA, and pass/fail result here.

## Outstanding release criteria

- [x] Confirm a completed, passing GitHub Actions browser-suite run (a3b19d3c).
- [x] Confirm a passing run of the newly added axe-core audit (`ba268edf`).
- [ ] Review mobile and desktop screenshots for clipping and readability.
- [ ] Confirm new guided-demo keyboard automation passes, then manually test keyboard-only navigation across all new pages.
- [x] Resolve the blocking guided-tour ARIA violation and confirm the automated audit passes.
- [ ] Review any incomplete/manual-review items in the axe evidence artifact.
- [ ] Review mobile touch-target JSON evidence and assess WCAG spacing/exceptions.
- [ ] Perform at least one real-device iPhone visual check.
- [x] Confirm GitHub Pages deployment workflow succeeded for tested commit `ba268edf`.
- [ ] Independently compare the live rendered site with the tested commit.

## Evidence boundaries

This quality report describes **test coverage and verification work**, not an independently verified passing run. The public demos are browser-only educational simulations; private Master Key AI worker qualifications are separate, self-reported engineering evidence.

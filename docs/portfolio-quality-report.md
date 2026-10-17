# Portfolio Quality Report — automated verification scope

**Updated:** October 17, 2026  
**Status:** Browser quality suite expanded and committed. **Latest GitHub Actions PASS has not been independently confirmed.**

## What the existing browser suite checks

The portfolio already uses a Python/Playwright screenshot runner (`scripts/capture_portfolio.py`) and the GitHub Actions workflow `.github/workflows/portfolio-screenshots.yml`. The current workflow is configured to run on pushes to `main`, pull requests affecting the site/tests, and manual dispatch.

| Check | Coverage | Current evidence status |
|---|---|---|
| Render screenshots | 1440 × 900 desktop; 390 × 844 mobile | Automated; run result not yet confirmed |
| HTTP response | Each enumerated page must return HTTP 200 | Automated; run result not yet confirmed |
| JavaScript runtime errors | Browser `pageerror` capture | Automated; run result not yet confirmed |
| Horizontal overflow | Document scroll width versus viewport width | Automated; run result not yet confirmed |
| Internal broken links | HTTP status for same-origin links on enumerated pages | Automated; run result not yet confirmed |
| Interactive tour | Next, previous, restart, last-chapter stop | Automated; run result not yet confirmed |
| AI case-study architecture | Five stages, selection and explanation | Automated; run result not yet confirmed |
| Recruiter landing pages | One H1, guided-demo navigation | Automated; run result not yet confirmed |
| Accessibility smoke checks | Named visible links/buttons, image alt presence, duplicate IDs, exactly one H1 and main | Automated for five new experiences; run result not yet confirmed |

**Scope:** These are basic programmatic checks, not a comprehensive WCAG 2.2 AA audit. They do not establish screen-reader compatibility, keyboard usability for every widget, color contrast compliance, real-device performance, or cross-browser support.

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

- [ ] Confirm a completed, passing GitHub Actions run.
- [ ] Review mobile and desktop screenshots for clipping and readability.
- [ ] Perform keyboard-only navigation on the new pages.
- [ ] Run a dedicated axe-core or equivalent accessibility audit; review false positives and actual violations.
- [ ] Perform at least one real-device iPhone visual check.
- [ ] Verify the public GitHub Pages deployment matches the tested commit.

## Evidence boundaries

This quality report describes **test coverage and verification work**, not an independently verified passing run. The public demos are browser-only educational simulations; private Master Key AI worker qualifications are separate, self-reported engineering evidence.

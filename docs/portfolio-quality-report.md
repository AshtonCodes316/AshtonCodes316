# Portfolio Quality Report — automated verification scope

**Updated:** October 26, 2026  
**Verified public CI checkpoint:** [Browser/screenshots/accessibility workflow](https://github.com/AshtonCodes316/AshtonCodes316/actions/runs/39378519609) and [GitHub Pages deployment](https://github.com/AshtonCodes316/AshtonCodes316/actions/runs/39378519251) both **passed** on October 20, 2026 at commit `10360381` (merged recruiter experience launch). This replaces the earlier "CI pending push" status for the October 19 recruiter-track/brand changes. Subsequent documentation-only edits require their own run/status checks; see [current Actions history](https://github.com/AshtonCodes316/AshtonCodes316/actions). **Manual contrast/ARIA review, physical-device verification, and independent live-site comparison remain outstanding.** Historical local Playwright evidence (32 screenshots, zero reported failures) is not a substitute for a current CI artifact or a physical-device test.

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

The browser test suite now exercises the guided demo with actual ArrowRight and ArrowLeft key presses while the tour is focused, checks that its accessible progress value updates, and records visible mobile links/buttons smaller than 24 pixels in either dimension to per-page JSON files. **This evidence collection does not by itself establish a WCAG touch-target failure**: spacing and exceptions require human review. The expanded suite was subsequently verified by the passing October 20, 2026 browser workflow at commit `10360381`; this does not replace manual keyboard-only review of every interactive component.

## Actual mobile artifact review — October 17, 2026

Inspected the `portfolio-browser-evidence` artifact from [passing workflow 39077308750](https://github.com/AshtonCodes316/AshtonCodes316/actions/runs/39077308750). The 5 newly tested experiences report **31 visible links/buttons with a measured dimension under 24 CSS pixels**: guided demo 9, AI implementation 5, AI implementation careers 7, automation operations 5, and technical customer success 5. Most listed controls are inline links with ~19-pixel bounding-box heights. These are **review candidates**, not 31 confirmed WCAG failures; target spacing and exceptions were not evaluated.

The axe report contains `incomplete` entries, including color-contrast evaluations on multiple pages, which require manual review even though the automated violation count is zero. The artifact also identified one `aria-prohibited-attr` incomplete item on the homepage. No screen-reader or physical iPhone test was conducted.

**Artifact format correction:** The initial touch-target JSON files had an extra literal `\\n` after the JSON payload. This was corrected in the screenshot runner in commit `a3647f06`; the subsequent run must confirm the files parse directly.

## Verified mobile target improvement — October 17, 2026

Compared the actual mobile touch-target JSON files in the [earlier passing run 39079671905](https://github.com/AshtonCodes316/AshtonCodes316/actions/runs/39079671905) against the [new passing run 39080265059](https://github.com/AshtonCodes316/AshtonCodes316/actions/runs/39080265059). **31 flagged controls became 0** across the five tested pages at a 390-pixel browser viewport. Counts by page: guided demo **9 → 0**, AI implementation **5 → 0**, AI implementation careers **7 → 0**, automation operations **5 → 0**, technical customer success **5 → 0**. The JSON files in the latest artifact parse successfully. Both the browser workflow and [GitHub Pages deployment](https://github.com/AshtonCodes316/AshtonCodes316/actions/runs/39080264899) passed at commit `06c6a173`.

This metric uses the project's under-24-CSS-pixel candidate heuristic. It is **not** a WCAG conformance assessment, a physical-touchscreen test, or evidence that all mobile controls meet a 44-pixel design target. The axe report still contains incomplete contrast and ARIA items requiring human review.

## Dedicated accessibility audit

The `scripts/audit_portfolio_accessibility.py` runner loads pinned axe-core 4.10.3 in Chromium against local pages, checks WCAG 2.0/2.1/2.2 A/AA-tagged rules at desktop and mobile viewports, and writes `browser-evidence/axe-accessibility-report.json`. The GitHub Actions job is configured to fail if any violations are reported. The check passed in the GitHub Actions run linked above; manual review remains necessary.

## Pages added to automated coverage

- [Guided portfolio tour](guided-demo/)
- [AI implementation interactive case study](ai-implementation/)
- [AI implementation recruiter page](ai-implementation-careers/)
- [Automation operations recruiter page](automation-operations/)
- [Technical customer success recruiter page](technical-customer-success/)
- [AI Orchestration / Agentic Systems](ai-orchestration/) — added Oct 19, 2026 (included in Oct 20 public CI checkpoint)
- [AI Automation / Solutions Engineering](ai-automation/) — added Oct 19, 2026 (included in Oct 20 public CI checkpoint)
- [AI-Native Application Development](ai-native-apps/) — added Oct 19, 2026 (included in Oct 20 public CI checkpoint)

Existing pages remain in the same suite. The case-study hub assertion was updated from three to four sections after a fourth case study was added. The screenshot runner (`scripts/capture_portfolio.py`) now enumerates the three new tracks for HTTP, overflow, broken-link, touch-target, and accessibility smoke checks.

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
- [x] Confirm expanded guided-demo keyboard automation passes in the October 20 public browser workflow.
- [ ] Manually test keyboard-only navigation across all new pages.
- [x] Resolve the blocking guided-tour ARIA violation and confirm the automated audit passes.
- [ ] Review any incomplete/manual-review items in the axe evidence artifact.
- [ ] Review mobile touch-target JSON evidence and assess WCAG spacing/exceptions.
- [ ] Perform at least one real-device iPhone visual check.
- [x] Confirm GitHub Pages deployment workflow succeeded for tested commit `ba268edf`.
- [ ] Independently compare the live rendered site with the tested commit.

## Evidence boundaries

This quality report links **specific passing GitHub Actions runs** for the public portfolio. Those runs establish only the configured automated checks at the cited commits, not independent security certification, full WCAG conformance, live AI integration, or physical-device performance. Private Master Key qualifications remain separate self-reported engineering evidence. The public demos are browser-only educational simulations; private Master Key AI worker qualifications are separate, self-reported engineering evidence.

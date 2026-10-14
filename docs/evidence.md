# Verified Portfolio Evidence Index

This page separates **documented repository evidence** from future demonstrations. The original project source repositories remain private.

| Project | Evidence reviewed | What it supports | Still needed |
|---|---|---|---|
| The Master Key | Private README and Oct. 12, 2026 local pytest output | Architecture plus 146 security and 174 domain/persistence passing test executions (1 skipped) in an isolated worktree with five test-only adjustments | Exact patch, sanitized logs, CI/independent reproduction, broader integration qualification |
| Bubba Bucks | Private README and Python project metadata | Research pipeline scope, read-only data ingestion design, pytest/Ruff tooling | Redacted CLI demo and current test run |
| TourneyNest | Private README and architecture document | T0–T7 structural checkpoints, privacy-aware sharing design, deferred Apple integrations | Simulator/device verification and UI screenshots |
| TipFlow | Private README | Financial product concept for tipped workers | Implementation review and screenshots |
| ApplyForge | Private README | Local-first job application copilot concept | Implementation review and demo |
| Merriwisp | Private repository metadata | Repository exists | README, scope, and implementation review |

## Local MK verification disclosure

The Oct. 12 results are **self-reported local test runs**, not independent verification or pristine-commit results. The two tested batches total **320 passing test executions and one skip**. The full suite was **collected (3,834 tests), not run**. Five test files were changed in a disposable worktree; production code was unchanged. See [MK case study](master-key.md) for environment, commit, command, and limitations.

## Authorization acceptance investigation (XMAS-29)

A separate October 2026 local assessment reported a calibrated 66-case authorization suite: reference policy gate 66/66 on both tested trees, canonical MK 7/66, and isolated A7 16/66. Five deliberately insecure controls were reportedly detected by targeted tests. These results identify outstanding safety gaps and **do not** establish authorization readiness. The scratchpad evidence, including its SHA-256 inventory, is not publicly accessible or independently reproduced here. See the [authorization regression case study](mk-engineering-case-study.md#authorization-regression-investigation--october-2026-xmas-29).

## Publication rules

- Do not publish original private source, credentials, tokens, internal hostnames, or personal records.
- Screenshots must be reviewed and sanitized before publishing.
- Report project maturity accurately; do not imply production deployment or live customers without evidence.
- Show real test outputs only when their command, environment, and result have been verified.
- Treat architectural diagrams as illustrations, not proof of live execution.

[Back to portfolio](portfolio.md) · [Main profile](../README.md)

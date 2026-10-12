# MK private repository — controlled verification runbook

**Status: PREPARED, NOT EXECUTED.** This document describes a procedure for an authorized operator on a machine with access to the private repository. No new MK tests were run to create this document.

## Preconditions

- Use a disposable, isolated development environment with Python 3.12+ and sufficient disk space.
- Obtain authorization to access the private repository. Do not paste access tokens into commands, logs, or chat.
- Keep the repository private. Do not activate paid model providers, external workers, scheduled runtimes, or live integrations.
- Confirm which branch and commit should be tested. **Do not assume the most recent historical commit is the current canonical revision.**
- Review repository-specific setup and environment requirements before installing dependencies.

## Read-only inspection first

From an existing authorized checkout:

```bash
git remote -v
git status --short
git branch --show-current
git rev-parse HEAD
python --version
```

Review the output privately; remote URLs, usernames, and filesystem paths may be sensitive.

## Controlled Python test procedure

Use a fresh virtual environment; avoid altering a running MK installation.

```bash
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
python -m pytest -q
```

Record the command's exit code, number of collected/passed/failed/skipped tests, duration, dependency versions, and exact commit. A test result is not verified until actual output is reviewed. If dependencies cannot be installed without spending money or changing system software, **STOP and report BLOCKED**.

## Demo gate — separate from tests

The private README documents:

```bash
python -m master_key.cli demo
```

**Do not execute this automatically.** First inspect the current CLI's `demo` implementation and all downstream calls for writes, external API requests, background processes, credentials, and financial effects. Only run in an isolated disposable environment after that inspection and explicit approval.

## Evidence record template

```text
Date (UTC):
Repository: the-master-key (private)
Branch:
Full commit SHA:
Working tree clean?:
Operating system:
Python version:
Dependency install status:
Test command:
Test exit code:
Collected / passed / failed / skipped:
Duration:
Demo inspected?:
Demo authorized and executed?:
Demo exit code:
Unexpected network / writes / spending:
Limitations:
Reviewer:
Publication approved?:
```

## Publication rules

Publish a short redacted summary only after verifying logs and outputs. Remove secrets, tokens, personal data, private hostnames, internal file paths, sensitive security controls, and proprietary code. Never claim tests from one environment prove production readiness, and never conflate a standalone educational example with the actual MK runtime.

[Verification status](mk-verification-status.md) · [MK case study](master-key.md)

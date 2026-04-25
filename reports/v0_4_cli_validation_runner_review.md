# v0.4 CLI Validation Runner Review

## Executive Summary

v0.4 adds a lightweight CLI validation runner for the Markdown-first workflow prototype. The runner does not generate design content. It verifies repository structure, sample outputs, eval cases, existing validation scripts, and working-file public-safety rules.

This moves the project from static Markdown structure toward a minimally executable validation posture while preserving the core boundary: LLM-assisted workflow artifacts are reviewed by humans and not automatically approved.

## Files Added

| File | Purpose |
| --- | --- |
| `scripts/run_sample_workflow.py` | Standard-library CLI validation runner. |
| `docs/cli_validation_runner.md` | Explains purpose, usage, and boundaries. |
| `reports/v0_4_cli_validation_runner_review.md` | Captures v0.4 review and validation summary. |

## Files Updated

| File | Update |
| --- | --- |
| `README.md` | Added runner command to Quick Start and v0.4 direction section. |

## What v0.4 Demonstrates

- The repository can be checked with one command.
- Existing validation scripts can be coordinated by a simple runner.
- Required sample outputs and eval cases are treated as workflow assets.
- Public-safe scanning is part of the executable check.

## What It Does Not Demonstrate

- It does not generate design documents.
- It does not call LLMs or external APIs.
- It does not update baselines or artifacts.
- It does not approve decisions.

## Validation Results

| Command | Result |
| --- | --- |
| `python3 scripts/run_sample_workflow.py` | Passed |
| `python3 scripts/run_sample_workflow.py --write-report` | Passed |
| `python3 scripts/check_sensitive_identifiers.py` | Passed |
| `python3 scripts/validate_output_schema.py` | Passed |
| `python3 scripts/check_unresolved_assertions.py` | Passed |
| `python3 scripts/compare_expected_outputs.py` | Passed |
| `git diff --check` | Passed |

## Public-Safety Result

Working-file public-safe scan returned no hits for restricted markers or local email patterns.

## Remaining Gaps

| Gap | Recommendation |
| --- | --- |
| Validation is file and token based. | Add stricter schema/status validation in a later version. |
| Runner does not execute workflow transformations. | Consider a v0.5 CLI workflow generator only after validation remains stable. |
| Report output is generated but not interpreted. | Future CLI could summarize risk categories and recommended next actions. |

## Recommended Commit Message

```text
Add CLI validation runner
```

## Directory Handling

Only repository-local public-safe files were used. Private directories named in the working instructions were not read.

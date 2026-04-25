# CLI Validation Runner

## Purpose

The v0.4 CLI validation runner makes the Markdown-first workflow prototype reproducible with a single local command.

The CLI runner makes the Markdown-first workflow prototype reproducible without pretending to automate network design.

## Why v0.4 Adds A CLI Runner

v0.1 through v0.3 established the repository structure, meeting-to-design workflow slice, and evidence-to-decision loop. v0.4 adds a minimal executable layer so reviewers can verify that the repository still has required files, sample outputs, eval cases, validation scripts, and public-safe content.

## What The Runner Checks

- Required top-level files.
- Required directories.
- v0.1, v0.2, and v0.3 sample outputs.
- Eval cases.
- Existing validation scripts.
- Working-file public-safe scan excluding `.git`.

## What It Does Not Do

- It does not generate design content.
- It does not call an LLM.
- It does not call external APIs.
- It does not update design baselines.
- It does not approve design decisions.
- It does not publish or push anything.

## How To Run It

```bash
python3 scripts/run_sample_workflow.py
python3 scripts/run_sample_workflow.py --check-only
python3 scripts/run_sample_workflow.py --write-report
python3 scripts/run_sample_workflow.py --report-path reports/latest_cli_validation_run.md
```

## Example Output

```text
LLM Infra Design Studio - CLI Validation Runner
Repository root: /path/to/llm-infra-design-studio
Required files: passed
Required directories: passed
Sample outputs: passed
Eval cases: passed
Validation scripts: passed
Public-safe scan: passed
Overall result: passed
```

## Future Evolution

The runner is intentionally small. It can later become the entry point for stricter schema checks, workflow-specific validations, CLI subcommands, API-backed case execution, or a SaaS review interface. The approval boundary should remain unchanged: humans approve design decisions.

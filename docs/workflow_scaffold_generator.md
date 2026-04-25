# Workflow Scaffold Generator

## Purpose

The v0.6 scaffold generator creates empty workflow artifact sets that can be filled by engineers or future LLM-assisted steps.

The scaffold generator creates the structure for a workflow run; it does not decide the design.

## Why v0.6 Adds A Scaffold Generator

Earlier versions established the Markdown-first workflow, synthetic samples, evaluation checks, and CLI validation runner. v0.6 adds a small executable step that initializes a consistent artifact set for a new scenario.

This makes the repository usable as a starting point for repeatable workflow runs without pretending to automate infrastructure design decisions.

## Supported Workflows

- `meeting-to-design`
- `evidence-to-decision`

## What The Generator Creates

For `meeting-to-design`, the generator creates placeholders for meeting intake, issue and decision logs, stakeholder questions, design update proposal, and human approval checklist.

For `evidence-to-decision`, the generator creates placeholders for source manifest, official source reconciliation, information gap request, design decision packet, design reflection request, and human approval checklist.

Each generated file includes scenario metadata, workflow metadata, draft status, source reference placeholders, human approval requirements, and a warning that the scaffold is not an approved design update.

## What Generated Scaffolds Are Not

- They are not approved design artifacts.
- They are not production-ready architecture decisions.
- They are not generated from real customer data.
- They do not call an LLM or external API.
- They do not update source templates, samples, or production artifacts.

## How To Run It

List supported workflows:

```bash
python3 scripts/generate_workflow_scaffold.py --list-workflows
```

Create an evidence-to-decision scaffold:

```bash
python3 scripts/generate_workflow_scaffold.py \
  --scenario-id scenario_003 \
  --workflow evidence-to-decision \
  --output-dir generated/scenario_003 \
  --force
```

Preview a meeting-to-design scaffold without writing files:

```bash
python3 scripts/generate_workflow_scaffold.py \
  --scenario-id scenario_004 \
  --workflow meeting-to-design \
  --output-dir tmp/scenario_004 \
  --dry-run
```

## Example Commands

```bash
python3 scripts/generate_workflow_scaffold.py --list-workflows
python3 scripts/generate_workflow_scaffold.py --scenario-id scenario_003 --workflow evidence-to-decision --output-dir generated/scenario_003 --force
python3 scripts/run_sample_workflow.py --check-only
```

## Future LLM-Assisted Generation

The generator creates the file structure and approval-safe placeholders first. A future LLM-assisted step can then fill sections within those boundaries, while preserving source references, uncertainty, and human approval requirements.

## Future CLI / API / SaaS Evolution

The generator can later become a CLI subcommand, API endpoint, or SaaS workflow initialization action. The core boundary should remain stable: generation may prepare artifacts for review, but humans approve design decisions.

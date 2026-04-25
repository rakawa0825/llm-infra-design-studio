# Artifact Generation

## Purpose

Generate structured Markdown and CSV artifacts from reviewed inputs.

## When to Use

Use after verification and human merge decisions.

## Inputs

- Approved requirements
- Delta report
- Templates

## Example Inputs

- `samples/output/sample_requirements_table.md`
- `samples/output/sample_delta_report.md`
- `templates/design_update_proposal_template.md`

## Process

1. Select the target template.
2. Fill fields with source-backed content.
3. Preserve unresolved and assumption labels.
4. Mark draft or approved status.

## Outputs

- Updated artifact draft

## Example Outputs

- `templates/design_update_proposal_template.md`
- `templates/detail_design_handoff_template.md`

## Quality Checks

- Template sections are complete.
- Source IDs are retained.

## Failure Modes

- Producing final-looking content before approval.

## Human Review Required

Required before publication or handoff.

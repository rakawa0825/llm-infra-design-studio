# Delta Impact Analysis

## Purpose

Identify how new information changes existing design artifacts.

## When to Use

Use when new review comments, vendor answers, or requirements arrive.

## Inputs

- Previous artifacts
- New sources
- Current source manifest

## Example Inputs

- `samples/output/sample_requirements_table.md`
- `samples/input/sample_review_comments.md`
- `samples/output/sample_source_manifest.md`

## Process

1. Compare meaning, not just wording.
2. Classify each delta by impact.
3. Identify affected artifacts.
4. Mark merge decision owner.

## Outputs

- Delta report
- Update proposal

## Example Outputs

- `samples/output/sample_delta_report.md`
- `templates/design_update_proposal_template.md`

## Quality Checks

- Every delta has a source.
- Impact and approval status are explicit.

## Failure Modes

- Hiding scope changes as editorial edits.

## Human Review Required

Required for merge decisions and scope changes.

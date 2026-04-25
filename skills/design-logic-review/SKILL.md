# Design Logic Review

## Purpose

Review extracted requirements for consistency, gaps, and design implications.

## When to Use

Use after requirement extraction and before verification.

## Inputs

- Requirements table
- Communication matrix
- Review comments

## Example Inputs

- `samples/output/sample_requirements_table.md`
- `samples/output/sample_communication_matrix.csv`
- `samples/input/sample_review_comments.md`

## Process

1. Check each requirement against target architecture.
2. Identify contradictions and gaps.
3. Create handoff items for detailed design.
4. Flag human approval needs.

## Outputs

- Design logic review notes
- Handoff item list

## Example Outputs

- `templates/detail_design_handoff_template.md`
- `samples/output/sample_unresolved_issues.md`

## Quality Checks

- No contradiction is silently resolved.
- Detailed-design items are separated from approved decisions.

## Failure Modes

- Treating draft logic as accepted design.

## Human Review Required

Required for all design conclusions.

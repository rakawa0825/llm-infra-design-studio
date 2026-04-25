# Meeting Intake

## Purpose

Convert public-safe meeting or hearing notes into structured source input for the design lifecycle.

## When to Use

Use at the start of a meeting-to-design cycle or when new hearing notes arrive.

## Inputs

- Meeting transcript
- Meeting date
- Source owner
- Participant roles

## Process

1. Confirm the input is synthetic or approved for public use.
2. Record meeting purpose, source owner, and date.
3. Identify candidate facts, assumptions, issues, decisions, and confirmation items.
4. Assign or request a source ID for downstream traceability.

## Outputs

- Meeting intake record
- Source manifest update candidate
- Candidate extraction list

## Quality Checks

- Source origin is clear.
- No private names or real project data are included.
- Candidate items preserve uncertainty.

## Failure Modes

- Treating meeting notes as final decisions.
- Mixing private content with synthetic examples.
- Losing participant role context.

## Human Review Required

Required for source acceptance and uncertain source origin.

## Example Inputs

- `samples/input/sample_design_review_meeting_transcript.md`
- `templates/meeting_intake_template.md`

## Example Outputs

- `samples/output/sample_issue_register.md`
- `samples/output/sample_decision_log.md`

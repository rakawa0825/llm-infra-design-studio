# Stakeholder Question Generation

## Purpose

Create targeted questions for customer, vendor, internal review, and detailed-design follow-up.

## When to Use

Use after issue extraction, decision extraction, or design logic review.

## Inputs

- Issue register
- Requirements table
- Decision log
- Vendor answer

## Process

1. Identify unclear requirement, ownership, risk, or implementation statements.
2. Classify each question by stakeholder owner.
3. Attach source reference and design impact.
4. Mark required response before baseline or handoff.

## Outputs

- Stakeholder question list
- Confirmation item list

## Quality Checks

- Each question has a target owner.
- Each question explains design impact.
- Questions do not imply a preferred answer.

## Failure Modes

- Asking broad questions that do not resolve an artifact decision.
- Assigning the wrong stakeholder owner.
- Turning a question into an assumption.

## Human Review Required

Required before sending customer-facing or vendor-facing questions.

## Example Inputs

- `samples/output/sample_issue_register.md`
- `samples/output/sample_decision_log.md`

## Example Outputs

- `samples/output/sample_stakeholder_questions.md`

# Review Required Policy

## Purpose

This policy defines when future LLM-assisted output should use `review_required` or `needs_more_information`.

## Use `review_required` When

- The output is structurally valid but needs human review.
- A proposed artifact update is awaiting approval.
- Risk acceptance may be required.
- Customer confirmation is required.
- Vendor confirmation is required.
- A design decision packet is ready for review but not approved.

## Use `needs_more_information` When

- Source evidence is insufficient.
- Ownership is unresolved.
- Source statements conflict.
- An official source is missing.
- Baseline comparison is missing.
- Required source references are incomplete.

## Normal Review Flow

`review_required` is normal and acceptable. It means the package can move to human review.

`needs_more_information` is also acceptable when evidence is insufficient. It means the workflow should request additional information before proposing design changes.

## Approval Boundary

`approved_by_human` cannot be produced by LLM output. It can only be set by a human approval record after review.

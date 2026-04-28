# Text Document Output Templates

## Purpose

The artifact templates define reusable text-based document structures for the LLM-assisted Infrastructure Design Lifecycle Framework.

They make document generation explicit, but they do not bypass engineering review. They are review artifacts, not final approved customer deliverables.

## Why text-based output is the v0.1 priority

v0.1 prioritizes Markdown and YAML outputs because they are easy to inspect, diff, review, and validate.

The goal is to generate traceable design content before rendering it into any specific corporate template.

Text-based outputs make it easier to preserve:

- source traceability,
- lifecycle phase,
- document status,
- approval status,
- unresolved items,
- missing inputs,
- detailed-design handoff items,
- human approval boundaries.

## Relationship to lifecycle phases

The templates map to lifecycle phases:

- `requirement_definition_draft.md`: Requirement Definition.
- `high_level_design_patch.md`: High-Level Design.
- `detailed_design_handoff.md`: Detailed-Design Handoff.
- `review_response_draft.md`: Review Response.
- `human_approval_checklist.md`: Human Approval.
- `unresolved_items.yaml`: Requirement Clarification and Validation.
- `missing_inputs.yaml`: Requirement Clarification and Validation.
- `design_issue_log.yaml`: High-Level Design and Review Response.

## Relationship to `samples/lifecycle_minimal/`

The lifecycle minimal sample shows one concrete synthetic instance of the v0.1 flow.

The templates in `templates/artifacts/` generalize that sample so future synthetic cases can reuse the same artifact structure without copying scenario-specific values.

## Template directory

Artifact templates are stored in:

```text
templates/artifacts/
```

Current templates:

- `requirement_definition_draft.md`
- `high_level_design_patch.md`
- `detailed_design_handoff.md`
- `review_response_draft.md`
- `human_approval_checklist.md`
- `unresolved_items.yaml`
- `missing_inputs.yaml`
- `design_issue_log.yaml`

## What templates do not prove

Templates do not prove:

- production readiness,
- correctness for a real network design,
- human approval,
- customer acceptance,
- security certification,
- deployment safety.

They define reviewable document structure. They do not make the generated content correct by themselves.

## Future adapter layer

Company-specific formatting belongs in a future artifact adapter layer.

The v0.1 priority is to generate traceable text-based design content before rendering it into a specific corporate template.

Future adapters may render approved or reviewable content into:

- Word templates,
- Excel workbooks,
- PowerPoint decks,
- company-specific document templates.

Those adapters should not change the approval boundary. They should only render content whose source traceability, unresolved items, missing inputs, and human approval state are already explicit.

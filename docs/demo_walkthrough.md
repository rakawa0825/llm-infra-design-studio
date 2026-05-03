# Demo Walkthrough

## Purpose

This walkthrough shows what the v0.1 lifecycle sample produces.

It helps reviewers answer:

- What goes in?
- What gets normalized?
- What design artifacts come out?
- What remains unresolved?
- What requires human approval?
- What does validation check?

This is a synthetic public-safe walkthrough. It is not a production meeting-minutes system. It is not a real customer design. It is not final approved design language.

## Demo Flow Overview

```text
Input evidence
-> Intermediate lifecycle state
-> Text-based design outputs
-> Validation
-> Human approval boundary
```

```text
customer_hearing_note.md
meeting_transcript_excerpt.md
existing_design_excerpt.md
review_comments.yaml
vendor_note.md
        ↓
evidence_registry.yaml
requirement_candidates.yaml
unresolved_items.yaml
missing_inputs.yaml
design_issue_log.yaml
        ↓
requirement_definition_draft.md
high_level_design_patch.md
detailed_design_handoff.md
review_response_draft.md
human_approval_checklist.md
        ↓
validate_lifecycle_minimal.py
validate_artifact_generation_plan.py
check_sensitive_identifiers.py
```

## Before: Scattered Synthetic Inputs

| Input | Role | Contributes | Cannot prove |
| --- | --- | --- | --- |
| [`customer_hearing_note.md`](../samples/lifecycle_minimal/input/customer_hearing_note.md) | customer intent evidence | requirement candidates | final approval |
| [`meeting_transcript_excerpt.md`](../samples/lifecycle_minimal/input/meeting_transcript_excerpt.md) | meeting context | discussion / action context | final design language |
| [`existing_design_excerpt.md`](../samples/lifecycle_minimal/input/existing_design_excerpt.md) | baseline context | current documented state | current correctness |
| [`review_comments.yaml`](../samples/lifecycle_minimal/input/review_comments.yaml) | review gap evidence | design issues | correct answer |
| [`vendor_note.md`](../samples/lifecycle_minimal/input/vendor_note.md) | technical behavior reference | behavior constraints | customer approval |

The inputs are intentionally incomplete. They represent scattered evidence, not a clean prompt.

## Intermediate: Lifecycle State

| Intermediate artifact | Purpose |
| --- | --- |
| [`evidence_registry.yaml`](../samples/lifecycle_minimal/intermediate/evidence_registry.yaml) | registers evidence sources and authority |
| [`requirement_candidates.yaml`](../samples/lifecycle_minimal/intermediate/requirement_candidates.yaml) | holds candidate requirements before approval |
| [`unresolved_items.yaml`](../samples/lifecycle_minimal/intermediate/unresolved_items.yaml) | preserves unresolved questions |
| [`missing_inputs.yaml`](../samples/lifecycle_minimal/intermediate/missing_inputs.yaml) | tracks missing information required for final language |
| [`design_issue_log.yaml`](../samples/lifecycle_minimal/intermediate/design_issue_log.yaml) | maps gaps, conflicts, and handoff needs to design artifacts |

This layer prevents meeting statements, vendor notes, or review comments from being promoted directly into final design language.

## After: Text-Based Design Outputs

| Output artifact | What it shows | Approval state |
| --- | --- | --- |
| [`requirement_definition_draft.md`](../samples/lifecycle_minimal/output/requirement_definition_draft.md) | source-backed requirement candidates | `REVIEW_REQUIRED` |
| [`high_level_design_patch.md`](../samples/lifecycle_minimal/output/high_level_design_patch.md) | proposed high-level design / basic design patch | `REVIEW_REQUIRED` |
| [`detailed_design_handoff.md`](../samples/lifecycle_minimal/output/detailed_design_handoff.md) | items moved to detailed design | `REVIEW_REQUIRED` |
| [`review_response_draft.md`](../samples/lifecycle_minimal/output/review_response_draft.md) | response draft for review comments | `REVIEW_REQUIRED` |
| [`human_approval_checklist.md`](../samples/lifecycle_minimal/output/human_approval_checklist.md) | decisions requiring human approval | not approved by default |

The outputs are text-based review artifacts, not final customer deliverables.

## What This Demonstrates

- scattered evidence can be normalized,
- customer intent becomes requirement candidates, not final requirements,
- existing design excerpts can be treated as possibly stale baseline,
- review comments become design gaps, not automatic design answers,
- vendor notes become technical references, not customer approval,
- unresolved items remain visible,
- detailed-design handoff is separated from high-level design,
- human approval remains required.

## What This Does Not Demonstrate

- no real meeting system is included,
- no real customer data is included,
- no real LLM API execution is included,
- no production UI is included,
- no Word / Excel / PowerPoint rendering is included,
- no network config generation is included,
- no network diagram generation is included,
- no final design approval is automated.

## Validation

```bash
python3 scripts/run_sample_workflow.py --check-only
python3 scripts/validate_lifecycle_minimal.py
python3 scripts/validate_artifact_generation_plan.py
python3 scripts/check_sensitive_identifiers.py
```

- `run_sample_workflow.py --check-only` validates repository structure and sample checks.
- `validate_lifecycle_minimal.py` validates lifecycle sample IDs and approval-boundary discipline.
- `validate_artifact_generation_plan.py` validates artifact plan paths and claims.
- `check_sensitive_identifiers.py` checks configured sensitive identifier patterns.

Validation does not prove real network design correctness or approve design language.

## Additional v0.2 Traceability Sample

For a Markdown-only traceability prototype slice, see [Workspace Minimal Traceability Sample](../samples/workspace_minimal/README.md).

It shows a synthetic ID chain from source evidence to validation result record and can be checked with:

```bash
python3 scripts/validate_workspace_minimal.py
```

This sample is not a production workflow and does not include an automated approval system.

## Private Meeting System Boundary

This public repository does not include the private operational meeting system.

A private meeting/transcript runner may implement evidence intake, routing, normalization, extraction, resolution, validation, and private output adapters. This repository only models public-safe abstractions, synthetic samples, artifact contracts, and validation patterns.

See: [`docs/integration/private_meeting_system_adapter_boundary.md`](integration/private_meeting_system_adapter_boundary.md)

## Reviewer Takeaway

The useful question is not whether this is a finished product.

The useful question is whether the workflow preserves evidence, uncertainty, lifecycle phase, and human approval boundaries while preparing reviewable infrastructure design artifacts.

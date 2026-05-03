# v0.2 Traceability Direction

Status: planned direction / not implemented

## Purpose

This note describes a public-safe v0.2 direction for making infrastructure design artifacts more traceable across source evidence, requirements, design sections, review work, decisions, handoffs, and validation results.

This is a roadmap note only. It does not define implemented capability, production readiness, or repository license changes.

The direction builds on the existing v0.2 Markdown-first, ID-driven, Git-backed workspace idea by making the trace chain explicit before adding samples, validators, runners, or adapters.

## Why Traceability Matters

Infrastructure design work often depends on scattered evidence, unresolved questions, proposed edits, human review, and downstream handoff decisions.

If those items are only converted into a polished document, reviewers can lose sight of:

- which source led to which requirement,
- which design section is affected,
- which review item remains unresolved,
- which patch is proposed but not approved,
- which decision created a handoff,
- which validation result was checked before review.

The v0.2 traceability direction is meant to keep those connections visible. The goal is not generic document generation. The goal is source-backed, reviewable, human-approved design workflow support.

## Proposed ID Taxonomy

Candidate ID prefixes:

| Prefix | Meaning |
| --- | --- |
| `SRC` | Source evidence |
| `REQ` | Requirement or requirement candidate |
| `DS` | Design section |
| `RV` | Review item |
| `PD` | Patch draft |
| `DR` | Diff review |
| `DL` | Decision log |
| `HO` | Handoff item |
| `VR` | Validation result |

The recommended public-safe ID shape is:

```text
PREFIX-000
```

IDs should be stable once referenced. They should help reviewers follow evidence, assumptions, unresolved items, patch drafts, decisions, handoffs, and validation results without treating AI-generated text as automatically approved design language.

## Example Synthetic Trace Chain

A future synthetic trace chain may look like:

```text
SRC-001 -> REQ-001 -> DS-001 -> RV-001 -> PD-001 -> DR-001 -> DL-001 -> HO-001 -> VR-001
```

Example interpretation:

- `SRC-001`: a synthetic source evidence item,
- `REQ-001`: a requirement candidate derived from the source,
- `DS-001`: the design section affected by the requirement,
- `RV-001`: a review question or unresolved item,
- `PD-001`: a proposed design patch,
- `DR-001`: review feedback on the patch,
- `DL-001`: a human decision record,
- `HO-001`: a downstream handoff item,
- `VR-001`: a validation result that records what was checked.

This chain is illustrated in the Markdown-only synthetic sample at [Workspace Minimal Traceability Sample](../../samples/workspace_minimal/README.md). The sample is not an implementation, runner, validator, or production workflow.

## Minimal Workspace Concept

A future minimal workspace may use simple Markdown files grouped by artifact type.

Possible future shape:

```text
workspace_minimal/
  README.md
  trace_map.md
  sources/
  requirements/
  design_sections/
  review_items/
  patch_drafts/
  diff_reviews/
  decision_logs/
  handoffs/
  validation_results/
```

This structure is represented as a Markdown-only synthetic sample at `samples/workspace_minimal/`. The sample is for review of traceability shape only; it does not implement automated workflow behavior.

The intended workspace properties are:

- Markdown-first,
- readable in Git diffs,
- ID-driven,
- synthetic-example only,
- explicit about unresolved items,
- explicit about human approval boundaries,
- suitable for future lightweight validation.

## Future Validation Direction

Future validation may include:

- ID uniqueness validation,
- filename-to-ID consistency checks,
- relationship validation between referenced IDs,
- unresolved item visibility checks,
- handoff traceability checks,
- validation-result reference checks,
- human approval boundary checks.

Future validators should support review readiness. They should not approve design decisions, close unresolved issues, or replace qualified engineering judgment.

The current limited validator for the Markdown-only sample is documented in [Workspace Minimal Validation](../validation/workspace_minimal_validation.md).

## Public Safety Boundary

Any future public v0.2 traceability sample must use synthetic examples only.

Do not include:

- real operational data,
- real customer names,
- real project names,
- company or internal organization names,
- hostnames,
- private runtime URLs,
- transcripts,
- design excerpts,
- review comment excerpts,
- secrets,
- private runner behavior,
- private connector behavior.

The public repository may describe public-safe abstractions and synthetic examples. It must not include a private meeting system, private runner, real transcript import, or real customer workflow data.

## What Is Not Included

This direction does not include:

- no runner,
- no UI,
- no FastAPI,
- no private connector,
- no private meeting system implementation,
- no production deployment,
- no autonomous design approval,
- no real customer data,
- no validator scripts in this note,
- no OSS/license change.

v0.2 must not be described as implemented until public-safe sample files, validation behavior, documentation, and release boundaries exist and are reviewed.

## Possible Future Steps

Possible future steps:

1. Define a minimal public-safe `workspace_minimal` sample structure.
2. Draft a synthetic traceability walkthrough.
3. Design ID uniqueness validation before implementing any validator.
4. Design relationship validation before implementing any validator.
5. Add public-safe sample files only after the structure and validation story are reviewed.
6. Add validator scripts only after docs and samples establish the expected behavior.
7. Keep v0.1 positioning intact while presenting v0.2 as a planned traceability direction.

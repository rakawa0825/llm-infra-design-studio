# Artifact Generation Contract

## 1. Purpose

The artifact generation contract defines how lifecycle intermediate outputs are transformed into text-based review artifacts.

Document generation is required, but generation is not generic free-form writing. Generated artifacts must be source-backed, phase-aware, reviewable, and approval-gated.

The contract ensures that generation preserves:

- source evidence,
- lifecycle phase,
- unresolved items,
- missing inputs,
- approval boundaries,
- detailed-design handoff items,
- validation requirements.

The v0.1 priority is to produce reviewable text artifacts before any future Word / Excel / PowerPoint rendering.

## 2. Contract model

Each artifact generation entry should use this model:

```yaml
artifact_id: "<artifact_id>"
artifact_type: "<artifact_type>"
lifecycle_phase: "<phase>"
template_path: "<template_path>"
output_path: "<output_path>"
input_sources:
  - "<source_id>"
intermediate_dependencies:
  - "<intermediate_file_or_id>"
required_sections:
  - "<section_name>"
approval_gate: "<approval_gate_name>"
review_state: "REVIEW_REQUIRED"
allowed_claims:
  - "<allowed_claim>"
forbidden_claims:
  - "<forbidden_claim>"
validation_checks:
  - "<validation_check>"
```

The contract should be read as an approval-boundary document. It states what may be generated, what must remain visible, and what must not be claimed.

## 3. Required artifact types

### `requirement_definition_draft`

- **Purpose:** draft requirement definitions from source-backed candidates.
- **Required inputs:** requirement candidates, unresolved items, missing inputs, evidence registry.
- **Required template:** `templates/artifacts/requirement_definition_draft.md`.
- **Expected output:** `requirement_definition_draft.md`.
- **Approval boundary:** candidate requirements remain `REVIEW_REQUIRED` until human approval.
- **Must not claim:** final customer-approved requirements or production-ready design.

### `high_level_design_patch`

- **Purpose:** draft high-level design / basic design text changes.
- **Required inputs:** design issue log, existing design excerpt, review comments, requirement candidates.
- **Required template:** `templates/artifacts/high_level_design_patch.md`.
- **Expected output:** `high_level_design_patch.md`.
- **Approval boundary:** patch remains `DRAFT` and `REVIEW_REQUIRED` until approved.
- **Must not claim:** final routing parameters, production readiness, or final customer approval.

### `detailed_design_handoff`

- **Purpose:** separate parameter-level or implementation-level items from high-level design.
- **Required inputs:** unresolved items, vendor note, review comments.
- **Required template:** `templates/artifacts/detailed_design_handoff.md`.
- **Expected output:** `detailed_design_handoff.md`.
- **Approval boundary:** handoff items require human owner review before closure.
- **Must not claim:** that detailed-design questions are resolved or approved.

### `review_response_draft`

- **Purpose:** draft responses to review comments without closing them prematurely.
- **Required inputs:** review comments, design issue log, related sources.
- **Required template:** `templates/artifacts/review_response_draft.md`.
- **Expected output:** `review_response_draft.md`.
- **Approval boundary:** review comments are not closed by default.
- **Must not claim:** comment closure without human approval.

### `human_approval_checklist`

- **Purpose:** collect approval gates for requirement, design patch, handoff, review response, and artifact reflection.
- **Required inputs:** all relevant sources, unresolved items, missing inputs, and output artifacts.
- **Required template:** `templates/artifacts/human_approval_checklist.md`.
- **Expected output:** `human_approval_checklist.md`.
- **Approval boundary:** no item is approved by default.
- **Must not claim:** approval state unless a human approval record exists.

### `unresolved_items`

- **Purpose:** preserve unresolved design or requirement questions.
- **Required inputs:** normalized evidence, review comments, meeting context.
- **Required template:** `templates/artifacts/unresolved_items.yaml`.
- **Expected output:** `unresolved_items.yaml`.
- **Approval boundary:** unresolved items remain open until reviewed by a human owner.
- **Must not claim:** issue closure, accepted risk, or final design language.

### `missing_inputs`

- **Purpose:** identify inputs required before an artifact can be finalized.
- **Required inputs:** requirement clarification notes, review comments, source gaps.
- **Required template:** `templates/artifacts/missing_inputs.yaml`.
- **Expected output:** `missing_inputs.yaml`.
- **Approval boundary:** missing inputs block final design language until resolved.
- **Must not claim:** completeness when required inputs are absent.

### `design_issue_log`

- **Purpose:** track gaps, conflicts, handoff needs, and review-response needs.
- **Required inputs:** existing design excerpts, review comments, requirement candidates.
- **Required template:** `templates/artifacts/design_issue_log.yaml`.
- **Expected output:** `design_issue_log.yaml`.
- **Approval boundary:** issues remain review artifacts until handled by human owners.
- **Must not claim:** final resolution without approval.

## 4. Lifecycle minimal mapping

The lifecycle minimal sample uses the contract as follows:

```text
intermediate/requirement_candidates.yaml
+ intermediate/unresolved_items.yaml
+ intermediate/missing_inputs.yaml
-> output/requirement_definition_draft.md

intermediate/design_issue_log.yaml
+ input/existing_design_excerpt.md
+ input/review_comments.yaml
-> output/high_level_design_patch.md

intermediate/unresolved_items.yaml
+ input/vendor_note.md
-> output/detailed_design_handoff.md

input/review_comments.yaml
+ intermediate/design_issue_log.yaml
-> output/review_response_draft.md

all relevant sources
+ unresolved items
+ output artifacts
-> output/human_approval_checklist.md
```

The concrete plan for this sample is defined in:

```text
samples/lifecycle_minimal/artifact_generation_plan.yaml
```

## 5. Approval boundary

Artifact generation does not approve the artifact.

Generated text remains `DRAFT` and `REVIEW_REQUIRED` unless a human approval record exists.

The contract requires that:

- missing inputs remain visible,
- unresolved items do not disappear,
- detailed-design handoff items are not promoted into basic design decisions,
- vendor-style technical behavior does not become customer approval,
- review comments are not closed by default,
- artifact reflection requires human approval.

## 6. Future adapter boundary

Future Word / Excel / PowerPoint adapters may render approved or reviewable text artifacts into company-specific formats.

The v0.1 priority is the text-generation contract, not layout rendering.

Adapters must not weaken source traceability, unresolved item handling, review state visibility, or human approval boundaries.

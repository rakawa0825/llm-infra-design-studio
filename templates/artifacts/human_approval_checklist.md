# <artifact_title>

## Checklist status

- checklist_status: "DRAFT"
- default_approval_state: "not approved"
- artifact_reflection_allowed: false

No item is approved by default.

## Requirement approval

- [ ] requirement_id: "<requirement_id>"
  - decision_owner_role: "<owner_role>"
  - affected_artifact: "<artifact>"
  - source_ids:
    - "<source_id>"
  - approval_state: "REVIEW_REQUIRED"
  - risk_if_approved_incorrectly: "<risk>"

## High-level design / basic design patch approval

- [ ] patch_id: "<patch_id>"
  - decision_owner_role: "<owner_role>"
  - affected_artifact: "<artifact>"
  - source_ids:
    - "<source_id>"
  - approval_state: "REVIEW_REQUIRED"
  - risk_if_approved_incorrectly: "<risk>"

## Detailed-design handoff approval

- [ ] handoff_item_id: "<unresolved_item_id>"
  - decision_owner_role: "<owner_role>"
  - affected_artifact: "<artifact>"
  - source_ids:
    - "<source_id>"
  - approval_state: "REVIEW_REQUIRED"
  - risk_if_approved_incorrectly: "<risk>"

## Review response approval

- [ ] review_comment_id: "<review_comment_id>"
  - decision_owner_role: "<owner_role>"
  - affected_artifact: "<artifact>"
  - source_ids:
    - "<source_id>"
  - approval_state: "REVIEW_REQUIRED"
  - risk_if_approved_incorrectly: "<risk>"

## Artifact reflection approval

- [ ] artifact_id: "<artifact_id>"
  - decision_owner_role: "<owner_role>"
  - source_ids:
    - "<source_id>"
  - approval_state: "REVIEW_REQUIRED"
  - risk_if_approved_incorrectly: "<risk>"

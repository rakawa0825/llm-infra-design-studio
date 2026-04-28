# Human Approval Checklist

## Status

- Checklist status: `DRAFT`
- Default approval state: not approved
- Artifact reflection allowed: No

## Requirement approval

- [ ] **Decision owner role:** customer approval owner.
  - **Affected artifact:** `requirement_definition_draft.md`
  - **Source IDs:** `SRC-001`, `SRC-002`, `SRC-004`
  - **Approval state:** `REVIEW_REQUIRED`
  - **Risk if approved incorrectly:** candidate intent may become final requirement language without confirmed inspection scope.

## High-level design / basic design patch approval

- [ ] **Decision owner role:** infrastructure architect.
  - **Affected artifact:** `high_level_design_patch.md`
  - **Source IDs:** `SRC-001`, `SRC-003`, `SRC-004`, `SRC-005`
  - **Approval state:** `REVIEW_REQUIRED`
  - **Risk if approved incorrectly:** stale baseline or unresolved exception traffic may be reflected into design language.

## Unresolved item handling

- [ ] **Decision owner role:** security reviewer.
  - **Affected artifact:** `unresolved_items.yaml`
  - **Source IDs:** `SRC-001`, `SRC-002`, `SRC-004`, `SRC-005`
  - **Approval state:** `REVIEW_REQUIRED`
  - **Risk if approved incorrectly:** unresolved inspection or exception scope may be closed prematurely.

## Detailed-design handoff approval

- [ ] **Decision owner role:** detailed design owner.
  - **Affected artifact:** `detailed_design_handoff.md`
  - **Source IDs:** `SRC-002`, `SRC-004`, `SRC-005`
  - **Approval state:** `REVIEW_REQUIRED`
  - **Risk if approved incorrectly:** routing, failover, or monitoring details may be handled at the wrong design phase.

## Review response approval

- [ ] **Decision owner role:** review coordinator.
  - **Affected artifact:** `review_response_draft.md`
  - **Source IDs:** `SRC-004`
  - **Approval state:** `REVIEW_REQUIRED`
  - **Risk if approved incorrectly:** review comments may appear closed without approved evidence.

## Artifact reflection approval

- [ ] **Decision owner role:** design governance owner.
  - **Affected artifact:** all output artifacts.
  - **Source IDs:** `SRC-001`, `SRC-002`, `SRC-003`, `SRC-004`, `SRC-005`
  - **Approval state:** `REVIEW_REQUIRED`
  - **Risk if approved incorrectly:** draft text may become authoritative design language without approval.

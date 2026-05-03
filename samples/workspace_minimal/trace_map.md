# Workspace Minimal Trace Map

Status: synthetic trace map / not production-ready

## Complete Chain

```text
SRC-001 -> REQ-001 -> DS-001 -> RV-001 -> PD-001 -> DR-001 -> DL-001 -> HO-001 -> VR-001
```

## Relationship Table

| From | Relationship | To | Meaning |
| --- | --- | --- | --- |
| `SRC-001` | `derived_into` | `REQ-001` | Synthetic source evidence informs a requirement candidate. |
| `REQ-001` | `targets` | `DS-001` | The requirement candidate affects a design section. |
| `DS-001` | `reviewed_by` | `RV-001` | The design section has an unresolved review question. |
| `RV-001` | `addressed_by` | `PD-001` | A patch draft proposes wording for review. |
| `PD-001` | `reviewed_by` | `DR-001` | The proposed patch receives diff review feedback. |
| `DR-001` | `decided_by` | `DL-001` | The diff review leads to a human-owned decision record. |
| `DL-001` | `creates_handoff` | `HO-001` | The decision creates follow-up work. |
| `HO-001` | `validated_by` | `VR-001` | The handoff and related open items are recorded in a validation result. |

## Unresolved Item Visibility

| ID | Status | Visibility |
| --- | --- | --- |
| `RV-001` | `open` | Planned-maintenance tolerance is not confirmed. |
| `DL-001` | `deferred` | Final design language is deferred until tolerance is confirmed. |
| `HO-001` | `pending` | Follow-up confirmation is required before downstream design work. |

## Approval Status

| ID | Human approval | Current state |
| --- | --- | --- |
| `REQ-001` | `required` | Requirement candidate needs review. |
| `PD-001` | `required` | Patch draft is not approved final language. |
| `DL-001` | `required` | Decision records deferral, not approval. |
| `HO-001` | `required` | Handoff is pending confirmation. |
| `VR-001` | `required` | Validation result records visibility checks only. |

## Validation Status

| ID | Status | Meaning |
| --- | --- | --- |
| `VR-001` | `pass_with_open_items` | The synthetic chain is visible, and open items remain explicit. |

`VR-001` is a Markdown record, not an automated validator output.

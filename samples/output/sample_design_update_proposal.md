# Sample Design Update Proposal

## Proposal Summary

Draft updates are proposed for Branch-B exception handling, monitoring handoff, and Cloud-Security-Service logging confirmation. This proposal is not approved design.

## Source Evidence

| Source ID | Evidence Summary |
| --- | --- |
| SRC-006 | Synthetic design review meeting identified Branch-B exception uncertainty, monitoring threshold handoff, and vendor logging confirmation needs. |

## Proposed Artifact Updates

| Proposal ID | Impacted Artifact | Proposed Update | Status | Source Reference | Human Approval Required |
| --- | --- | --- | --- | --- | --- |
| UPD-010 | Requirements table | Add Branch-B temporary local breakout as customer confirmation item. | customer_confirmation_required | SRC-006 | Yes |
| UPD-011 | Communication matrix | Add placeholder row for Branch-B exception behavior only after customer confirmation. | human_approval_required | SRC-006 | Yes |
| UPD-012 | Unresolved issues | Add vendor confirmation item for log retention and export format. | vendor_confirmation_required | SRC-006 | Yes |
| UPD-013 | Detailed-design handoff | Add monitoring threshold definition for tunnel availability events. | detailed_design_handoff | SRC-006 | Yes |

## Open Questions

- Does the customer confirm Branch-B temporary local breakout during migration?
- What logging retention and export format will the vendor configuration use?
- Which detailed-design owner defines monitoring thresholds?

## Human Approval Points

- Approve or reject UPD-010 before requirements baseline changes.
- Approve communication matrix update only after customer confirmation.
- Review operations impact before accepting logging readiness.

## Status Allowed Values

- confirmed
- assumption
- unresolved
- customer_confirmation_required
- vendor_confirmation_required
- internal_review_required
- detailed_design_handoff
- human_approval_required

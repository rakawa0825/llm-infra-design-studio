# Sample Issue Register

| Issue ID | Issue | Category | Owner Role | Status | Impact | Next Action | Source Reference | Approval Required |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ISS-010 | Branch-B temporary local breakout behavior is not confirmed. | Customer confirmation | Customer owner | customer_confirmation_required | May change communication matrix and traffic steering requirements. | Ask customer to confirm migration exception behavior. | SRC-006 | Yes |
| ISS-011 | Cloud-Security-Service log retention period is not confirmed. | Vendor confirmation | Vendor owner | vendor_confirmation_required | May affect operations acceptance and logging handoff. | Request vendor retention and export-format confirmation. | SRC-006 | Yes |
| ISS-012 | Monitoring alert thresholds are not defined. | Detailed-design handoff | Detailed design owner | detailed_design_handoff | May affect monitoring readiness and alert ownership. | Define thresholds during detailed design. | SRC-006 | Yes |

## Human Approval Points

- Do not close ISS-010 without customer confirmation.
- Do not accept operations readiness until ISS-011 has a vendor answer and human review.
- Carry ISS-012 into detailed-design handoff.

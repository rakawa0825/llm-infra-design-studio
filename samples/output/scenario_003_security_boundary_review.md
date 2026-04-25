# Scenario 003 Security Boundary Review

| boundary_id | traffic_scope | inspection_scope | enforcement_point | excluded_traffic | responsibility_owner | confirmation_required | approval_status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SEC-BND-003-001 | Branch internet traffic | unresolved | Cloud-Security-Service | point-of-sale traffic may be excluded | security_reviewer | customer and vendor confirmation | vendor_confirmation_required |
| SEC-BND-003-002 | DR failover branch traffic | unresolved | Cloud-Security-Service | unknown | architecture_reviewer | security inspection behavior during DR | human_approval_required |

## Human Approval Points

- Inspection scope is not approved.
- Excluded traffic must be confirmed before communication matrix reflection.

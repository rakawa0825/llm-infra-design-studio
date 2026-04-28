# High-Level Design Patch

This patch corresponds to a high-level design / basic design document update.

## Status

- Patch status: `DRAFT`
- Review state: `REVIEW_REQUIRED`
- Final customer approval: No
- Production readiness: No

## Proposed section title

Branch Traffic Handling and Cloud Security Inspection

## Current gap

The existing design excerpt describes a legacy managed network path for branch internet-bound traffic. It does not explicitly define cloud security inspection scope, exception traffic handling, monitoring or management traffic treatment, or detailed routing policy behavior.

Related issue IDs:

- `DI-001`
- `DI-002`
- `DI-003`

## Proposed draft text

Branch internet-bound traffic is a candidate for cloud security inspection. The final inspection scope remains `REVIEW_REQUIRED` until the customer approval owner confirms which traffic classes are in scope.

Exception traffic, including possible monitoring or management traffic, must not be treated as approved bypass traffic until reviewed. Detailed routing policy, failover behavior, and monitoring traffic handling are assigned to detailed-design handoff.

## Source references

- `SRC-001`: customer hearing note.
- `SRC-002`: meeting transcript excerpt.
- `SRC-003`: existing design excerpt.
- `SRC-004`: review comments.
- `SRC-005`: vendor-style technical behavior note.

## Unresolved dependencies

- `UNRES-001`: exception traffic definition.
- `UNRES-002`: monitoring and management traffic handling.
- `UNRES-003`: failover and routing policy behavior.

## Detailed-design handoff markers

- Routing policy behavior must be validated in detailed design.
- Monitoring or management traffic treatment must be validated by operations and detailed design owners.
- Failover behavior must not be written as a final high-level design decision.

## Human approval requirement

This patch must be reviewed and approved by the appropriate human owner before it is reflected into a high-level design artifact.

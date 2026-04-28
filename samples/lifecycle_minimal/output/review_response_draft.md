# Review Response Draft

## Status

- Document status: `DRAFT`
- Review state: `REVIEW_REQUIRED`
- Closed comments: none

## Responses

### `RC-001`

- **Comment:** Security inspection scope for branch internet-bound traffic is not defined.
- **Draft response:** The current draft identifies branch internet-bound traffic as a requirement candidate for cloud security inspection. Final inspection scope remains `REVIEW_REQUIRED` pending human approval.
- **Status:** `REVIEW_REQUIRED`
- **Related source IDs:** `SRC-001`, `SRC-002`, `SRC-004`
- **Next action:** confirm approved inspection scope.
- **Closure allowed:** No, not without human approval.

### `RC-002`

- **Comment:** Exception traffic handling is unclear and may affect monitoring or management traffic.
- **Draft response:** Exception traffic is listed as unresolved and assigned to detailed-design handoff. Monitoring and management traffic handling must be validated separately.
- **Status:** `REVIEW_REQUIRED`
- **Related source IDs:** `SRC-001`, `SRC-004`, `SRC-005`
- **Next action:** confirm exception traffic list and owner role.
- **Closure allowed:** No, not without human approval.

### `RC-003`

- **Comment:** Existing design excerpt describes a legacy traffic path that may conflict with the new inspection requirement.
- **Draft response:** The existing design excerpt is treated as baseline context and stale baseline candidate. It does not override newer hearing or review evidence.
- **Status:** `REVIEW_REQUIRED`
- **Related source IDs:** `SRC-003`, `SRC-004`
- **Next action:** compare baseline language against approved requirement scope.
- **Closure allowed:** No, not without human approval.

### `RC-004`

- **Comment:** Detailed routing policy, failover behavior, and monitoring traffic treatment need detailed-design handoff.
- **Draft response:** These items are separated into `detailed_design_handoff.md` and must not be written as final high-level design decisions.
- **Status:** `REVIEW_REQUIRED`
- **Related source IDs:** `SRC-002`, `SRC-004`, `SRC-005`
- **Next action:** assign detailed-design owners.
- **Closure allowed:** No, not without human approval.

# Sample Delta Report

| Delta ID | New Source | Previous Understanding | New Information | Impacted Artifact | Impact | Recommendation | Human Decision |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DELTA-001 | SRC-003 | Branch-A and Branch-B had the same assumed cloud security behavior. | Branch-B may require a temporary migration exception. | Requirements table, communication matrix | Medium | Defer until customer confirms. | Pending |
| DELTA-002 | SRC-004 | Cloud-Security-Service logging was assumed generally available. | Retention period and export format require confirmation. | Requirements table, unresolved issues | Medium | Add vendor confirmation item. | Pending |
| DELTA-003 | SRC-003 | Monitoring integration was listed as a requirement. | Exact thresholds should be handled in detailed design. | Requirements table, handoff checklist | Low | Mark as detailed-design handoff. | Pending |

## Assumptions

- No delta is approved until the human decision column changes from pending.

## Human Approval Points

- Decide whether DELTA-001 changes target design scope.
- Approve DELTA-002 as a vendor confirmation item.
- Approve DELTA-003 as a detailed-design handoff item.

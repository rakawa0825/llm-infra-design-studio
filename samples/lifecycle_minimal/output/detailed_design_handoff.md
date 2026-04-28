# Detailed-Design Handoff

## Status

- Document status: `DRAFT`
- Review state: `REVIEW_REQUIRED`
- Approved detailed-design decision: No

## Purpose

This document separates items that must not be decided in high-level design.

## Handoff items

### `UNRES-001` Exception traffic definition

- **Target owner role:** security reviewer.
- **Source references:** `SRC-001`, `SRC-002`, `SRC-004`, `SRC-005`.
- **Required decision:** identify which traffic classes may bypass cloud security inspection.
- **Parameter or policy questions:**
  - Which traffic classes are exception traffic?
  - Which exceptions require customer approval?
  - Which exceptions require operational monitoring?
- **Approval requirement:** human approval required before design reflection.

### `UNRES-002` Monitoring and management traffic handling

- **Target owner role:** operations reviewer.
- **Source references:** `SRC-001`, `SRC-004`, `SRC-005`.
- **Required decision:** confirm whether monitoring or management traffic follows the inspection path or an exception path.
- **Parameter or policy questions:**
  - What traffic classes are considered monitoring or management traffic?
  - Does inspection affect monitoring continuity?
  - What alerting or operational handoff is required?
- **Approval requirement:** human approval required before design reflection.

### `UNRES-003` Failover and routing policy behavior

- **Target owner role:** network architect.
- **Source references:** `SRC-002`, `SRC-003`, `SRC-004`, `SRC-005`.
- **Required decision:** validate routing policy and failover behavior for inspected and exception traffic.
- **Parameter or policy questions:**
  - What is the preferred path for inspected traffic?
  - What behavior is expected during failover?
  - Does exception traffic follow the same failover path?
- **Approval requirement:** human approval required before design reflection.

## Boundary

These items are not high-level design decisions. They require detailed-design validation before any final artifact language is accepted.

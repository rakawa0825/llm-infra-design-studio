# Artifact Map Model

## Purpose

The Artifact Map records how source evidence may affect review artifacts and proposed artifact updates.

## Role In The Lifecycle

The artifact map sits between evidence classification and artifact update proposal. It helps reviewers understand which sources affect which artifacts, which sections may need updates, and which dependencies remain unresolved.

## Artifact Type Taxonomy

- `communication_matrix`
- `network_domain_review_packet`
- `design_decision_packet`
- `design_reflection_request`
- `routing_impact_analysis`
- `security_boundary_review`
- `monitoring_logging_review`
- `dr_failover_review`
- `human_approval_checklist`
- `issue_register`
- `decision_log`

## Source-To-Artifact Impact Relationship

Each artifact map entry should identify:

- related source IDs
- impacted artifact type
- impacted sections
- proposed updates
- unresolved dependencies
- approval requirements
- do-not-reflect-yet items

## Artifact Status Taxonomy

- `draft`
- `review_required`
- `needs_more_information`
- `approved_by_human`
- `superseded`
- `rejected`

`approved_by_human` can only be set by humans.

## Update Proposal Boundary

The artifact map can record proposed updates, but proposed updates are not approved design changes. They remain review artifacts until a human approver decides.

## Human Approval Boundary

Humans must approve artifact updates, risk acceptance, customer-facing statements, unresolved item closure, and production-impacting changes.

## Relationship To Source Registry

The artifact map must reference source IDs from the source registry. If a source is missing, stale, or unresolved, the downstream artifact should be `needs_more_information` or `review_required`.

## Relationship To Design Baseline

Artifact map entries should identify when a source may affect an existing design baseline. Baseline changes require review before reflection.

## Relationship To Future RAG/MCP Integration

The artifact map gives future RAG/MCP workflows a structured way to identify which artifacts may be impacted by retrieved sources. This repository does not implement RAG or MCP integration yet.

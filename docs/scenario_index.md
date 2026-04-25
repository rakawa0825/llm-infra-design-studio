# Scenario Index

## Purpose

This index helps reviewers inspect the synthetic scenarios without reading the entire repository.

## scenario_001 / ExampleCorp

### Purpose

Demonstrate the original Markdown-first workflow for source manifests, requirements, deltas, unresolved issues, and human approval.

### Input Files

- `samples/input/sample_meeting_transcript.md`
- `samples/input/sample_existing_design_excerpt.md`
- `samples/input/sample_review_comments.md`
- `samples/input/sample_vendor_answer.md`
- `samples/input/sample_communication_requirements.csv`

### Output Files

- `samples/output/sample_source_manifest.md`
- `samples/output/sample_requirements_table.md`
- `samples/output/sample_delta_report.md`
- `samples/output/sample_unresolved_issues.md`
- `samples/output/sample_human_approval_checklist.md`
- `samples/output/sample_communication_matrix.csv`

### What It Demonstrates

- Source traceability.
- Requirement extraction.
- Delta review.
- Unresolved issue preservation.
- Human approval checkpoints.

### Human Approval Boundary

The scenario does not approve design decisions, close unresolved items, or authorize production artifact updates.

## scenario_002 / Northstar Manufacturing

### Purpose

Demonstrate a second synthetic workflow shape focused on data center resilience, operations monitoring, DR failover alerting, and communication matrix impact.

### Input Files

- `samples/input/scenario_002_design_review_meeting.md`
- `samples/input/scenario_002_existing_design_baseline.md`
- `samples/input/scenario_002_operations_requirements.csv`
- `samples/input/scenario_002_vendor_answer.md`

### Output Files

- `samples/output/scenario_002_source_manifest.md`
- `samples/output/scenario_002_requirements_table.md`
- `samples/output/scenario_002_issue_register.md`
- `samples/output/scenario_002_decision_log.md`
- `samples/output/scenario_002_delta_report.md`
- `samples/output/scenario_002_design_decision_packet.md`
- `samples/output/scenario_002_information_gap_request.md`
- `samples/output/scenario_002_design_reflection_request.md`
- `samples/output/scenario_002_human_approval_checklist.md`

### What It Demonstrates

- Multiple synthetic scenario coverage.
- Issue and decision separation.
- Operations and monitoring impact.
- DR and communication matrix review.
- Human approval and information gap handling.

### Human Approval Boundary

Tentative decisions remain review-required. Vendor-style answers are supporting evidence, not approval.

## scenario_003 / Atlas Retail

### Purpose

Demonstrate the v0.9 network design domain pack across communication matrix, routing / SD-WAN, security / SSE boundary, monitoring / logging, and DR / failover review.

### Input Files

- `samples/input/scenario_003_network_domain_meeting.md`
- `samples/input/scenario_003_network_baseline.md`
- `samples/input/scenario_003_network_requirements.csv`
- `samples/input/scenario_003_synthetic_vendor_note.md`

### Output Files

- `samples/output/scenario_003_network_domain_review_packet.md`
- `samples/output/scenario_003_routing_impact_analysis.md`
- `samples/output/scenario_003_security_boundary_review.md`
- `samples/output/scenario_003_monitoring_logging_review.md`
- `samples/output/scenario_003_dr_failover_review.md`

### What It Demonstrates

- Network-domain classification.
- Communication matrix impact.
- Routing / SD-WAN impact.
- Security / SSE boundary impact.
- Monitoring / logging impact.
- DR / failover impact.

### Human Approval Boundary

The scenario creates review artifacts only. Routing behavior, inspection scope, monitoring ownership, DR behavior, and artifact reflection remain human-approved decisions.

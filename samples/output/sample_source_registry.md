# Sample Source Registry

## Purpose

This synthetic registry records public-safe evidence sources and their downstream artifact relationships.

## Source Registry

| Source ID | Source Type | Source Title | Source Summary | Source Status | Authority Level | Owner Role | Source Date Or Version | Related Workflow | Related Artifacts | Privacy Classification | Freshness Status | Unresolved Items | Human Review Required | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-REG-001 | meeting_transcript | ExampleCorp meeting transcript | Synthetic meeting evidence for initial workflow review. | active | meeting_statement | project_control | v1 | meeting-to-design | sample_requirements_table; sample_delta_report | public_safe_synthetic | current | confirmation items remain open | true | Meeting statements are not approval. |
| SRC-REG-002 | vendor_answer | Northstar Manufacturing vendor answer | Synthetic vendor-style response for monitoring behavior. | active | vendor_provided | vendor_reviewer | v1 | evidence-to-decision | scenario_002_information_gap_request; scenario_002_design_decision_packet | public_safe_synthetic | current | logging scope partially unresolved | true | Supporting evidence only. |
| SRC-REG-003 | meeting_transcript | Atlas Retail network domain meeting | Synthetic review meeting for network domain classification. | active | meeting_statement | network_reviewer | v1 | network-domain-review | scenario_003_network_domain_review_packet; scenario_003_routing_impact_analysis | public_safe_synthetic | current | DR behavior is tentative | true | Not approved design. |
| SRC-REG-004 | official_source_excerpt | Synthetic official source excerpt | Generic source excerpt for cloud security steering. | active | official | security_reviewer | v1 | evidence-to-decision | sample_official_source_reconciliation; sample_design_decision_packet | public_safe_synthetic | current | applicability requires review | true | Official-like synthetic excerpt. |
| SRC-REG-005 | existing_design_baseline | Existing design baseline | Synthetic baseline used for comparison before deltas. | needs_review | internal_review | architecture_reviewer | v1 | evidence-to-decision | sample_design_decision_packet; sample_design_reflection_request | public_safe_synthetic | needs_review | baseline assumptions unresolved | true | Baseline is not final approval. |

## Source Type Taxonomy

- meeting_transcript
- official_source_excerpt
- existing_design_baseline
- review_comment
- vendor_answer
- customer_confirmation
- operations_requirement
- communication_requirement
- issue_log
- decision_log

## Source Status Taxonomy

- draft
- active
- superseded
- unresolved
- confirmed
- needs_review

## Authority Levels

- official
- customer_confirmed
- vendor_provided
- internal_review
- meeting_statement
- assumption

## Human Approval Boundary

Source registry entries do not approve design decisions. Authority changes, customer confirmation, risk acceptance, and artifact reflection require human review.

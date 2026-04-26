# Sample Artifact Map

## Purpose

This synthetic artifact map records how source evidence may affect review artifacts and proposed updates.

## Artifact Map

| Artifact ID | Artifact Type | Artifact Title | Artifact Status | Related Sources | Impacted Sections | Proposed Updates | Unresolved Dependencies | Approval Required | Approver Role | Next Action | Do Not Reflect Yet |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ART-MAP-001 | communication_matrix | Sample communication matrix | review_required | SRC-REG-001; SRC-REG-003 | Branch traffic rows | Add proposed Cloud-Security-Service rows after confirmation. | ports and protocols unresolved | true | network_reviewer | request detailed-design confirmation | true |
| ART-MAP-002 | network_domain_review_packet | Scenario 003 network domain review packet | review_required | SRC-REG-003 | domain coverage; approval points | Preserve cross-domain impact findings. | DR behavior tentative | true | architecture_reviewer | route for human approval | true |
| ART-MAP-003 | design_decision_packet | Sample design decision packet | review_required | SRC-REG-004; SRC-REG-005 | confirmed facts; assumptions; gaps | Prepare review packet with baseline comparison. | official applicability requires review | true | architecture_reviewer | collect missing confirmation | true |
| ART-MAP-004 | information_gap_request | Sample information gap request | needs_more_information | SRC-REG-002; SRC-REG-005 | information gaps | Ask targeted questions for unresolved logging and baseline assumptions. | logging scope partially unresolved | true | operations_reviewer | request owner response | true |
| ART-MAP-005 | design_reflection_request | Sample design reflection request | review_required | SRC-REG-003; SRC-REG-004 | proposed artifact updates | Draft reflection request only after source review. | inspection scope unresolved | true | design_governance_director | hold until approval | true |
| ART-MAP-006 | human_approval_checklist | Sample human approval checklist | review_required | SRC-REG-001; SRC-REG-002; SRC-REG-003 | approval points | Track required approvals before artifact reflection. | multiple approval owners | true | design_governance_director | review approval scope | true |

## Source-To-Artifact Traceability

This section records source-to-artifact traceability for synthetic review artifacts.

- `SRC-REG-001` affects requirement and delta artifacts.
- `SRC-REG-002` affects information gaps and decision packets.
- `SRC-REG-003` affects network domain review and routing impact artifacts.
- `SRC-REG-004` affects official source reconciliation and decision packets.
- `SRC-REG-005` affects baseline comparison and reflection requests.

## Human Approval Points

- Artifact updates require human approval.
- approved_by_human can only be set by humans.
- Proposed updates are review artifacts, not final design.

## Do Not Reflect Yet

Do not reflect proposed updates when source evidence is unresolved, baseline assumptions are stale, or approval ownership is unclear.

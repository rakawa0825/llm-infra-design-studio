# Communication Matrix Model

## Purpose

The communication matrix model defines how network communication requirements should be reviewed before they become artifact updates.

## Required Fields

| Field | Meaning |
| --- | --- |
| source_zone | Logical source zone. |
| destination_zone | Logical destination zone. |
| source_component | Source component or site. |
| destination_component | Destination component or service. |
| protocol | Protocol under review. |
| port | Port or port range under review. |
| direction | Traffic direction. |
| traffic_purpose | Business or technical purpose. |
| security_inspection_requirement | Whether inspection is required, assumed, or unresolved. |
| logging_requirement | Whether logging is required, assumed, or unresolved. |
| approval_status | Review and approval status. |
| unresolved_items | Open questions or gaps. |
| related_source_references | Source IDs supporting the entry. |

## Communication States

- confirmed communication
- assumed communication
- proposed communication
- unresolved communication
- detailed-design handoff

## Human Review

Communication entries that affect policy, routing, inspection, logging, or production traffic require human approval before reflection into final artifacts.

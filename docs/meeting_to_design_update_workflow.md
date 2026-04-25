# Meeting-to-Design Update Workflow

## Overview

The v0.2 workflow connects meeting and hearing inputs to design artifact updates. It preserves source traceability, separates issues from decisions, identifies design deltas, and routes human approval checkpoints.

| Stage | Input | Process | Output | Risk | Human Approval / Escalation |
| --- | --- | --- | --- | --- | --- |
| 1. Meeting intake | Meeting notes or transcript | Record source owner, date, participants by role, and public-safe status. | Meeting intake record | Private or unclear source origin | Escalate uncertain source origin before use. |
| 2. Source manifest update | Meeting intake record | Assign source ID and downstream use. | Updated source manifest | Missing source ownership | Escalate missing owner. |
| 3. Requirement extraction | Source manifest and meeting content | Extract candidate requirements with source IDs and status. | Requirements table updates | Assumptions may look like facts | Escalate unsupported requirements. |
| 4. Issue extraction | Meeting content | Extract open questions, blockers, ownership, impact, and next action. | Issue register | Open issues may be silently closed | Escalate closure requests. |
| 5. Decision extraction | Meeting content | Separate tentative decisions from confirmed decisions. | Decision log | Tentative statements may be treated as final | Require human decision status. |
| 6. Confirmation classification | Issues and decisions | Classify customer, vendor, internal review, or detailed-design confirmation. | Stakeholder questions | Wrong owner assignment | Escalate ambiguous owner. |
| 7. Design delta analysis | New requirements, issues, decisions | Compare against previous understanding and affected artifacts. | Delta report | Scope change hidden as wording update | Escalate material deltas. |
| 8. Artifact update proposal | Delta report and templates | Draft proposed updates and rationale. | Design update proposal | Proposal may be read as accepted design | Mark approval status clearly. |
| 9. Human approval checklist | Proposal and decision log | Record required approver role, status, residual risk, and source reference. | Approval checklist | Pending approval treated as accepted | Block cycle closure. |
| 10. Next-cycle storage | Issues, decisions, approvals, deltas | Update state records for the next review cycle. | Stored cycle state | Lost unresolved items | Carry open items forward. |

## Quality Rule

Every material claim must remain traceable to a source ID, and every pending decision must remain visibly pending until a human approval record changes its status.

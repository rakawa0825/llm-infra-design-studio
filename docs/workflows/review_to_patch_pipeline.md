# Review-to-Patch Pipeline

## Purpose

The Review-to-Patch Pipeline describes how review comments and source evidence are converted into reviewable design patches.

The pipeline does not approve network design decisions. It prepares source-backed, traceable, human-reviewable outputs that can be accepted, rejected, revised, or handed off by human reviewers.

## Inputs

Typical inputs include:

- meeting notes or transcript excerpts,
- review comments,
- vendor reference material,
- existing design document sections,
- technical reference notes,
- communication requirements,
- issue logs,
- decision logs,
- human approval notes.

Each input should be registered with source context before it is used to support a design patch.

## Processing stages

1. **Source intake:** collect evidence and assign source identifiers.
2. **Source classification:** classify source type, authority level, freshness, owner, and confidentiality.
3. **Review comment decomposition:** split comments into facts, assumptions, unresolved items, proposed changes, and handoff items.
4. **Section mapping:** map each extracted item to candidate document sections or artifact types.
5. **Evidence linking:** attach source references to each proposed artifact impact.
6. **Draft patch generation:** prepare a proposed design patch with explicit status and source references.
7. **Impact analysis:** identify communication matrix, routing, security boundary, monitoring, DR/failover, and operational impacts.
8. **review_required classification:** mark items that need human approval, more information, customer confirmation, vendor confirmation, or detailed-design handoff.
9. **Human approval:** route the patch package to the appropriate reviewer or approver role.
10. **Final design patch package:** package approved, rejected, unresolved, and handoff items for the next workflow cycle.

## Output artifacts

The pipeline can produce:

- Source Registry entries,
- Source Context Cards,
- decomposed review comment tables,
- Artifact Map entries,
- impact analysis summaries,
- design patch drafts,
- information gap requests,
- human approval checklists,
- operational handoff notes.

## Review states

Allowed review states:

- `source_backed`: the claim has a listed source reference.
- `draft`: the item is structured but not ready for approval.
- `review_required`: the item needs human review before reflection.
- `detailed_design_handoff`: the item belongs in detailed design or operational follow-up.
- `unresolved`: the item is open and must not be closed without approval.
- `rejected`: a human reviewer has rejected the proposed item.

These states do not grant production approval by themselves.

## Failure modes

The pipeline must flag or reject outputs with:

- weak grounding,
- missing source,
- conflicting source,
- over-inference,
- stale source,
- unclear ownership,
- unsupported technical assumption.

Failure modes should route to `review_required`, `needs_more_information`, `unresolved`, or `rejected` rather than becoming approved design content.

## Human approval boundary

LLM-assisted workflow steps may organize evidence, prepare patch drafts, surface conflicts, and generate review questions.

Only humans may approve:

- final design decisions,
- customer-facing wording,
- production-impacting changes,
- risk acceptance,
- unresolved issue closure,
- detailed-design handoff,
- artifact reflection into an approved baseline.

## Example output schema

```yaml
patch_id: PATCH-EXAMPLE-001
workflow: review-to-patch
review_state: review_required
source_references:
  - SRC-EXAMPLE-MEETING-001
  - SRC-EXAMPLE-BASELINE-001
target_artifact: network_domain_review_packet
target_section: communication_matrix_impact
proposed_change: "Add a proposed communication flow review item for Branch-A to Cloud-Security-Service."
evidence_summary: "Meeting evidence indicates a possible new traffic steering requirement, but inspection scope remains unresolved."
assumptions:
  - "Traffic steering may apply only to selected branch internet traffic."
unresolved_items:
  - "Inspection scope requires customer confirmation."
human_approval_required: true
do_not_reflect_yet: true
next_action: "Route to architecture reviewer and security boundary owner."
```

## Future improvements

Potential future improvements:

- richer source registry validation,
- patch package comparison across workflow cycles,
- stronger source freshness checks,
- integration with offline mock generation,
- optional LLM-assisted drafting after contract and failure-mode checks,
- exportable review packages for human approvers.

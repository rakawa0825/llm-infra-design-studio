# v0.1 Synthetic Case Design

## 1. Purpose

This synthetic case will be used to validate the v0.1 workflow from scattered infrastructure design evidence to text-based design document outputs.

The purpose is not to prove full automation. The purpose is to show that the LLM-assisted Infrastructure Design Lifecycle Framework can:

- normalize scattered evidence,
- extract requirement candidates,
- preserve unresolved items,
- generate a requirement definition draft,
- generate a high-level design document patch,
- separate detailed-design handoff items,
- produce a human approval checklist,
- preserve source traceability.

The case is intentionally public-safe and fictional. It should later be convertible into `samples/lifecycle_minimal/` without using real customer data, real project names, real transcripts, or real design excerpts.

## 2. Scenario Summary

The synthetic scenario represents customer hearing to requirement definition and high-level design patch for branch network traffic handling.

A customer is discussing how branch site traffic should be handled across normal internet-bound traffic, traffic that may require cloud security inspection, exception traffic that may bypass inspection, and unresolved details that belong in detailed design.

The project team has several scattered inputs:

- customer hearing notes that suggest intent but do not provide final approval,
- a meeting transcript excerpt with context about branch traffic handling,
- an existing design excerpt that describes a legacy traffic path but may be incomplete or stale,
- review comments asking whether exception traffic and security inspection scope are documented,
- a vendor note that explains technical behavior but does not equal customer approval.

The key ambiguity is whether branch internet-bound traffic should pass through a cloud security service, which traffic should be treated as exception traffic, and which routing or monitoring details should be handed off to detailed design.

Unresolved items must not be promoted into final design language. Meeting-derived statements and vendor-provided technical behavior must remain approval-gated until a human reviewer confirms how they should be reflected.

## 3. Input Sources

### 1. `customer_hearing_note.md`

- **Purpose:** capture customer intent from a hearing or clarification session.
- **Contains:** high-level intent for branch traffic handling, security inspection expectations, exception traffic concerns, and business context.
- **Can prove:** that a customer-facing topic was raised and may become a requirement candidate.
- **Cannot prove:** final approved requirement language, detailed routing behavior, or production-ready design.
- **Likely lifecycle phase:** Evidence Intake, Requirement Clarification.
- **Human approval before reflection:** required before hearing statements become final requirements or high-level design language.

### 2. `meeting_transcript_excerpt.md`

- **Purpose:** preserve meeting context around branch traffic, exception handling, and ownership.
- **Contains:** discussion fragments, tentative statements, questions, and follow-up items.
- **Can prove:** that a topic was discussed and what uncertainty existed at the time.
- **Cannot prove:** customer approval, final design decisions, or closure of unresolved items.
- **Likely lifecycle phase:** Evidence Intake, Evidence Normalization, Requirement Clarification.
- **Human approval before reflection:** required before transcript-derived statements become design artifact language.

### 3. `existing_design_excerpt.md`

- **Purpose:** provide baseline context for the current or previous branch traffic design.
- **Contains:** current high-level design assumptions, legacy traffic path description, and known artifact sections.
- **Can prove:** what the existing baseline says.
- **Cannot prove:** that the baseline is still correct, complete, or approved for the new requirement.
- **Likely lifecycle phase:** Evidence Normalization, High-Level Design.
- **Human approval before reflection:** required if the excerpt conflicts with newer hearing notes, review comments, or vendor notes.

### 4. `review_comments.yaml`

- **Purpose:** capture structured review comments and design gaps.
- **Contains:** reviewer questions, missing documentation points, ambiguity flags, and requested clarifications.
- **Can prove:** that a gap, question, or concern was raised during review.
- **Cannot prove:** the correct design answer or final requirement.
- **Likely lifecycle phase:** Requirement Clarification, High-Level Design, Validation.
- **Human approval before reflection:** required before a review comment becomes design language or closes a gap.

### 5. `vendor_note.md`

- **Purpose:** record generic technical behavior from a vendor-style reference note.
- **Contains:** cloud security service behavior, failover behavior, inspection boundary notes, or lifecycle considerations.
- **Can prove:** that a technical behavior was described by a vendor-style source.
- **Cannot prove:** customer design approval, project scope, or whether the behavior should be used in this design.
- **Likely lifecycle phase:** Evidence Normalization, Requirement Clarification, Detailed-Design Handoff.
- **Human approval before reflection:** required before vendor behavior becomes a design constraint or high-level design statement.

## 4. Lifecycle Coverage

### 1. Evidence Intake

- **Input:** all five synthetic input sources.
- **Transformation:** assign source identifiers and preserve source type, authority, and likely phase.
- **Output:** evidence source list for later registry creation.
- **Approval boundary:** intake does not approve any requirement or design language.

### 2. Evidence Normalization

- **Input:** hearing notes, transcript excerpt, existing design excerpt, review comments, and vendor note.
- **Transformation:** classify statements as customer intent, meeting context, baseline context, review gap, or technical behavior.
- **Output:** normalized source descriptions and authority levels.
- **Approval boundary:** normalization does not resolve conflicts or stale baseline concerns.

### 3. Requirement Clarification

- **Input:** normalized evidence and review comments.
- **Transformation:** extract requirement candidates, unresolved items, missing inputs, and confirmation needs.
- **Output:** requirement candidates, unresolved item list, and missing input list.
- **Approval boundary:** customer hearing statements may become candidates, not final requirements.

### 4. Requirement Definition

- **Input:** requirement candidates and unresolved items.
- **Transformation:** draft text-based requirement definitions with source references and maturity status.
- **Output:** `requirement_definition_draft.md`.
- **Approval boundary:** requirement draft remains reviewable until human approval.

### 5. High-Level Design

- **Input:** requirement definition draft, existing design excerpt, review comments, and vendor note.
- **Transformation:** prepare a high-level design document patch for branch traffic handling.
- **Output:** `high_level_design_patch.md`.
- **Approval boundary:** the patch must not claim final design status while inspection scope or exception traffic remains unresolved.

### 6. Detailed-Design Handoff

- **Input:** unresolved routing details, exception traffic handling, monitoring behavior, and parameter-level questions.
- **Transformation:** separate items that require detailed-design validation or later parameter decisions.
- **Output:** `detailed_design_handoff.md`.
- **Approval boundary:** detailed-design handoff items must not be written as high-level design decisions.

### 7. Validation

- **Input:** intermediate outputs and document outputs.
- **Transformation:** check source traceability, unresolved item preservation, missing input visibility, approval boundaries, and public-safe content.
- **Output:** validation notes for the synthetic case.
- **Approval boundary:** validation checks structure and discipline; it does not approve the design.

### 8. Human Approval

- **Input:** requirement definition draft, design patch, unresolved items, and handoff list.
- **Transformation:** identify human-owned decisions and approval checklist items.
- **Output:** `human_approval_checklist.md`.
- **Approval boundary:** humans approve final design language, unresolved issue closure, risk acceptance, and artifact reflection.

## 5. Expected Intermediate Outputs

Task 003 may later create these files under `samples/lifecycle_minimal/`.

### `evidence_registry.yaml`

- **Purpose:** register synthetic evidence sources and their authority.
- **Minimum fields:**
  - `source_id`
  - `source_type`
  - `title`
  - `available_at`
  - `authority_level`
  - `contains_customer_intent`
  - `contains_technical_behavior`
  - `contains_approved_decision`
  - `requires_human_review`
  - `public_safe_note`

### `requirement_candidates.yaml`

- **Purpose:** capture candidate requirements before they become approved requirements.
- **Minimum fields:**
  - `requirement_id`
  - `summary`
  - `source_ids`
  - `requirement_maturity`
  - `target_phase`
  - `approval_status`
  - `notes`

### `unresolved_items.yaml`

- **Purpose:** preserve open questions and prevent premature closure.
- **Minimum fields:**
  - `item_id`
  - `summary`
  - `source_ids`
  - `blocking_reason`
  - `owner_role`
  - `target_resolution_phase`
  - `approval_required`

### `missing_inputs.yaml`

- **Purpose:** list missing information required before design language can be finalized.
- **Minimum fields:**
  - `missing_input_id`
  - `summary`
  - `needed_for`
  - `blocking_phase`
  - `recommended_next_action`

### `design_issue_log.yaml`

- **Purpose:** track design gaps, artifact impacts, and recommended handling.
- **Minimum fields:**
  - `issue_id`
  - `summary`
  - `affected_artifact`
  - `affected_section`
  - `source_ids`
  - `classification`
  - `recommended_handling`

## 6. Expected Document Outputs

### `requirement_definition_draft.md`

- **Purpose:** draft requirement definition text from source-backed candidates.
- **Intended reader:** requirement reviewer, infrastructure architect, project control lead.
- **Should include:** requirement candidates, maturity status, source references, unresolved dependencies, and approval status.
- **Must not claim:** final customer-approved requirements while hearing-derived statements remain unapproved.
- **Traceability behavior:** every requirement statement should link to source IDs and approval status.

### `high_level_design_patch.md`

- **Purpose:** propose high-level design document changes for branch traffic handling.
- **Intended reader:** high-level design reviewer, network design lead, security reviewer.
- **Should include:** proposed branch traffic handling language, exception traffic notes, source references, unresolved items, and `review_required` markers.
- **Must not claim:** final design approval, production readiness, or detailed routing parameters.
- **Traceability behavior:** each proposed patch section should reference source IDs and unresolved dependencies.

### `detailed_design_handoff.md`

- **Purpose:** separate detailed-design items from high-level design decisions.
- **Intended reader:** detailed design owner, implementation planner, operations reviewer.
- **Should include:** exception traffic handling, routing/QoS details, monitoring behavior, parameter-level questions, and owner roles.
- **Must not claim:** that detailed-design items are resolved or approved.
- **Traceability behavior:** each handoff item should reference source IDs and target resolution phase.

### `review_response_draft.md`

- **Purpose:** prepare a response to review comments without closing unresolved items prematurely.
- **Intended reader:** reviewer, architect, project control lead.
- **Should include:** response status, related source IDs, proposed handling, unresolved items, and next actions.
- **Must not claim:** that review comments are closed unless human approval is recorded.
- **Traceability behavior:** each response should map to review comment IDs and source IDs.

### `human_approval_checklist.md`

- **Purpose:** list decisions that require human review before artifact reflection.
- **Intended reader:** approver, design governance owner, architecture reviewer.
- **Should include:** requirement approval, high-level design patch approval, unresolved item handling, detailed-design handoff approval, and artifact reflection approval.
- **Must not claim:** approval by default.
- **Traceability behavior:** each checklist item should reference affected sources, artifacts, and unresolved items.

## 7. Approval Boundary Rules

- Customer hearing statements may become requirement candidates, but not final requirements without approval.
- Meeting transcript statements may provide context, but must not become final design language by themselves.
- Vendor notes may explain technical behavior, but do not equal customer approval.
- Review comments may identify gaps, but do not automatically define the correct design.
- Existing design excerpts may provide baseline context, but may be stale.
- Unresolved items must remain unresolved until reviewed.
- Detailed-design handoff items must not be written as high-level design decisions.
- Human approval is required before uncertain or meeting-derived statements become final design language.

## 8. Example Decision Boundaries

### 1. Branch internet-bound traffic should be inspected by the cloud security service.

- **Status:** requirement candidate.
- **Reason:** customer intent exists, but approval is required before final requirement or design language.

### 2. Monitoring traffic may bypass cloud inspection.

- **Status:** detailed-design handoff.
- **Reason:** exception traffic requires parameter-level validation and operational review.

### 3. Vendor note confirms failover behavior.

- **Status:** technical behavior reference.
- **Reason:** vendor-style technical behavior does not equal customer design approval.

### 4. Existing design says all traffic follows the legacy path.

- **Status:** stale baseline candidate.
- **Reason:** the baseline may conflict with newer review comments or hearing evidence.

### 5. Review comment asks whether exception traffic is documented.

- **Status:** design gap.
- **Reason:** the comment identifies missing documentation, not the final design answer.

## 9. Public-Safety Constraints

The synthetic case must not contain:

- real customer names,
- real project names,
- real vendor names,
- real product names,
- real IP addresses,
- real hostnames,
- real site names,
- real meeting transcripts,
- private design excerpts,
- internal organization names,
- confidential diagrams.

## 10. Success Criteria

The case design is successful if:

1. the case clearly supports v0.1,
2. the case starts from scattered evidence, not a clean prompt,
3. the case leads to requirement definition and high-level design outputs,
4. the case preserves unresolved items,
5. the case includes detailed-design handoff,
6. the case includes human approval boundaries,
7. the case is public-safe,
8. the case can later be converted into `samples/lifecycle_minimal/`.

## 11. Non-Goals

This task does not create:

- full synthetic input files,
- sample output files,
- scripts,
- validators,
- production UI,
- real LLM integration,
- Word / Excel / PowerPoint outputs,
- config generation,
- network diagram generation.

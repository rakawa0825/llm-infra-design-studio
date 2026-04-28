# Source Context Card

## Purpose

A Source Context Card records how a source may be used in an LLM-assisted infrastructure design workflow.

It prevents source evidence from being treated as more authoritative than it is. It also makes explicit what the source must not be used for, which decisions require human review, and which workflow domains the source can support.

## Fields

```yaml
source_id:
title:
source_type:
owner:
authority_level:
freshness_status:
confidentiality:
related_domain:
used_for:
not_used_for:
decision_status:
human_review_required:
notes:
```

Field intent:

- `source_id`: stable identifier used by the Source Registry and Artifact Map.
- `title`: short public-safe source title.
- `source_type`: meeting note, review comment, vendor answer, baseline, official excerpt, issue log, or decision log.
- `owner`: role responsible for the source, not a real person name.
- `authority_level`: official, customer_confirmed, vendor_provided, internal_review, meeting_statement, or assumption.
- `freshness_status`: current, stale, superseded, unknown, or needs_review.
- `confidentiality`: public_safe, synthetic, internal_review_only, or do_not_send.
- `related_domain`: communication matrix, routing, security boundary, monitoring, DR/failover, governance, or operations.
- `used_for`: valid workflow uses.
- `not_used_for`: decisions or claims that must not be inferred from the source.
- `decision_status`: draft, confirmed, unresolved, review_required, detailed_design_handoff, or rejected.
- `human_review_required`: true when the source affects design decisions, risk, scope, or artifact reflection.
- `notes`: concise caveats and context.

## Example

```yaml
source_id: SRC-ATLAS-MEETING-001
title: Atlas Retail network domain review meeting excerpt
source_type: meeting_transcript_excerpt
owner: requirements_facilitation
authority_level: meeting_statement
freshness_status: current
confidentiality: synthetic
related_domain:
  - communication_matrix
  - routing_sdwan
  - security_boundary
used_for:
  - identify proposed traffic steering impact
  - create review_required questions
  - link source evidence to a draft design patch
not_used_for:
  - final approval of routing behavior
  - production configuration generation
  - closing unresolved inspection scope
decision_status: review_required
human_review_required: true
notes: "The meeting statement suggests a possible Cloud-Security-Service steering change, but inspection scope and failover behavior remain unresolved."
```

## How it is used

The Source Context Card is used during:

- source intake,
- Source Registry updates,
- review comment decomposition,
- evidence-to-decision processing,
- Artifact Map updates,
- design patch drafting,
- human approval checklist creation.

It helps determine whether a source can support a confirmed fact, an assumption, an unresolved item, a detailed-design handoff item, or a human approval point.

## Design notes

Source Context Cards should remain concise. They are not replacements for full source documents.

The card should make source authority and usage limits visible before any LLM-assisted step drafts review artifacts. If a source is stale, weakly grounded, or unclear, downstream outputs should remain `review_required` or `needs_more_information`.

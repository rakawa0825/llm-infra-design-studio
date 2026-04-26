# Source Registry Model

## Purpose

The Source Registry records evidence sources used by the workflow and preserves the metadata needed to judge source authority, freshness, ownership, and downstream impact.

## Role In The Lifecycle

The registry sits between source intake and downstream artifact generation. It helps the workflow answer:

- what sources exist
- what type each source is
- what authority each source has
- which artifacts each source may affect
- what remains unresolved
- what requires human review

## Source Type Taxonomy

- `meeting_transcript`
- `official_source_excerpt`
- `existing_design_baseline`
- `review_comment`
- `vendor_answer`
- `customer_confirmation`
- `operations_requirement`
- `communication_requirement`
- `issue_log`
- `decision_log`

## Source Status Taxonomy

- `draft`
- `active`
- `superseded`
- `unresolved`
- `confirmed`
- `needs_review`

## Source Authority Levels

- `official`
- `customer_confirmed`
- `vendor_provided`
- `internal_review`
- `meeting_statement`
- `assumption`

## Source Owner Roles

- `architecture_reviewer`
- `network_reviewer`
- `security_reviewer`
- `operations_reviewer`
- `customer_reviewer`
- `vendor_reviewer`
- `project_control`

## Freshness / Version Handling

Each source should record `source_date_or_version` and `freshness_status`. Superseded or stale sources may still be useful as historical evidence, but they must not be treated as current design approval.

## Privacy / Public-Safe Boundary

The registry must not include real customer data, real meeting transcripts, real IP addresses, private diagrams, private local paths, or private project identifiers. Synthetic samples should use fictional names only.

## Relationship To Evidence-To-Decision Loop

Evidence-to-decision workflows use the source registry to determine whether facts are source-backed, assumptions remain assumptions, and information gaps require follow-up.

## Relationship To Future RAG-Ready Workflows

The registry provides source metadata that future retrieval workflows can use to select permitted sources. This is not RAG integration. It is a public-safe source metadata layer that can later support retrieval boundaries.

## What Humans Must Approve

Humans must approve source authority changes, customer-confirmed status, artifact reflection, risk acceptance, unresolved item closure, and any production-impacting design decision.

# Evidence-to-Decision Loop

## Purpose

The Evidence-to-Decision Loop converts fragmented meeting evidence, official source excerpts, existing design baselines, and review inputs into a structured decision packet for human review.

The system does not generate final design decisions. It prepares structured evidence so that humans can decide faster and with less ambiguity.

## Why Meeting Notes Alone Are Insufficient

Meeting notes are useful evidence, but they are not enough to approve design changes. A meeting may include tentative ideas, unclear assumptions, missing vendor confirmation, or statements that conflict with the existing baseline. Those statements must be reconciled with source evidence and approval rules before design artifacts change.

## Evidence Types

| Evidence Type | Purpose |
| --- | --- |
| Meeting evidence | Captures stakeholder statements, tentative decisions, questions, and concerns. |
| Official source excerpt | Provides source-backed behavior, constraints, version, date, or applicability notes. |
| Existing design baseline | Shows the current approved or pending understanding. |
| Review input | Adds objections, gaps, risks, or handoff requirements. |
| Decision log | Records human decision state and rationale. |

## Decision Packet Concept

A design decision packet groups facts, assumptions, gaps, baseline comparison, impact analysis, proposed artifact updates, and required human decisions. It is a review package, not an approved design.

## Official Source Reconciliation

Official source reconciliation compares meeting statements with source excerpts. It marks whether each claim is aligned, partially aligned, conflicting, insufficiently evidenced, or not applicable. The official excerpt supports review; it does not replace human approval.

## Design Baseline Comparison

Baseline comparison identifies whether new evidence changes requirements, communication matrices, monitoring assumptions, unresolved issues, handoff items, or approval points.

## Information Gap Handling

Information gaps become targeted requests with owner role, affected artifact, required timing, and status. Gaps remain open until answered, deferred, or cancelled by an accountable human process.

## Human Decision States

| State | Meaning |
| --- | --- |
| draft | Packet is being prepared. |
| review_required | Human review is required before action. |
| approved | Human approver accepted the decision. |
| rejected | Human approver rejected the decision. |
| needs_more_information | More evidence is required. |
| deferred | Decision is intentionally postponed. |

## What The LLM May Do

- Structure evidence.
- Identify gaps and conflicts.
- Reconcile meeting statements with provided source excerpts.
- Compare new evidence with a baseline.
- Draft decision packets, information gap requests, and reflection requests.

## What Only Humans May Do

- Approve design decisions.
- Accept risk.
- Close unresolved items.
- Commit scope.
- Authorize customer-facing statements.
- Approve artifact reflection into design baselines.

## v0.3 Demonstration Scope

v0.3 demonstrates a synthetic evidence-to-decision loop using meeting evidence, a synthetic official source excerpt, and a synthetic existing design baseline.

## Future Expansion

Future work may add stricter schema validation, CLI execution, baseline state handling, and API-backed artifact storage. Those should preserve the same approval boundary.

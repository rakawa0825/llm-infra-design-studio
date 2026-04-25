# Contract Failure Modes

## Purpose

This document defines failure-mode tests for future LLM-assisted workflow output.

A future LLM output should be useful even when it is incomplete, but it must never silently approve design decisions.

## Why Failure-Mode Testing Is Required Before LLM Integration

LLM-assisted workflow steps can produce fluent output that looks more certain than the evidence allows. Failure-mode tests make unsafe behavior visible before any optional LLM integration is added.

## Dangerous LLM Output Patterns

- Returning `approved_by_human`.
- Omitting source references for facts or impacts.
- Promoting assumptions into confirmed facts.
- Treating unresolved items as closed.
- Marking proposed artifact updates as approved.
- Returning empty human approval points.
- Producing design updates when evidence is insufficient.

## Contract Failure vs Review-Required

A contract failure means the output violates the contract and must be rejected.

A review-required output is acceptable when it preserves uncertainty, keeps source references, and routes decisions to humans.

## Examples Of Invalid Outputs

- A result status of `approved_by_human`.
- A confirmed fact with no `source_references`.
- A proposed artifact update with `approved_for_update`.
- An unresolved item marked `closed`.
- A design impact that has no source reference.

## Human Approval Boundary

Only humans can approve design decisions, risk acceptance, artifact updates, and unresolved item closure. LLM output can request review, ask for more information, or draft a proposal, but it cannot approve the result.

## What v0.8 Demonstrates

- Negative fixtures for dangerous output patterns.
- Valid fixtures for `review_required` and `needs_more_information`.
- Validator behavior that rejects invalid output and accepts incomplete but safe output.

## What v0.8 Does Not Do

- It does not call an LLM.
- It does not generate design content.
- It does not approve artifacts.
- It does not replace human review.

# LLM Contract Layer

## Purpose

The LLM Contract Layer defines the input and output boundary for future LLM-assisted workflow execution.

The contract layer prepares the workflow for LLM-assisted execution without allowing the LLM to approve design decisions.

## Why An LLM Contract Layer Is Needed

Infrastructure design workflows contain facts, assumptions, unresolved items, tentative decisions, risk questions, and approval checkpoints. Without an explicit contract, an LLM-assisted step could over-infer missing requirements or make generated text look like an approved design update.

The contract layer fixes the shape of the input package and output package before any LLM integration is added.

## What May Be Included In An LLM Input Package

- Synthetic meeting excerpts.
- Synthetic official source excerpts.
- Existing design baseline summaries.
- Task requests for a specific workflow.
- Source IDs and source status values.
- Explicit constraints that prevent invention, approval, and silent uncertainty removal.
- Human approval policy fields.

## What Must Never Be Included

- Real customer names.
- Real person names.
- Real meeting transcripts.
- Real network diagrams.
- Real vendor answers.
- Real production IP addresses.
- Private project paths.
- Confidential design excerpts.

## Required Output Structure

The output package must separate:

- confirmed facts
- assumptions
- unresolved items
- information gaps
- design impacts
- proposed artifact updates
- human approval points
- do-not-reflect-yet items
- failure metadata

## Source Traceability Requirements

Every confirmed fact, assumption, gap, impact, and proposed update should include a source reference. Missing source evidence should produce `needs_more_information`, not a fabricated requirement.

## Uncertainty Handling

Uncertainty is a first-class output. Ambiguous statements must remain assumptions or unresolved items until a human or authoritative source resolves them.

## Human Approval Boundary

LLM-generated output may recommend review actions, draft proposed updates, and prepare decision packets. It must not approve design decisions, accept risk, close unresolved items, or mark artifact updates as final.

## Failure And Review-Required States

- `review_required` is the normal output state for design decision packets.
- `needs_more_information` is used when evidence is insufficient.
- `failed` is used when contract validation or processing fails.
- `approved_by_human` is reserved for human-controlled records and is not allowed in LLM output samples.

## Over-Inference Prevention

The input contract requires explicit constraints:

- `do_not_invent_requirements`
- `do_not_mark_as_approved`
- `preserve_uncertainty`
- `require_source_references`

These constraints keep tentative statements from becoming approved decisions and prevent assumptions from becoming confirmed facts.

## What v0.7 Demonstrates

- A JSON input package contract.
- A JSON output package contract.
- Valid templates and samples.
- A local validator that checks contract shape and approval boundaries.
- Integration with the repository validation runner.

## What v0.7 Does Not Do

- It does not call an LLM.
- It does not call external APIs.
- It does not generate final design content.
- It does not approve design decisions.
- It does not update production artifacts.

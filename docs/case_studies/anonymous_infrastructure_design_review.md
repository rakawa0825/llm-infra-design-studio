# Anonymous Case Study: Infrastructure Design Review Workflow

## Context

A large enterprise infrastructure design project had important review evidence spread across meeting notes, review comments, vendor reference material, existing design documents, transcripts, unresolved issues, and human approval decisions.

The project involved network design review, operational handoff, and design-document updates. The content in this case study is anonymized and synthetic. It does not include real customer names, private project identifiers, production diagrams, real meeting transcripts, or real IP addresses.

## Problem

The main difficulty was not a lack of information. The difficulty was that information lived in different formats and carried different levels of authority.

Some statements were confirmed requirements. Some were tentative meeting comments. Some were vendor-provided reference points. Some were unresolved review questions. Some were detailed-design handoff items that should not be finalized in a high-level design document.

Without a structured workflow, it was easy to:

- lose source context,
- promote assumptions into facts,
- close unresolved items too early,
- mix design decisions with operational notes,
- create final-looking document changes before human approval.

## Input evidence

The workflow treated each evidence item as a source, not as an automatic decision.

Example source categories:

- meeting notes and transcript excerpts,
- review comments,
- vendor reference material,
- existing design document sections,
- communication requirement tables,
- unresolved issue logs,
- human approval notes.

Each source needed context: source type, owner, authority level, freshness, related domain, intended use, and items that must not be inferred from it.

## Workflow

The review workflow followed this pattern:

```text
Fragmented project evidence
-> Source Registry
-> Source Context Card
-> Extraction
-> Impact Analysis
-> Artifact Map
-> review_required / human approval
-> Reviewable design patch
-> Operational handoff
```

The LLM/Codex-assisted steps helped structure the evidence, but did not approve the result. Outputs were kept in draft, unresolved, detailed-design handoff, or `review_required` state until a human reviewer made the decision.

## Human decisions preserved

The workflow preserved human-owned decisions instead of resolving them silently.

Examples:

- whether a technical value should be treated as proposed, confirmed, or detailed-design handoff,
- whether a communication flow should be embedded in the main document or handled as an appendix,
- whether a vendor lifecycle statement should be included as a design constraint or an operational note,
- whether ambiguous QoS or routing details should remain `review_required`,
- whether an unresolved ownership issue should block artifact reflection,
- whether a proposed design patch should be approved, rejected, or returned for more evidence.

## Outputs

The workflow produced reviewable intermediate artifacts, not final design approvals.

Example outputs:

- Source Registry entries,
- Source Context Cards,
- extracted facts, assumptions, unresolved items, and handoff items,
- Artifact Map entries,
- impact analysis by network domain,
- reviewable design patch draft,
- human approval checklist,
- operational handoff notes.

Each output kept source references and review status visible.

## Lessons learned

The strongest value was not automatic document generation. The stronger pattern was evidence discipline.

The workflow made it easier to see:

- which statements were source-backed,
- which claims were assumptions,
- which changes depended on customer or vendor confirmation,
- which design impacts crossed communication matrix, routing, security, monitoring, or DR/failover domains,
- which decisions required human approval before being reflected into artifacts.

## Reusable pattern

The case suggests a reusable enterprise AI pattern:

```text
Evidence intake
-> source context preservation
-> structured extraction
-> artifact impact mapping
-> review_required state
-> human-approved design patch
-> operational handoff
```

This pattern can apply beyond network design whenever professional workflows require traceability, uncertainty handling, and human approval.

## Why this matters for enterprise AI

Enterprise AI systems should not simply produce confident-looking answers. They should help teams manage evidence, preserve uncertainty, identify review points, and route decisions to the right human owners.

This case study demonstrates how LLM/Codex-assisted workflows can support infrastructure design review without replacing engineers or claiming production-ready automation.

# Diagram Generation Extension

## Purpose

Diagram generation is a future extension area for the LLM-assisted Infrastructure Design Lifecycle Framework.

The future goal is to support reviewable diagram candidates such as:

- logical network diagrams,
- physical network diagrams,
- design explanation diagrams,
- rollout / migration diagrams,
- operations handover diagrams.

This capability is not implemented in v0.1. It is not part of current validation. Generated diagrams must remain review artifacts until human approval is recorded.

## Core Principle

Diagram generation should be model-first, not image-first.

Bad path:

```text
prompt
-> image
-> unverified diagram
```

Preferred path:

```text
evidence
-> structured design model
-> diagram candidate
-> validation
-> human approval
-> rendering adapter
```

The source of truth should be the structured design model and its source references, not a rendered image.

## Structured Design Model

A future diagram model may include:

- site,
- device,
- interface,
- link,
- segment,
- route,
- security boundary,
- traffic flow,
- redundancy pair,
- dependency,
- unresolved item,
- approval status,
- source reference.

Each model element should preserve its source evidence, lifecycle phase, review state, and approval boundary.

## Logical Diagram Scope

Future logical diagrams may represent:

- branch / headquarters / cloud relationships,
- traffic flow,
- security inspection path,
- exception traffic path,
- routing domains,
- trust boundaries,
- failover behavior,
- unresolved design assumptions.

Logical diagrams should not imply final design approval. They should show what is confirmed, proposed, unresolved, or waiting for detailed-design handoff.

## Physical Diagram Scope

Future physical diagrams may represent:

- devices,
- circuits,
- links,
- physical locations,
- rack or site-level placement,
- port / interface relationships,
- carrier or access relationships,
- implementation dependencies.

Physical diagrams require stricter validation than logical diagrams because they can look implementation-ready. They should not be generated as final implementation diagrams without human approval.

## Output Adapters

Future rendering adapters may include:

- Mermaid,
- draw.io,
- SVG,
- PNG,
- PowerPoint,
- Markdown-embedded diagrams.

Adapters are rendering layers, not the source of truth. They should consume structured diagram candidates after source references, unresolved items, and approval states are preserved.

## Relationship to Current v0.1

v0.1 focuses on text-based artifacts:

- requirement definition draft,
- high-level design / basic design patch,
- detailed-design handoff,
- review response draft,
- human approval checklist.

Diagram generation is future work. It should depend on stable lifecycle evidence, artifact contracts, and approval boundaries before any rendering adapter is added.

## Safety and Approval Boundary

Future diagram workflows must follow these rules:

- diagrams must preserve source references,
- unresolved items must remain visible,
- diagrams must not invent devices, links, routes, or security boundaries,
- diagrams must not convert review comments into approved topology,
- diagrams must not imply production readiness,
- human approval is required before diagram reflection into official design documents.

## Non-Goals

This task does not add:

- diagram generation implementation,
- image generation,
- Mermaid generation,
- draw.io generation,
- PowerPoint rendering,
- config generation,
- production topology validation.


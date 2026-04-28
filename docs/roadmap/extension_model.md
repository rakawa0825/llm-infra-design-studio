# Extension Model

## Purpose

This document defines how the LLM-assisted Infrastructure Design Lifecycle Framework can expand after the v0.1 text-based baseline.

The extensions below are future modules. They are not required for v0.1 and should not be presented as currently implemented unless added explicitly later.

## Input adapters

Future input adapters may normalize additional evidence sources into the same lifecycle model:

- transcript adapter,
- OCR adapter,
- review spreadsheet adapter,
- vendor Q&A adapter,
- existing design document adapter.

Each adapter should preserve source identity, authority level, freshness, confidentiality, and human review requirements.

## Phase modules

Future phase modules may expand the lifecycle beyond initial requirement and design document support:

- requirement definition module,
- high-level design module,
- detailed design module,
- parameter decision module,
- test planning module,
- rollout planning module,
- operations handover module.

Each phase module should define its inputs, outputs, review states, unresolved item handling, and human approval boundary.

## Artifact adapters

Future artifact adapters may render approved or reviewable outputs into different formats:

- Markdown output,
- Word template output,
- Excel workbook output,
- PowerPoint deck output,
- company-specific templates.

Markdown remains the v0.1 priority because it is inspectable, versionable, easy to diff, and safe for early workflow validation.

Word / Excel / PowerPoint support should be treated as an adapter layer, not the core workflow.

## Technical extensions

Future technical extensions may include:

- config generation,
- network diagram generation,
- parameter sheet generation,
- test case generation,
- migration procedure generation.

These extensions require stricter validation and human approval controls because they may have direct production impact if misused.

### Future diagram generation

Diagram generation is future work and should be model-first, not image-first.

Future logical and physical diagrams should be separate artifact types derived from structured design models with source references, unresolved items, approval status, and lifecycle phase preserved. Diagram output must remain approval-gated and should not imply production readiness.

See [Diagram Generation Extension](../extensions/diagram_generation_extension.md).

## Extension rules

Any extension should preserve the same baseline rules:

- source evidence remains visible,
- assumptions remain assumptions,
- unresolved items remain unresolved,
- generated outputs remain reviewable,
- human approval is required before final design language or production-impacting artifacts are accepted,
- synthetic examples remain public-safe unless a separate private deployment policy exists.

## Not required for v0.1

The following are intentionally not required for v0.1:

- production UI,
- real LLM API integration,
- company-specific template rendering,
- network configuration generation,
- production diagram generation,
- full lifecycle automation.

The immediate priority is to make the source-to-design-document lifecycle clear, traceable, and reviewable with text-based artifacts.

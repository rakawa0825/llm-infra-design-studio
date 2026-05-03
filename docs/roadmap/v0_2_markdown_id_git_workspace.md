# v0.2 Markdown-first ID-driven Git-backed Workspace Direction

## Purpose

v0.2 will explore a Markdown-first, ID-driven, Git-backed design workspace for infrastructure design lifecycle artifacts.

The intent is to make reviewable design work persistent, traceable, and diff-friendly while preserving the public-safe, synthetic, human-reviewed boundary established in v0.1.

This document describes future direction only. It does not define implemented capability.

For a more specific public-safe traceability direction under this workspace model, see [v0.2 Traceability Direction](v0_2_traceability_direction.md).

## Positioning

v0.1 defines the lifecycle framework and the synthetic artifact flow:

- what kinds of infrastructure design artifacts are handled,
- how source evidence is preserved,
- how requirements, design patches, review items, handoff items, and approval points are separated,
- how validators can check the sample lifecycle without relying on real customer data.

v0.2 explores how engineers can work with those artifacts as a persistent design workspace.

In short:

```text
v0.1 = defines what the lifecycle handles
v0.2 = explores how the lifecycle can be operated as a workspace
```

## Core Principles

| Principle | Direction |
| --- | --- |
| Markdown-first | Keep artifacts readable, reviewable, versionable, and easy to diff before introducing richer format adapters. |
| ID-driven | Assign stable IDs to sources, requirements, design sections, review items, patch drafts, decisions, handoff items, and validation results. |
| Git-backed | Treat Git history, branches, diffs, and review comments as the default collaboration substrate. |
| Artifact-first | Prioritize explicit intermediate artifacts over hidden state or opaque automation. |
| Human-in-the-loop | Preserve approval gates for customer-facing language, production impact, risk acceptance, and scope commitments. |
| Adapter-later | Add Word, Excel, PowerPoint, diagram, and system adapters only after the core workspace contract is stable. |

## Cursor-like Analogy

Cursor embeds AI into the coding workflow. This direction explores how similar workflow principles can be applied to infrastructure design artifacts.

The project should not be described only as "Cursor for infrastructure." The stronger positioning remains:

```text
LLM-assisted Infrastructure Design Lifecycle Framework
```

v0.2 adds a workspace direction under that framework rather than replacing the current repository subject.

## ID Model Preview

Candidate ID prefixes:

| Prefix | Meaning |
| --- | --- |
| `SRC` | Source evidence or source manifest entry |
| `REQ` | Requirement or requirement candidate |
| `DS` | Design section or design section fragment |
| `RV` | Review item |
| `PD` | Patch draft |
| `DR` | Diff review |
| `DL` | Decision log entry |
| `HO` | Detailed-design handoff item |
| `VR` | Validation result |

The goal is traceability across source, requirement, design section, review item, patch draft, diff review, decision log, handoff, and validation result.

A future trace chain may look like:

```text
SRC -> REQ -> DS -> RV -> PD -> DR -> DL -> HO -> VR
```

The ID model must not turn assumptions into confirmed facts. Each artifact should preserve whether a statement is confirmed, assumed, unresolved, or waiting for human approval.

## Future Workspace Shape

The following structure is a proposed future shape. It is not implemented in the current repository.

```text
workspace/
  00_sources/
  10_requirements/
  20_design/
  30_review/
  40_handoff/
  50_validation/
```

This structure is intended to separate evidence, requirements, design content, review work, detailed-design handoff, and validation artifacts while keeping all files reviewable in Git.

## Future Runner Direction

Future deterministic runner concepts may include:

- classify review items,
- build patch draft,
- build diff review,
- build decision log,
- validate workspace.

The immediate direction is to define workflow contracts with deterministic sample inputs and outputs. LLM integration is not part of the immediate step.

Any future runner should preserve:

- source traceability,
- unresolved issue visibility,
- human approval points,
- public-safe sample data,
- clear separation between proposed changes and accepted design language.

## Non-goals

The v0.2 direction does not currently include:

- UI-first development,
- Excel / Word / PowerPoint adapters,
- diagram rendering,
- config generation,
- autonomous design approval,
- direct modification of final design documents.

These may become future extensions only after the Markdown-first workspace contract, ID taxonomy, and validation model are stable.

## Human Approval Points

The following decisions remain human-owned:

- whether v0.2 should become the next public release target,
- whether a workspace structure should be added to the repository,
- whether ID prefixes should be finalized,
- whether runner behavior should be introduced,
- whether any generated patch should become final design language,
- whether adapters should be added for private or company-specific formats.

## Open Risks

| Risk | Handling Direction |
| --- | --- |
| Repository subject becomes unclear after public release | Keep v0.1 public positioning intact and introduce v0.2 as future direction only. |
| Workspace folders imply implemented capability | Mark proposed structures as not implemented until samples and validators exist. |
| IDs become decorative instead of traceable | Define an explicit source-to-validation trace chain before adding runners. |
| Automation appears to approve design changes | Keep human approval gates visible in every workflow artifact. |

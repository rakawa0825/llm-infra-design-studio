# LLM Infra Design Studio

LLM Infra Design Studio is an experimental workflow template for LLM-assisted infrastructure design.

It helps teams transform fragmented infrastructure design information - meeting notes, existing design documents, communication requirements, review comments, vendor answers, and unresolved issues - into structured, reviewable, reusable, and human-approved engineering artifacts.

This is not an automatic network design system.

## Quick Start

This repository is a Markdown-first workflow prototype with lightweight CLI validation and scaffold generation. Review the documents, samples, templates, and workflow files directly, then run the checks:

```bash
python3 scripts/check_sensitive_identifiers.py
python3 scripts/validate_output_schema.py
python3 scripts/check_unresolved_assertions.py
python3 scripts/compare_expected_outputs.py
python3 scripts/validate_llm_contracts.py
python3 scripts/validate_llm_contracts.py --include-negative
python3 scripts/run_sample_workflow.py --write-report
python3 scripts/generate_workflow_scaffold.py --list-workflows
python3 scripts/generate_workflow_scaffold.py --scenario-id scenario_003 --workflow evidence-to-decision --output-dir generated/scenario_003 --force
python3 scripts/run_sample_workflow.py --check-only
```

Passing validation means the sample artifacts, generated scaffolds, and LLM contract samples meet the current local checks. It does not mean the repository is approved for publication or production use.

## Problem

Enterprise infrastructure design work often depends on scattered inputs, repeated review cycles, and decisions that must remain traceable over time. This repository provides a Markdown-first structure for organizing those inputs and producing artifacts that engineers can review, challenge, approve, and reuse.

## Intended Users

- Enterprise network engineers.
- Infrastructure architects.
- Technical success and deployment teams.
- SI and infrastructure design teams.
- Reviewers who need structured design evidence.

The repository supports review structure, workflow discipline, source traceability, and reusable artifact formats. It does not make automatic design decisions.

## What This Is

- A public-safe workflow template for LLM-assisted infrastructure design.
- A synthetic sample project using fictional enterprise connectivity data.
- A starting point for source manifests, requirement tables, review notes, delta reports, and approval checklists.
- A human-in-the-loop operating model for design support.

## What This Is Not

- Not an automatic network design system.
- Not a source of production-ready architecture decisions.
- Not a replacement for qualified engineers.
- Not a repository for real customer data, private diagrams, meeting transcripts, or project files.

## Lifecycle Overview

The core loop is:

Source Intake -> Source Manifest -> Normalization -> Requirement Extraction -> Design Logic Review -> Verification -> Delta Impact Analysis -> Artifact Update -> Human Approval -> Decision Storage -> Reuse in Next Cycle

## v0.2 Direction: Meeting-to-Design Workflow

The next workflow slice treats meeting intake as the entry point, not the final product. A design meeting or hearing should lead to requirement extraction, issue and decision management, design delta analysis, artifact update proposals, and human approval checkpoints.

The goal is to show how enterprise design review moves from conversation to traceable design artifacts while preserving unresolved items and approval boundaries.

## v0.3 Direction: Evidence-to-Decision Loop

The next loop combines meeting evidence, official source excerpts, and an existing design baseline into a decision packet for human review. It generates information gap requests and design reflection requests, but does not automatically approve or update design documents.

The goal is to prepare source-backed decisions while keeping missing information, baseline impact, and human approval visible.

## v0.4 Direction: CLI Validation Runner

v0.4 adds a lightweight CLI runner that validates repository structure, samples, evals, validation scripts, and public-safety checks. It does not generate final design decisions; it prepares the project for future CLI, API, and SaaS evolution by making the workflow assets reproducible.

## v0.5 Direction: Multiple Synthetic Scenarios

v0.5 adds a second synthetic scenario focused on data center resilience, operations monitoring, DR failover alerting, and communication matrix impact. This helps show that the workflow is not tied to a single ExampleCorp branch-connectivity sample.

## v0.6 Direction: Minimal Workflow Scaffold Generator

v0.6 adds a minimal scaffold generator that creates empty workflow artifact sets for `meeting-to-design` and `evidence-to-decision`. It does not call an LLM, generate approved design decisions, or update production artifacts. It prepares the project for future workflow generation, API layers, and SaaS execution while keeping human approval visible.

## v0.7 Direction: LLM-Ready Contract Layer

v0.7 defines input and output contracts for future LLM-assisted workflow steps. It does not call an LLM, and it prevents LLM output from becoming approved design decisions. The contract preserves uncertainty, source traceability, and human approval boundaries while preparing the project for future offline mock generation or optional LLM integration.

## v0.8 Direction: Contract Failure and Review-Required Cases

v0.8 adds failure-mode fixtures that test invalid LLM outputs before real LLM integration. It distinguishes failed, `review_required`, and `needs_more_information` states, and verifies that LLM outputs cannot approve design decisions. This prepares the project for safer future mock generation or optional LLM integration.

## v0.9 Direction: Network Design Domain Pack

v0.9 adds network-specific review domains: communication matrix, routing / SD-WAN impact, security / SSE boundary, monitoring / logging, and DR / failover. The domain pack identifies network design impact areas but does not approve design decisions.

## Repository Structure

- `agents/`: Agent role definitions for lifecycle support.
- `skills/`: Markdown-first skill definitions.
- `workflows/`: Step-by-step process files.
- `templates/`: Reusable public-safe artifact templates.
- `schemas/`: JSON contract documentation for future LLM-assisted workflow packages.
- `samples/`: Synthetic input and output examples.
- `evals/`: Small evaluation cases and expected outputs.
- `generated/`: Committed example workflow scaffolds.
- `scripts/`: Minimal validation and safety-check scripts.
- `state/`: Lightweight project state logs for decisions, issues, deltas, and approvals.
- `docs/`: Public-facing summary and talk-track documents.

## Public Sample Policy

All examples in this repository are synthetic. Use fictional names such as ExampleCorp, Branch-A, Branch-B, Primary-DC, DR-DC, and Cloud-Security-Service. Use RFC documentation IP ranges only: `192.0.2.0/24`, `198.51.100.0/24`, and `203.0.113.0/24`.

## Human-In-The-Loop Principle

LLMs may structure information, surface contradictions, propose review questions, and draft artifacts. Humans must approve design decisions, scope commitments, customer-facing statements, risk acceptance, unresolved issue closure, detailed design handoff, and production-impacting decisions.

## Known Limitations of v0.1

- Validation scripts are minimal and intentionally easy to inspect.
- Samples are synthetic and do not represent a production network.
- There is no production network integration.
- There is no SaaS UI yet.
- There is no automatic design decisioning.
- Human approval remains required for design decisions, scope commitments, risk acceptance, handoff, publication, and production-impacting actions.

## Current Status

`v0.9 Network design domain pack`

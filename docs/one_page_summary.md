# One Page Summary

LLM Infra Design Studio is a Markdown-first workflow template for LLM-assisted infrastructure design. It demonstrates how an LLM-supported workflow can turn fragmented design inputs into traceable artifacts that engineers can review, challenge, approve, and reuse.

The repository is built around a fully synthetic ExampleCorp scenario for branch connectivity migration to SD-WAN and cloud security. The sample content shows how meeting notes, design excerpts, review comments, vendor answers, and communication requirements can become source manifests, requirements tables, delta reports, unresolved issue lists, and human approval checklists.

## What It Shows

- Markdown-first workflow design for LLM-assisted engineering work.
- Source traceability from extracted facts back to sample inputs.
- Explicit separation of confirmed facts, assumptions, unresolved issues, and detailed-design handoff items.
- Human governance for scope commitments, risk acceptance, customer-facing language, and production-impacting decisions.
- Lightweight validation scripts for sample safety, output structure, unresolved assertions, and expected behavior.

## Why It Matters

Infrastructure design work often has enough ambiguity that an LLM should not be asked to decide architecture automatically. This project instead treats the LLM as a workflow assistant: it structures evidence, surfaces contradictions, drafts review artifacts, and keeps approval points visible.

## Relevant Roles

| Role | Relevance |
| --- | --- |
| AI Deployment Engineer | Shows how to wrap LLM output with validation, governance, and reviewable artifacts. |
| AI Success Engineer | Demonstrates a customer-facing workflow pattern that keeps uncertainty and human approval visible. |
| Codex / workflow-oriented technical roles | Shows how agents, skills, templates, samples, evals, and scripts can form a small but coherent engineering workflow product. |
| Infrastructure architect | Provides a reusable structure for source-backed requirement extraction and design review. |

## Boundary

This project does not automate network design. It does not contain production configuration, real customer data, or production network integration. It is a public-safe v0.1 prototype for making design evidence easier to inspect and reuse.

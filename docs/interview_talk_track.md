# Interview Talk Track

## Project Summary

LLM Infra Design Studio is a public-safe, Markdown-first prototype for using LLMs in infrastructure design workflows. It is designed around a synthetic enterprise connectivity scenario and shows how fragmented inputs can be converted into traceable, reviewable artifacts.

## 30-Second Version

The project is not an automatic network design tool. It is a workflow product: it helps structure design evidence, preserve source traceability, separate facts from assumptions, and keep human approval gates visible. The value is making LLM-assisted engineering work safer, more auditable, and easier to review.

## Three-Minute Version

Enterprise infrastructure design often starts with scattered meeting notes, review comments, old design excerpts, communication matrices, and vendor answers. If an LLM turns that directly into a final design, the workflow becomes risky because missing evidence and unresolved assumptions can disappear.

This repository takes a different approach. It defines a lifecycle from source intake to source manifest, normalization, requirement extraction, design logic review, verification, delta impact analysis, artifact update, and human approval. Every material claim should remain traceable to a source ID. Unresolved issues remain unresolved until a human decision is recorded.

The sample scenario is intentionally synthetic. It uses fictional branches, data centers, and cloud security components with documentation-only address ranges. That makes the repository safe to inspect while still showing the shape of a real deployment workflow.

## What I Would Emphasize In An Interview

- I focused on workflow safety rather than flashy generation.
- I treated uncertainty as an output, not a problem to hide.
- I separated LLM assistance from human-owned decisions.
- I added validation scripts so the repo has an executable quality posture, even in v0.1.
- I structured the project with agents, skills, workflows, templates, samples, evals, and reports so it can be reviewed as an engineering system.

## Role Alignment

| Role | Talking Point |
| --- | --- |
| AI Deployment Engineer | The repo shows how to deploy LLM-assisted workflows with safety checks, source traceability, and clear review gates. |
| AI Success Engineer | The repo demonstrates how to make customer-facing AI workflow value explainable without overclaiming automation. |
| Codex / workflow-oriented technical roles | The repo shows how to turn an ambiguous professional workflow into structured files, repeatable checks, and incremental commits. |

## Differentiator

The workflow treats uncertainty as a first-class output: facts, assumptions, unresolved issues, vendor confirmations, customer confirmations, and detailed-design handoff items are separated. Human approval remains required for design decisions, risk acceptance, publication, and production-impacting actions.

## What I Would Not Claim

- I would not claim it produces production-ready network designs.
- I would not claim the validation scripts are comprehensive.
- I would not claim the sample is based on a real customer.
- I would not claim the workflow replaces qualified engineers.

# LLM Infra Design Studio

LLM Infra Design Studio is an experimental workflow template for LLM-assisted infrastructure design.

It helps teams transform fragmented infrastructure design information - meeting notes, existing design documents, communication requirements, review comments, vendor answers, and unresolved issues - into structured, reviewable, reusable, and human-approved engineering artifacts.

This is not an automatic network design system.

## Problem

Enterprise infrastructure design work often depends on scattered inputs, repeated review cycles, and decisions that must remain traceable over time. This repository provides a Markdown-first structure for organizing those inputs and producing artifacts that engineers can review, challenge, approve, and reuse.

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

## Repository Structure

- `agents/`: Agent role definitions for lifecycle support.
- `skills/`: Markdown-first skill definitions.
- `workflows/`: Step-by-step process files.
- `templates/`: Reusable public-safe artifact templates.
- `samples/`: Synthetic input and output examples.
- `evals/`: Small evaluation cases and expected outputs.
- `scripts/`: Minimal validation and safety-check scripts.
- `state/`: Lightweight project state logs for decisions, issues, deltas, and approvals.
- `docs/`: Public-facing summary and talk-track documents.

## Public Sample Policy

All examples in this repository are synthetic. Use fictional names such as ExampleCorp, Branch-A, Branch-B, Primary-DC, DR-DC, and Cloud-Security-Service. Use RFC documentation IP ranges only: `192.0.2.0/24`, `198.51.100.0/24`, and `203.0.113.0/24`.

## Human-In-The-Loop Principle

LLMs may structure information, surface contradictions, propose review questions, and draft artifacts. Humans must approve design decisions, scope commitments, customer-facing statements, risk acceptance, unresolved issue closure, detailed design handoff, and production-impacting decisions.

## Current Status

`v0.1 Markdown-first prototype`

# LLM Infra Design Studio

LLM Infra Design Studio is a Markdown-first workflow prototype for LLM-assisted infrastructure and network design review.

It helps turn fragmented design evidence - meeting notes, existing design baselines, requirements, review comments, vendor-style answers, and unresolved issues - into structured review artifacts with source traceability and human approval boundaries.

This is not an automatic network design system.

## 30-Second Overview

- **Purpose:** support infrastructure design review, not replace engineers.
- **Core workflow:** source evidence -> requirement and issue extraction -> design impact analysis -> review artifacts -> human approval.
- **Network domains:** communication matrix, routing / SD-WAN, security / SSE boundary, monitoring / logging, and DR / failover.
- **Safety boundary:** assumptions and unresolved items remain visible; LLM-ready outputs cannot approve design decisions.

## Quick Start

Run the main validation command:

```bash
python3 scripts/run_sample_workflow.py --check-only
```

For contract failure and review-required cases:

```bash
python3 scripts/validate_llm_contracts.py --include-negative
```

Passing validation means the synthetic samples, generated scaffolds, LLM contract samples, and failure fixtures meet the current local checks. It does not mean the repository is approved for publication or production use.

## Reviewer Entry Points

- [Private Preview Guide](docs/private_preview_guide.md)
- [Scenario Index](docs/scenario_index.md)
- [Network Design Domain Model](docs/network_design_domain_model.md)
- [Scenario 003 Network Domain Review Packet](samples/output/scenario_003_network_domain_review_packet.md)
- [CLI Validation Runner](scripts/run_sample_workflow.py)

## What This Is

- A public-safe workflow prototype for LLM-assisted infrastructure design review.
- A reusable Markdown structure for agents, skills, workflows, templates, samples, evals, and validation scripts.
- A synthetic demonstration of source-backed network-domain review artifacts.
- A human-in-the-loop operating model for preserving uncertainty and approval boundaries.

## What This Is Not

- Not an automatic network design system.
- Not a source of production-ready architecture decisions.
- Not a replacement for qualified engineers.
- Not a repository for real customer data, private diagrams, meeting transcripts, or project files.
- Not an LLM API integration, SaaS application, or production automation layer.

## Core Workflow

```text
Source Intake
-> Source Manifest
-> Requirement / Issue / Decision Extraction
-> Evidence-To-Decision Review
-> Network Domain Review
-> Artifact Update Proposal
-> Human Approval
-> Decision Storage
```

## Network Domains

v0.9 adds a network design domain pack covering:

- Communication Matrix
- Routing / SD-WAN Impact
- Security / SSE Boundary
- Monitoring / Logging Requirement
- DR / Failover Review

The domain pack identifies network design impact areas. It does not approve or finalize network design decisions.

## Human Governance

LLMs may structure information, surface contradictions, propose review questions, and draft review artifacts. Humans must approve design decisions, scope commitments, customer-facing statements, risk acceptance, unresolved issue closure, detailed design handoff, publication, and production-impacting actions.

## Public-Safe Sample Policy

All examples are synthetic. Fictional names include ExampleCorp, Northstar Manufacturing, Atlas Retail, Branch-A, Branch-B, Primary-DC, DR-DC, Cloud-Security-Service, and Monitoring-System. Use RFC documentation IP ranges only when IP examples are needed: `192.0.2.0/24`, `198.51.100.0/24`, and `203.0.113.0/24`.

## Repository Structure

- `agents/`: Agent role definitions for lifecycle support.
- `skills/`: Markdown-first skill definitions.
- `workflows/`: Step-by-step process files.
- `templates/`: Reusable public-safe artifact templates.
- `schemas/`: JSON contract documentation for future LLM-assisted workflow packages.
- `samples/`: Synthetic input and output examples.
- `evals/`: Evaluation cases, expected outputs, and failure fixtures.
- `generated/`: Committed example workflow scaffolds.
- `scripts/`: Minimal validation and safety-check scripts.
- `docs/`: Reviewer guides, domain models, summaries, and talk-track documents.
- `reports/`: Review and validation reports.

## Current Status

v1.0 private preview. Next planned work is tracked through local issue drafts and focuses on Source Registry and Artifact Map before any LLM API integration.

See [ROADMAP.md](ROADMAP.md) for version history and planned next steps.

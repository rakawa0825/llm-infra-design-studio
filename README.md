# LLM Infra Design Studio

LLM Infra Design Studio is a Markdown-first prototype for turning fragmented infrastructure project evidence into reviewable, traceable, human-approved design artifacts across the infrastructure design lifecycle.

It helps engineers turn fragmented infrastructure project evidence into source-backed, reviewable, traceable, and human-approved design decisions. The repository is public-safe and uses synthetic examples only.

## What this is

- A workflow prototype for infrastructure design review.
- A structured repository of agents, skills, workflows, templates, samples, evals, and validation scripts.
- A source-backed review model for turning project evidence into reviewable design patches.
- A human-in-the-loop design support system that preserves uncertainty, review states, and operational handoff points.

## What this is not

- Not an autonomous infrastructure design system.
- Not a production-ready network design tool.
- Not a replacement for qualified engineers.
- Not a repository for real customer data, private diagrams, meeting transcripts, or project files.
- Not an LLM API integration, SaaS application, or production automation layer.

## Why this exists

Enterprise infrastructure design work is often scattered across meeting notes, review comments, vendor answers, existing design documents, technical references, unresolved issues, and human approval decisions.

This project models how LLM/Codex-assisted workflows can organize that evidence into reviewable artifacts without hiding uncertainty or bypassing human judgment.

## Core focus

This repository explores an LLM-assisted Infrastructure Design Lifecycle Framework.

The goal is to turn scattered customer hearing notes, meeting transcripts, review comments, existing design documents, and vendor answers into text-based, reviewable, traceable, human-approved design artifacts such as requirement definitions, high-level design document patches, detailed-design handoffs, unresolved item lists, and approval checklists.

This is not primarily a proposal-generation system. Proposal and presentation generation may be added later as optional adapters.

Review-to-Patch is one downstream workflow inside the broader lifecycle framework.

## Core workflow

```text
Fragmented project evidence
-> Source Registry
-> Extraction
-> Impact Analysis
-> Artifact Map
-> review_required / human approval
-> Reviewable design patch
-> Operational handoff
```

The workflow prepares design-review outputs. It does not approve final design decisions.

## Key concepts

- **Source Registry:** records evidence sources, source type, authority, freshness, owner role, privacy boundary, and related artifacts.
- **Artifact Map:** records which design artifacts may be impacted by each source and what updates remain proposed, unresolved, or approval-gated.
- **Source Context Card:** summarizes how one source may and may not be used in a workflow step.
- **review_required:** the normal state for outputs that need human inspection before design reflection.
- **Human Approval Boundary:** the line between AI-assisted structuring and human-owned decisions.
- **Design Patch:** a proposed, source-linked change package for review, not an approved production update.
- **Operational Handoff:** the transfer of review outcomes, assumptions, and unresolved items to operations or detailed design owners.
- **Detailed Design Handoff:** items intentionally moved out of high-level review because they require lower-level engineering validation.

## Example use case

A large enterprise infrastructure design review has meeting notes, review comments, vendor reference material, existing design baselines, and unresolved routing or monitoring questions spread across multiple sources.

The workflow can:

- classify sources and preserve context,
- extract facts, assumptions, unresolved items, and handoff items,
- map source evidence to affected design artifacts,
- identify communication matrix, routing, security boundary, monitoring, and DR/failover impacts,
- prepare a reviewable design patch,
- keep ambiguous items in `review_required` state until a human approves or rejects them.

See [Review-to-Patch Minimal Example](samples/review_to_patch_minimal/README.md) for a small synthetic dataset that follows this path end to end.

## Human approval boundary

LLMs may structure information, surface contradictions, draft review questions, and prepare review artifacts.

Humans must approve:

- production-impacting design decisions,
- scope commitments,
- risk acceptance,
- customer-facing language,
- unresolved issue closure,
- detailed design handoff,
- artifact reflection,
- publication or external sharing.

## Repository structure

- `agents/`: agent role definitions for lifecycle support.
- `skills/`: Markdown-first skill definitions.
- `workflows/`: process specifications.
- `templates/`: reusable artifact templates.
- `templates/codex_instructions/`: reusable Codex instruction templates.
- `schemas/`: JSON contract documentation for future LLM-assisted workflow packages.
- `samples/`: synthetic input and output examples.
- `evals/`: evaluation cases, expected outputs, and failure fixtures.
- `generated/`: committed example workflow scaffolds.
- `scripts/`: validation and safety-check scripts.
- `docs/`: reviewer guides, domain models, workflow specs, and career-safe summaries.
- `reports/`: review and validation reports.

## Current status

- Functional scope: `v0.1 Lifecycle Prototype`
- Repository release status: `Public Release Candidate`
- Suggested release label: `v0.1.0-rc.1`
- Production readiness: No
- Real customer data: No
- OSS/license status: pending license decision

The repository is in public-safe prototype shape using synthetic examples only.

Current capabilities include:

- meeting-to-design workflow modeling,
- evidence-to-decision review,
- network design domain review,
- Source Registry and Artifact Map modeling,
- LLM input/output contract validation,
- contract failure and review-required fixtures,
- one-command local validation.

Run the main validation command:

```bash
python3 scripts/run_sample_workflow.py --check-only
```

See [CLI Validation Runner](docs/cli_validation_runner.md) for what the checks verify and what they do not prove.

## First-time reviewer path

Start here:

1. Framework overview: [docs/architecture/infrastructure_design_lifecycle_framework.md](docs/architecture/infrastructure_design_lifecycle_framework.md)
2. v0.1 scope: [docs/roadmap/v0_1_scope.md](docs/roadmap/v0_1_scope.md)
3. Synthetic case design: [docs/cases/v0_1_synthetic_case_design.md](docs/cases/v0_1_synthetic_case_design.md)
4. Lifecycle minimal sample: [samples/lifecycle_minimal/README.md](samples/lifecycle_minimal/README.md)
5. Reviewer quickstart: [docs/quickstart_for_reviewers.md](docs/quickstart_for_reviewers.md)
6. Known limitations: [docs/known_limitations.md](docs/known_limitations.md)

## Validation

```bash
python3 scripts/run_sample_workflow.py --check-only
python3 scripts/validate_lifecycle_minimal.py
python3 scripts/validate_artifact_generation_plan.py
python3 scripts/check_sensitive_identifiers.py
```

Validation checks sample consistency, artifact generation plan consistency, approval-boundary discipline, and public-safe content. It does not prove real network design correctness or approve design language.

For contract failure and review-required cases:

```bash
python3 scripts/validate_llm_contracts.py --include-negative
```

Passing validation means the synthetic samples, generated scaffolds, contract samples, and failure fixtures meet the current local checks. It does not mean the repository is approved for production use.

## License status

No open-source license has been selected yet.

This repository is intended for public portfolio visibility and review. Reuse, redistribution, or derivative works are not granted until a license is added.

See [License Policy](docs/release/license_policy.md).

## Roadmap

Near-term work:

- finalize public release readiness,
- expand customer hearing to requirement definition examples,
- strengthen requirement-to-basic-design document generation,
- add replay-style validation patterns for time-sliced project evidence,
- improve lifecycle-oriented reviewer documentation.

Not now:

- real LLM API integration,
- FastAPI or SaaS UI,
- production network design automation,
- real customer data,
- vendor-specific configuration generation,
- Word / Excel / PowerPoint rendering,
- diagram generation.

## Positioning

I am not trying to replace engineers with AI.

I am building workflow structures that help engineers turn fragmented infrastructure information into reviewable, traceable, and human-approved decisions.

Start here:

- [Docs Index](docs/INDEX.md)
- [Infrastructure Design Lifecycle Framework](docs/architecture/infrastructure_design_lifecycle_framework.md)
- [v0.1 Scope](docs/roadmap/v0_1_scope.md)
- [Extension Model](docs/roadmap/extension_model.md)
- [Private Preview Guide](docs/private_preview_guide.md)
- [Scenario Index](docs/scenario_index.md)
- [Review-to-Patch Minimal Example](samples/review_to_patch_minimal/README.md)
- [Network Design Domain Model](docs/network_design_domain_model.md)
- [Review-to-Patch Pipeline](docs/workflows/review_to_patch_pipeline.md)

Supporting workflow:

- [YouTube Transcript to Study Artifact Workflow](docs/workflows/youtube_transcript_to_study_artifact.md)

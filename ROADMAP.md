# Roadmap

## v0.1 Markdown-First Prototype

- Define public-safe repository structure.
- Create synthetic ExampleCorp scenario.
- Provide templates for source, requirement, delta, and approval artifacts.
- Add minimal runnable validation scripts.

## v0.2 Meeting-To-Design Workflow Slice

- Add operating model and meeting-to-design workflow.
- Add PM/PL-style project control, requirements facilitation, and issue / decision separation.
- Add synthetic design review meeting and matching outputs.

## v0.3 Evidence-To-Decision Loop

- Add source-backed evidence reconciliation.
- Add official source comparison, baseline comparison, decision packet, information gap request, and design reflection request.
- Preserve human approval boundaries before artifact reflection.

## v0.4 CLI Validation Runner

- Add `scripts/run_sample_workflow.py`.
- Validate repository structure, samples, evals, validation scripts, and public-safety checks in one command.

## v0.5 Multiple Synthetic Scenarios

- Add Northstar Manufacturing as a second synthetic scenario.
- Demonstrate operations monitoring, DR failover alerting, and communication matrix impact.

## v0.6 Minimal Workflow Scaffold Generator

- Add `scripts/generate_workflow_scaffold.py`.
- Generate placeholder artifact sets for `meeting-to-design` and `evidence-to-decision`.

## v0.7 LLM-Ready Contract Layer

- Define JSON input and output contracts for future LLM-assisted workflow steps.
- Add contract validator and sample input/output packages.

## v0.8 Contract Failure And Review-Required Cases

- Add valid review-required and needs-more-information fixtures.
- Add invalid fixtures for generated approval, missing sources, empty approval points, assumption promotion, approved update language, and unresolved item closure.

## v0.9 Network Design Domain Pack

- Add concrete network review domains:
  - Communication Matrix
  - Routing / SD-WAN Impact
  - Security / SSE Boundary
  - Monitoring / Logging Requirement
  - DR / Failover Review
- Add Atlas Retail scenario and network-domain review outputs.

## v1.0 Private Preview

- Shorten README for external reviewers.
- Add private preview guide.
- Add scenario index.
- Keep validation commands stable.
- Do not add API, FastAPI, SaaS UI, or LLM integration.

## Future Public Template

- Publish stable documentation.
- Add contribution guidelines.
- Provide multiple synthetic infrastructure scenarios.
- Decide license before public release.

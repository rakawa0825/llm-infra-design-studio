# Private Preview Guide

## 30-Second Overview

LLM Infra Design Studio is a Markdown-first prototype for LLM-assisted infrastructure and network design review. It turns fragmented evidence into review artifacts while preserving source traceability, uncertainty, and human approval boundaries.

It does not automatically design networks.

## 3-Minute Inspection Path

1. Read [README.md](../README.md) for the project boundary and quick start.
2. Read [Network Design Domain Model](network_design_domain_model.md) for the v0.9 domain-specific center.
3. Inspect [Scenario 003 Network Domain Review Packet](../samples/output/scenario_003_network_domain_review_packet.md).
4. Open [Scenario Index](scenario_index.md) to see the progression from generic workflow samples to network-domain review.
5. Run the validation command.

## One-Command Validation

```bash
python3 scripts/run_sample_workflow.py --check-only
```

For LLM contract failure and review-required cases:

```bash
python3 scripts/validate_llm_contracts.py --include-negative
```

## Recommended Files To Inspect

- `README.md`
- `docs/network_design_domain_model.md`
- `docs/llm_contract_layer.md`
- `docs/contract_failure_modes.md`
- `docs/scenario_index.md`
- `samples/output/scenario_003_network_domain_review_packet.md`
- `scripts/run_sample_workflow.py`

## What Not To Infer

- Do not infer that the repository generates final network designs.
- Do not infer that any sample output is approved for production use.
- Do not infer that the project contains real customer data.
- Do not infer that an LLM is currently called.
- Do not infer that API, SaaS UI, or production automation exists.

## Public-Safe Boundary

All samples are synthetic. Fictional names, generic components, and documentation IP ranges are used where needed. Real customer names, real meeting transcripts, real network diagrams, real vendor answers, real IP addresses, and private design excerpts are out of scope.

## Current Limitations

- Validation is intentionally lightweight.
- Scenarios are synthetic and limited.
- Domain reviews stop at review artifacts.
- No production network integration exists.
- No LLM API integration exists.
- Human approval remains required for design decisions and artifact reflection.

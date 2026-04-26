# Add Source Registry And Artifact Map

## Summary

Define how source evidence maps to downstream review artifacts and proposed artifact updates.

## Why This Matters

The project needs an explicit source-to-artifact relationship before future RAG-ready, MCP-ready, or LLM-assisted workflow execution. This is the likely v1.1 implementation issue.

## Scope

- Source registry model.
- Artifact map model.
- Source type taxonomy.
- Source owner role.
- Source status.
- Artifact impact.
- Traceability from source to artifact update.

## Out of Scope

- RAG implementation.
- LLM API integration.
- Production artifact updates.
- Real customer data.

## Acceptance Criteria

- A source registry template exists.
- An artifact map template exists.
- A sample source registry and artifact map exist.
- A validation check confirms required fields.
- Human approval boundaries remain explicit.

## Validation

```bash
python3 scripts/run_sample_workflow.py --check-only
python3 scripts/validate_output_schema.py
```

## Labels

v1.1, traceability, source-registry, artifact-map

## Priority

High

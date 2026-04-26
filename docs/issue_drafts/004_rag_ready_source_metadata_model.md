# Define RAG-Ready Source Metadata Model

## Summary

Prepare a source metadata model for future retrieval-augmented workflows without implementing retrieval.

## Why This Matters

Future retrieval or MCP workflows need clear metadata and privacy boundaries before any source content is sent to a model or retrieval layer.

## Scope

- Source metadata.
- Source version.
- Source date.
- Source authority.
- Source classification.
- Retrieval boundary.
- Privacy boundary.
- Do-not-send fields.

## Out of Scope

- RAG implementation.
- Vector database.
- Embeddings.
- LLM API calls.
- Real project data.

## Acceptance Criteria

- RAG-ready metadata model exists.
- Do-not-send fields are explicit.
- Retrieval boundary and privacy boundary are defined.
- Synthetic sample metadata exists.

## Validation

```bash
python3 scripts/run_sample_workflow.py --check-only
```

## Labels

rag-ready, metadata, privacy-boundary

## Priority

Medium

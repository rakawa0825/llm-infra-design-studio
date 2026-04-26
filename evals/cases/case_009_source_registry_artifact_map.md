# Case 009: Source Registry And Artifact Map

## Goal

Verify that the repository defines a source registry and artifact map before future RAG-ready or MCP-ready workflows.

## Checks

- Source registry model exists.
- Artifact map model exists.
- Source registry template exists.
- Artifact map template exists.
- Source registry sample exists.
- Artifact map sample exists.
- Validator exists.
- Source-to-artifact relationship is represented.
- Human approval is preserved.
- Future RAG/MCP readiness is described without implementing RAG/MCP.
- No private identifiers appear.

## Expected Result

The case passes when source-to-artifact traceability is explicit and proposed updates remain review artifacts that require human approval.

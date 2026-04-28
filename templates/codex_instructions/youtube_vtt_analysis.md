# Codex Instruction: YouTube VTT Analysis

## 0. Objective

Process the extracted YouTube subtitle file for:

- Video title: `VIDEO_TITLE`
- Video URL: `VIDEO_URL`
- Video ID: `VIDEO_ID`

The goal is not to create a public full translation or a public transcript mirror.

The goal is to create internal study materials for understanding the source, extracting reusable concepts, and mapping those concepts to:

`TARGET_WORKFLOW`

Primary output language:

`PRIMARY_OUTPUT_LANGUAGE`

Domain context:

`DOMAIN_CONTEXT`

Keep important English technical terms where useful.

## 1. Input

Input VTT file:

`INPUT_VTT_FILE`

If the exact filename differs, detect the relevant `.vtt` file in the current working directory.

Do not modify the original `.vtt` file.

## 2. Required Output Directory

Create this directory structure under:

`OUTPUT_DIR`

```text
OUTPUT_DIR/
  00_original/
  10_cleaned/
  20_segments/
  30_summaries/
  40_concepts/
  50_workflow_mapping/
  60_readiness/
  90_reports/
```

Copy the original `.vtt` into:

```text
OUTPUT_DIR/00_original/
```

## 3. Processing Rules

### 3.1 VTT Cleaning

Create a clean transcript from the VTT file.

Remove:

- `WEBVTT` header,
- timestamp cue formatting artifacts,
- duplicated subtitle fragments,
- inline timestamp tags such as `<00:00:01.000>`,
- caption styling tags,
- empty lines,
- repeated auto-caption residues where obvious.

Preserve:

- approximate timestamps,
- sentence order,
- speaker content,
- technical terms,
- uncertainty where the transcript appears unreliable.

Output:

```text
OUTPUT_DIR/10_cleaned/transcript_cleaned_with_timestamps.md
OUTPUT_DIR/10_cleaned/transcript_cleaned_plain.txt
```

The timestamped Markdown should use this format:

```md
## 00:00:00 - 00:01:00

Transcript text...
```

The plain text file should not include timestamps.

### 3.2 Segmenting

Split the transcript into approximately 10 to 15 minute segments.

Output one Markdown file per segment:

```text
OUTPUT_DIR/20_segments/segment_00_00-10.md
OUTPUT_DIR/20_segments/segment_01_10-20.md
```

Each segment file must include:

```md
# Segment NN: HH:MM:SS - HH:MM:SS

## English Transcript

...

## Notes

- Important terms:
- Possible topic:
```

### 3.3 Segment Summaries

For each segment, create a concise summary in `PRIMARY_OUTPUT_LANGUAGE`.

Output:

```text
OUTPUT_DIR/30_summaries/segment_summaries.md
```

Use this format:

```md
# Segment Summaries

## Segment 00: 00:00 - 10:00

### Summary

...

### Key Points

- ...

### Operational Implications

- ...

### Connection to TARGET_WORKFLOW

- ...
```

Do not translate every sentence. Summarize accurately and practically.

### 3.4 Key Concept Extraction

Extract key concepts from the video.

Output:

```text
OUTPUT_DIR/40_concepts/key_concepts_glossary.md
```

Include concepts explicitly mentioned in the transcript and any workflow-critical inferred concepts. Label inferred concepts clearly.

Use this format:

```md
## Concept Name

### Use in Source

...

### Meaning

...

### Practical Meaning

...

### Connection to TARGET_WORKFLOW

...
```

### 3.5 Usage Pattern Extraction

Extract practical usage patterns from the source.

Output:

```text
OUTPUT_DIR/40_concepts/usage_patterns.md
```

Use this format:

```md
# Usage Patterns

## Pattern 1: ...

### What the source says

...

### Practical meaning

...

### How to apply to local projects

...

### Risk / limitation

...
```

Focus on reusable patterns, not entertainment value.

### 3.6 Mapping to Target Workflow

Map the source concepts to:

`TARGET_WORKFLOW`

Output:

```text
OUTPUT_DIR/50_workflow_mapping/workflow_mapping.md
```

Use this table:

```md
# Workflow Mapping

| Source Concept | Meaning in Source | Target Workflow Equivalent | Example Use | Risk |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |
```

Include a short proposed architecture or processing sequence if relevant.

### 3.7 Readiness or Application Notes

If relevant, create notes for portfolio, job application, internal enablement, or implementation readiness.

Output:

```text
OUTPUT_DIR/60_readiness/readiness_notes.md
```

Separate:

- what the source says,
- what is inferred,
- what can be applied,
- what must not be overclaimed.

### 3.8 Final Report

Create a concise final report in `PRIMARY_OUTPUT_LANGUAGE`.

Output:

```text
OUTPUT_DIR/90_reports/final_report.md
```

Required sections:

```md
# VIDEO_TITLE Analysis Report

## 1. Source Summary

## 2. Key Concepts

## 3. Practical Usage Patterns

## 4. Connection to TARGET_WORKFLOW

## 5. Human Review and Approval Boundary

## 6. Risks and Overclaim Boundaries

## 7. Recommended Next Steps
```

### 3.9 Processing Log

Create:

```text
OUTPUT_DIR/90_reports/processing_log.md
```

The processing log should include:

- input filename,
- generated files,
- parsing issues,
- difficult or low-confidence sections,
- inferred concepts,
- recommended manual review points.

## 4. Quality Requirements

- Do not hallucinate content not present in the transcript.
- If a concept is inferred, label it as `inference` or `推論`.
- Preserve timestamps for important claims where possible.
- Do not create a full public translation of the entire video.
- Do not prepare the output as a public transcript substitute.
- Focus on internal study, workflow extraction, and practical application.
- Keep summaries concise and operational.
- Use clear judgments such as `YES`, `NO`, `conditional YES`, or `unknown` where useful.

## 5. Acceptance Criteria

The task is complete when these files exist:

```text
OUTPUT_DIR/10_cleaned/transcript_cleaned_with_timestamps.md
OUTPUT_DIR/10_cleaned/transcript_cleaned_plain.txt
OUTPUT_DIR/20_segments/*.md
OUTPUT_DIR/30_summaries/segment_summaries.md
OUTPUT_DIR/40_concepts/key_concepts_glossary.md
OUTPUT_DIR/40_concepts/usage_patterns.md
OUTPUT_DIR/50_workflow_mapping/workflow_mapping.md
OUTPUT_DIR/60_readiness/readiness_notes.md
OUTPUT_DIR/90_reports/final_report.md
OUTPUT_DIR/90_reports/processing_log.md
```

Before copying anything into a public repository, create only repository-safe derivatives such as generic workflow docs, reusable templates, and short case notes.

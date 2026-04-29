# YouTube Transcript to Study Artifact Workflow

## Purpose

This workflow converts external video learning materials into structured, reviewable study artifacts.

It is intended for:

- learning support,
- workflow pattern extraction,
- practical transfer into local engineering workflows,
- OpenAI readiness preparation,
- portfolio-safe study notes.

The purpose is not to mirror a video transcript, publish a full translation, or redistribute copyrighted source material. The reusable asset is the processing method.

## Positioning

This is not part of the v0.1 infrastructure design document generation core.

It is a supporting workflow for external learning material:

```text
YouTube / external course / lecture / technical explanation
-> structured study artifact
-> workflow pattern extraction
-> portfolio / readiness note
```

The core framework remains focused on customer hearing notes, meeting transcripts, review comments, existing design documents, vendor answers, requirement definition, high-level design patches, detailed-design handoff, and human approval checks.

This workflow demonstrates a lightweight Field-to-Artifact pattern. It can help convert external learning resources into reusable knowledge assets without making those sources part of the core design lifecycle.

## Inputs

- YouTube URL
- VTT subtitle file
- optional manual notes
- optional audio file
- optional domain context

Each source should be treated as external learning material. If the material is not redistributable, keep the source file and full derived transcript outside this public repository.

## Tools

- `yt-dlp`
- Codex
- ChatGPT
- Markdown
- Git

## Basic Commands

Create a local working directory outside the public repository:

```bash
mkdir -p ~/Downloads/video_study
cd ~/Downloads/video_study
```

List available subtitles:

```bash
yt-dlp --list-subs "YOUTUBE_URL"
```

Download English auto-subtitles without the video:

```bash
yt-dlp --write-auto-subs --sub-lang en --skip-download "YOUTUBE_URL"
```

If subtitles are unavailable or too low quality, extract audio for local manual review:

```bash
yt-dlp -x --audio-format mp3 "YOUTUBE_URL"
```

Do not commit downloaded VTT files, audio files, full transcripts, or full translations.

## Processing Steps

1. Extract the subtitle file.
2. Preserve the original VTT unchanged.
3. Clean the transcript while preserving useful timestamps.
4. Split the transcript into 10 to 15 minute segments.
5. Summarize each segment.
6. Extract key concepts.
7. Extract practical usage patterns.
8. Map concepts to a target workflow.
9. Create OpenAI readiness notes.
10. Perform human review.

## Expected Outputs

Local-only outputs may include:

- cleaned transcript
- segment files
- segment summaries
- key concept glossary
- usage patterns
- workflow mapping
- OpenAI readiness notes
- final report
- processing log

Repository-safe outputs may include:

- workflow document
- Codex instruction template
- short example README
- output type list
- safety rules
- documentation index links

## Quality Rules

- Do not publish a full transcript.
- Do not publish a full translation.
- Do not include long verbatim excerpts.
- Separate transcript facts from inference.
- Preserve timestamps for important claims.
- Keep a human review gate before external reuse.
- Do not claim official endorsement without a source.
- Do not present generated analysis as if it were source text.
- Mark assumptions clearly.

## Publication Boundary

Public repositories should contain the repeatable processing method, not the copyrighted source material.

Do include:

- reusable workflow documentation,
- Codex instruction templates,
- source-safe example metadata,
- generated artifact type lists,
- publication and safety rules.

Do not include:

- YouTube full transcripts,
- full translations,
- downloaded VTT files,
- downloaded audio files,
- long excerpts from copyrighted material,
- source-derived claims without review,
- OpenAI endorsement claims without explicit sourcing.

## Relationship to Infrastructure Design Lifecycle Framework

This workflow is a reusable pattern for converting unstructured external learning material into structured artifacts.

```text
Unstructured source material
-> source intake
-> transcript / note normalization
-> segmentation
-> concept extraction
-> workflow mapping
-> readiness notes
-> human review
-> repository-safe artifact
```

It supports learning and readiness work, while the core Infrastructure Design Lifecycle Framework remains focused on customer hearing, requirement definition, design document updates, detailed-design handoff, and approval checks.

The same pattern can inform infrastructure workflows, but this workflow does not approve design decisions and does not create core v0.1 design artifacts by itself.

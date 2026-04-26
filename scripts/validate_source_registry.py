#!/usr/bin/env python3
"""Validate source registry and artifact map samples."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_REGISTRY = ROOT / "samples" / "output" / "sample_source_registry.md"
ARTIFACT_MAP = ROOT / "samples" / "output" / "sample_artifact_map.md"

SOURCE_REQUIRED_HEADINGS = [
    "# Sample Source Registry",
    "## Source Registry",
    "## Source Type Taxonomy",
    "## Source Status Taxonomy",
    "## Authority Levels",
    "## Human Approval Boundary",
]
ARTIFACT_REQUIRED_HEADINGS = [
    "# Sample Artifact Map",
    "## Artifact Map",
    "## Source-To-Artifact Traceability",
    "## Human Approval Points",
    "## Do Not Reflect Yet",
]
SOURCE_REQUIRED_TOKENS = [
    "meeting_transcript",
    "official_source_excerpt",
    "existing_design_baseline",
    "vendor_answer",
    "active",
    "needs_review",
    "official",
    "vendor_provided",
    "meeting_statement",
]
ARTIFACT_REQUIRED_TOKENS = [
    "communication_matrix",
    "network_domain_review_packet",
    "design_decision_packet",
    "design_reflection_request",
    "human_approval_checklist",
    "Approval Required",
    "Do Not Reflect Yet",
]
RISKY_TERMS = [
    "ORI" + "X",
    "Soft" + "Bank",
    "HC" + "NET",
    "Palo " + "Alto",
    "poporonbook" + ".local",
]
LOCAL_EMAIL_RE = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.local\b")


def read(path: Path, failures: list[str]) -> str:
    if not path.is_file():
        failures.append(f"missing file: {path.relative_to(ROOT)}")
        return ""
    return path.read_text(encoding="utf-8")


def check_tokens(label: str, text: str, tokens: list[str], failures: list[str]) -> None:
    for token in tokens:
        if token not in text:
            failures.append(f"{label} missing token: {token}")


def source_ids(text: str) -> set[str]:
    return set(re.findall(r"\bSRC-REG-\d{3}\b", text))


def public_safe_scan(label: str, text: str, failures: list[str]) -> None:
    for term in RISKY_TERMS:
        if term in text:
            failures.append(f"{label}: risky marker found")
    if LOCAL_EMAIL_RE.search(text):
        failures.append(f"{label}: local email pattern found")


def main() -> int:
    failures: list[str] = []
    source_text = read(SOURCE_REGISTRY, failures)
    artifact_text = read(ARTIFACT_MAP, failures)

    if source_text:
        check_tokens("source registry", source_text, SOURCE_REQUIRED_HEADINGS, failures)
        check_tokens("source registry", source_text, SOURCE_REQUIRED_TOKENS, failures)
        public_safe_scan("source registry", source_text, failures)

    if artifact_text:
        check_tokens("artifact map", artifact_text, ARTIFACT_REQUIRED_HEADINGS, failures)
        check_tokens("artifact map", artifact_text, ARTIFACT_REQUIRED_TOKENS, failures)
        public_safe_scan("artifact map", artifact_text, failures)

    if source_text and artifact_text:
        registry_ids = source_ids(source_text)
        mapped_ids = source_ids(artifact_text)
        missing = sorted(registry_ids - mapped_ids)
        if missing:
            failures.append(f"source IDs missing from artifact map: {', '.join(missing)}")
        if "approved_by_human can only be set by humans" not in artifact_text:
            failures.append("artifact map must state approved_by_human is human-only")
        if "Proposed updates are review artifacts, not final design" not in artifact_text:
            failures.append("artifact map missing update proposal boundary")

    if failures:
        print("Source registry validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Source registry validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

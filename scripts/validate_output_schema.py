#!/usr/bin/env python3
"""Validate required headings and simple table columns in sample outputs."""

from __future__ import annotations

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = {
    "sample_source_manifest.md": ["# Sample Source Manifest", "## Notes"],
    "sample_requirements_table.md": [
        "# Sample Requirements Table",
        "## Customer Confirmation Items",
        "## Vendor Confirmation Items",
        "## Detailed-Design Handoff Items",
        "## Human Approval Points",
    ],
    "sample_unresolved_issues.md": ["# Sample Unresolved Issues", "## Human Approval Points"],
    "sample_delta_report.md": ["# Sample Delta Report", "## Assumptions", "## Human Approval Points"],
    "sample_human_approval_checklist.md": ["# Sample Human Approval Checklist", "## Approval Rules"],
    "sample_issue_register.md": ["# Sample Issue Register", "## Human Approval Points"],
    "sample_decision_log.md": ["# Sample Decision Log", "## Decision Rules"],
    "sample_stakeholder_questions.md": ["# Sample Stakeholder Questions", "## Human Review Required"],
    "sample_design_update_proposal.md": [
        "# Sample Design Update Proposal",
        "## Proposal Summary",
        "## Source Evidence",
        "## Proposed Artifact Updates",
        "## Human Approval Points",
    ],
}

REQUIRED_TABLE_COLUMNS = {
    "sample_source_manifest.md": [
        "Source ID",
        "Title",
        "Type",
        "Owner",
        "Date",
        "Summary",
        "Sample-Safety Status",
        "Downstream Use",
    ],
    "sample_requirements_table.md": [
        "Requirement ID",
        "Requirement",
        "Status",
        "Source ID",
        "Confidence",
        "Confirmation Owner",
        "Notes",
    ],
    "sample_unresolved_issues.md": [
        "Issue ID",
        "Issue",
        "Category",
        "Owner",
        "Source ID",
        "Impact",
        "Next Action",
        "Approval Needed",
    ],
    "sample_delta_report.md": [
        "Delta ID",
        "New Source",
        "Previous Understanding",
        "New Information",
        "Impacted Artifact",
        "Impact",
        "Recommendation",
        "Human Decision",
    ],
    "sample_human_approval_checklist.md": [
        "Approval ID",
        "Item",
        "Approval Type",
        "Required Approver",
        "Status",
        "Residual Risk",
        "Notes",
    ],
    "sample_issue_register.md": [
        "Issue ID",
        "Issue",
        "Category",
        "Owner Role",
        "Status",
        "Impact",
        "Next Action",
        "Source Reference",
        "Approval Required",
    ],
    "sample_decision_log.md": [
        "Decision ID",
        "Decision Statement",
        "Decision Status",
        "Decision Scope",
        "Owner Role",
        "Approver Role",
        "Decision Date",
        "Source Reference",
        "Rationale",
        "Follow-Up",
    ],
    "sample_stakeholder_questions.md": [
        "Question ID",
        "Target Stakeholder",
        "Question",
        "Reason",
        "Design Impact",
        "Status",
        "Source Reference",
        "Needed Before",
    ],
    "sample_design_update_proposal.md": [
        "Proposal ID",
        "Impacted Artifact",
        "Proposed Update",
        "Status",
        "Source Reference",
        "Human Approval Required",
    ],
}

REQUIRED_CSV_COLUMNS = {
    "sample_communication_matrix.csv": [
        "source_zone",
        "source_component",
        "destination_zone",
        "destination_component",
        "protocol",
        "port",
        "direction",
        "status",
        "source_id",
        "notes",
    ],
}


def markdown_table_headers(text: str) -> list[list[str]]:
    headers: list[list[str]] = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("|") and stripped.endswith("|"):
            cells = [cell.strip() for cell in stripped.strip("|").split("|")]
            if cells and not all(set(cell) <= {"-", " "} for cell in cells):
                headers.append(cells)
    return headers


def missing_columns(actual: list[str], required: list[str]) -> list[str]:
    return [column for column in required if column not in actual]


def has_required_columns(headers: list[list[str]], required: list[str]) -> bool:
    return any(not missing_columns(header, required) for header in headers)


def main() -> int:
    output_dir = ROOT / "samples" / "output"
    failures: list[str] = []

    for filename, headings in REQUIRED.items():
        path = output_dir / filename
        if not path.exists():
            failures.append(f"missing file: {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")
        for heading in headings:
            if heading not in text:
                failures.append(f"{path.relative_to(ROOT)} missing heading: {heading}")

        required_columns = REQUIRED_TABLE_COLUMNS.get(filename, [])
        if required_columns:
            headers = markdown_table_headers(text)
            if not has_required_columns(headers, required_columns):
                for column in required_columns:
                    failures.append(f"{path.relative_to(ROOT)} missing table column: {column}")

    for filename, required_columns in REQUIRED_CSV_COLUMNS.items():
        path = output_dir / filename
        if not path.exists():
            failures.append(f"missing file: {path.relative_to(ROOT)}")
            continue
        with path.open(newline="", encoding="utf-8") as handle:
            reader = csv.reader(handle)
            header = next(reader, [])
        for column in missing_columns(header, required_columns):
            failures.append(f"{path.relative_to(ROOT)} missing CSV column: {column}")

    if failures:
        print("Output schema validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Output schema validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

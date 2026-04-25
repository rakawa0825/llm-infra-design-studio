#!/usr/bin/env python3
"""Validate required headings in sample Markdown outputs."""

from __future__ import annotations

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
}


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

    if failures:
        print("Output schema validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Output schema validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

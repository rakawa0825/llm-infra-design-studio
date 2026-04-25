#!/usr/bin/env python3
"""Minimal placeholder comparison for v0.1 eval expectations."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    cases = [
        {
            "expected": ROOT / "evals" / "expected" / "case_001_expected.md",
            "outputs": [
                ROOT / "samples" / "output" / "sample_delta_report.md",
                ROOT / "samples" / "output" / "sample_unresolved_issues.md",
            ],
            "tokens": ["Branch-B", "Unresolved", "Customer", "Pending"],
        },
        {
            "expected": ROOT / "evals" / "expected" / "case_002_expected.md",
            "outputs": [
                ROOT / "samples" / "output" / "sample_issue_register.md",
                ROOT / "samples" / "output" / "sample_decision_log.md",
                ROOT / "samples" / "output" / "sample_stakeholder_questions.md",
                ROOT / "samples" / "output" / "sample_design_update_proposal.md",
            ],
            "tokens": [
                "Branch-B",
                "customer_confirmation_required",
                "vendor_confirmation_required",
                "detailed_design_handoff",
                "human_approval_required",
            ],
        },
    ]

    failures: list[str] = []
    for case in cases:
        expected = case["expected"]
        output_paths = case["outputs"]
        for path in [expected, *output_paths]:
            if not path.exists():
                failures.append(f"missing file: {path.relative_to(ROOT)}")
        if failures:
            continue
        expected_text = expected.read_text(encoding="utf-8")
        combined = "\n".join(path.read_text(encoding="utf-8") for path in output_paths)
        for token in case["tokens"]:
            if token in expected_text and token not in combined:
                failures.append(f"expected token not found in sample outputs: {token}")

    if failures:
        print("Expected output comparison failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Expected output comparison passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

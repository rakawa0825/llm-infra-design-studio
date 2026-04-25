#!/usr/bin/env python3
"""Minimal placeholder comparison for v0.1 eval expectations."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    expected = ROOT / "evals" / "expected" / "case_001_expected.md"
    delta = ROOT / "samples" / "output" / "sample_delta_report.md"
    unresolved = ROOT / "samples" / "output" / "sample_unresolved_issues.md"

    failures: list[str] = []
    for path in [expected, delta, unresolved]:
        if not path.exists():
            failures.append(f"missing file: {path.relative_to(ROOT)}")

    if not failures:
        expected_text = expected.read_text(encoding="utf-8")
        combined = delta.read_text(encoding="utf-8") + "\n" + unresolved.read_text(encoding="utf-8")
        for token in ["Branch-B", "Unresolved", "Customer", "Pending"]:
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

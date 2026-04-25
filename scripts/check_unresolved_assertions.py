#!/usr/bin/env python3
"""Detect risky certainty phrases inside assumption or unresolved sections."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET_DIRS = [ROOT / "samples" / "output", ROOT / "templates", ROOT / "state"]
RISKY_PHRASES = ["must be", "is confirmed", "will be implemented", "approved"]
SAFE_NEGATIONS = ["not approved", "no delta is approved", "without named human approval"]
SECTION_RE = re.compile(r"^(#{1,6})\s+(.*)$", re.MULTILINE)


def uncertain_sections(text: str) -> list[tuple[str, str]]:
    matches = list(SECTION_RE.finditer(text))
    sections: list[tuple[str, str]] = []
    for idx, match in enumerate(matches):
        title = match.group(2).strip().lower()
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        if "unresolved" in title or "assumption" in title:
            sections.append((match.group(2).strip(), text[start:end]))
    return sections


def main() -> int:
    findings: list[str] = []
    for directory in TARGET_DIRS:
        if not directory.exists():
            continue
        for path in directory.rglob("*.md"):
            text = path.read_text(encoding="utf-8", errors="replace")
            for section_title, body in uncertain_sections(text):
                lower = body.lower()
                for phrase in RISKY_PHRASES:
                    if phrase in lower:
                        risky_lines = [
                            line.strip()
                            for line in lower.splitlines()
                            if phrase in line and not any(safe in line for safe in SAFE_NEGATIONS)
                        ]
                        for _line in risky_lines:
                            findings.append(
                                f"{path.relative_to(ROOT)} section '{section_title}' contains risky phrase: {phrase}"
                            )

    if findings:
        print("Unresolved assertion check failed:")
        for finding in findings:
            print(f"- {finding}")
        return 1

    print("Unresolved assertion check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

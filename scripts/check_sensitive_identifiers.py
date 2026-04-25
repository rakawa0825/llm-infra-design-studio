#!/usr/bin/env python3
"""Scan repository text files for public-safety risks."""

from __future__ import annotations

import ipaddress
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ALLOWED_DOC_NETS = [
    ipaddress.ip_network("192.0.2.0/24"),
    ipaddress.ip_network("198.51.100.0/24"),
    ipaddress.ip_network("203.0.113.0/24"),
]

RISKY_MARKERS = [
    "CONFI" + "DENTIAL",
    "ORI" + "X",
    "Soft" + "Bank",
    "HC" + "NET",
]

SKIP_DIRS = {".git", "__pycache__", ".venv", "venv", "node_modules", "tmp", "work", "private"}
TEXT_SUFFIXES = {".md", ".csv", ".py", ".txt", ".json", ".gitignore"}
IPV4_RE = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")


def iter_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts):
            continue
        if path.suffix in TEXT_SUFFIXES or path.name == ".gitignore":
            files.append(path)
    return files


def is_allowed_doc_ip(value: str) -> bool:
    try:
        addr = ipaddress.ip_address(value)
    except ValueError:
        return False
    return any(addr in network for network in ALLOWED_DOC_NETS)


def scan_file(path: Path) -> list[str]:
    findings: list[str] = []
    text = path.read_text(encoding="utf-8", errors="replace")
    rel = path.relative_to(ROOT)

    for marker in RISKY_MARKERS:
        if marker in text:
            findings.append(f"{rel}: risky marker found: {marker}")

    for match in IPV4_RE.finditer(text):
        value = match.group(0)
        if not is_allowed_doc_ip(value):
            findings.append(f"{rel}: non-documentation IPv4 address found: {value}")

    return findings


def main() -> int:
    findings: list[str] = []
    for path in iter_files():
        findings.extend(scan_file(path))

    if findings:
        print("Sensitive identifier scan failed:")
        for finding in findings:
            print(f"- {finding}")
        return 1

    print("Sensitive identifier scan passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

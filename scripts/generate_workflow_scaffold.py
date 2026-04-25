#!/usr/bin/env python3
"""Generate placeholder workflow artifact scaffolds."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCENARIO_RE = re.compile(r"^[A-Za-z0-9_-]+$")
WARNING = (
    "This scaffold is not an approved design update.\n"
    "Human review and approval are required before any artifact is used for design decisions."
)


@dataclass(frozen=True)
class ArtifactSpec:
    filename: str
    title: str
    sections: tuple[str, ...]


WORKFLOWS: dict[str, tuple[ArtifactSpec, ...]] = {
    "meeting-to-design": (
        ArtifactSpec(
            "README.md",
            "Meeting-To-Design Scaffold",
            ("Workflow Purpose", "Expected Inputs", "Expected Outputs", "Human Review Notes"),
        ),
        ArtifactSpec(
            "meeting_intake.md",
            "Meeting Intake",
            ("Meeting Summary", "Source References", "Confirmed Facts", "Assumptions", "Unresolved Items"),
        ),
        ArtifactSpec(
            "issue_register.md",
            "Issue Register",
            ("Issue Table", "Ownership Notes", "Escalation Items", "Human Approval Points"),
        ),
        ArtifactSpec(
            "decision_log.md",
            "Decision Log",
            ("Decision Table", "Tentative Statements", "Rejected Or Deferred Items", "Human Approval Points"),
        ),
        ArtifactSpec(
            "stakeholder_questions.md",
            "Stakeholder Questions",
            ("Customer Questions", "Vendor Questions", "Internal Review Questions", "Needed Before"),
        ),
        ArtifactSpec(
            "design_update_proposal.md",
            "Design Update Proposal",
            ("Proposal Summary", "Impacted Artifacts", "Source Evidence", "Approval Required"),
        ),
        ArtifactSpec(
            "human_approval_checklist.md",
            "Human Approval Checklist",
            ("Approval Items", "Approver Roles", "Decision Status", "Residual Risks"),
        ),
    ),
    "evidence-to-decision": (
        ArtifactSpec(
            "README.md",
            "Evidence-To-Decision Scaffold",
            ("Workflow Purpose", "Expected Inputs", "Expected Outputs", "Human Review Notes"),
        ),
        ArtifactSpec(
            "source_manifest.md",
            "Source Manifest",
            ("Source Inventory", "Source References", "Coverage Notes", "Missing Sources"),
        ),
        ArtifactSpec(
            "official_source_reconciliation.md",
            "Official Source Reconciliation",
            ("Source Claims", "Meeting Alignment", "Conflicts Or Gaps", "Required Actions"),
        ),
        ArtifactSpec(
            "information_gap_request.md",
            "Information Gap Request",
            ("Gap Table", "Owner Roles", "Required Before", "Status Allowed Values"),
        ),
        ArtifactSpec(
            "design_decision_packet.md",
            "Design Decision Packet",
            (
                "Source Summary",
                "Confirmed Facts",
                "Assumptions",
                "Baseline Comparison",
                "Design Impact",
                "Human Decisions Required",
                "Do Not Reflect Yet",
            ),
        ),
        ArtifactSpec(
            "design_reflection_request.md",
            "Design Reflection Request",
            ("Target Artifacts", "Proposed Changes", "Evidence", "Assumptions", "Approval Required"),
        ),
        ArtifactSpec(
            "human_approval_checklist.md",
            "Human Approval Checklist",
            ("Approval Items", "Approver Roles", "Decision Status", "Residual Risks"),
        ),
    ),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate workflow artifact scaffolds.")
    parser.add_argument("--list-workflows", action="store_true", help="List supported workflow IDs.")
    parser.add_argument("--scenario-id", help="Synthetic scenario identifier, such as scenario_003.")
    parser.add_argument("--workflow", choices=sorted(WORKFLOWS), help="Workflow scaffold to generate.")
    parser.add_argument("--output-dir", help="Base output directory for the scenario.")
    parser.add_argument("--dry-run", action="store_true", help="Print planned files without writing.")
    parser.add_argument("--force", action="store_true", help="Overwrite generated files if they already exist.")
    return parser.parse_args()


def ensure_repo_root() -> bool:
    return (ROOT / "README.md").is_file() and (ROOT / "scripts").is_dir()


def resolve_output_dir(raw_output_dir: str, workflow: str) -> Path:
    base = Path(raw_output_dir)
    if not base.is_absolute():
        base = ROOT / base
    target = (base / workflow).resolve()
    target.relative_to(ROOT)
    return target


def metadata_block(scenario_id: str, workflow: str, generated_at: str) -> str:
    return "\n".join(
        [
            "## Metadata",
            "",
            f"- scenario_id: `{scenario_id}`",
            f"- workflow: `{workflow}`",
            f"- generated_at: `{generated_at}`",
            "- status: `draft`",
            "- source_references: `TBD`",
            "- human_approval_required: `true`",
            "",
            "## Scaffold Warning",
            "",
            WARNING,
            "",
        ]
    )


def placeholder_table(title: str) -> str:
    return "\n".join(
        [
            "| Item ID | Status | Source References | Human Approval Required | Notes |",
            "| --- | --- | --- | --- | --- |",
            f"| TBD-{title.upper().replace(' ', '-')} | draft | TBD | true | Placeholder only. |",
        ]
    )


def render_artifact(spec: ArtifactSpec, scenario_id: str, workflow: str, generated_at: str) -> str:
    lines = [
        f"# {spec.title}",
        "",
        metadata_block(scenario_id, workflow, generated_at),
    ]
    for section in spec.sections:
        lines.extend([f"## {section}", "", placeholder_table(section), ""])
    lines.extend(
        [
            "## Status Constraints",
            "",
            "- Default status: `draft`",
            "- Do not mark generated scaffold content as `approved`.",
            "- Use `review_required` or `needs_more_information` until a human approver decides.",
            "",
        ]
    )
    return "\n".join(lines)


def planned_files(target_dir: Path, workflow: str) -> list[Path]:
    return [target_dir / spec.filename for spec in WORKFLOWS[workflow]]


def generate(args: argparse.Namespace) -> int:
    if not ensure_repo_root():
        print(f"Repository root check failed: {ROOT}", file=sys.stderr)
        return 1
    if not args.scenario_id or not args.workflow or not args.output_dir:
        print("--scenario-id, --workflow, and --output-dir are required unless --list-workflows is used.", file=sys.stderr)
        return 1
    if not SCENARIO_RE.match(args.scenario_id):
        print("Invalid --scenario-id. Use letters, numbers, underscore, or hyphen only.", file=sys.stderr)
        return 1

    try:
        target_dir = resolve_output_dir(args.output_dir, args.workflow)
    except ValueError:
        print("--output-dir must stay inside the repository.", file=sys.stderr)
        return 1

    files = planned_files(target_dir, args.workflow)
    existing = [path for path in files if path.exists()]
    if existing and not args.force and not args.dry_run:
        print("Target files already exist. Re-run with --force to overwrite:", file=sys.stderr)
        for path in existing:
            print(f"- {path.relative_to(ROOT)}", file=sys.stderr)
        return 1

    print(f"Workflow: {args.workflow}")
    print(f"Scenario: {args.scenario_id}")
    print(f"Target: {target_dir.relative_to(ROOT)}")
    for path in files:
        print(f"- {path.relative_to(ROOT)}")

    if args.dry_run:
        print("Dry run complete. No files written.")
        return 0

    target_dir.mkdir(parents=True, exist_ok=True)
    generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    for spec in WORKFLOWS[args.workflow]:
        path = target_dir / spec.filename
        path.write_text(render_artifact(spec, args.scenario_id, args.workflow, generated_at), encoding="utf-8")

    print("Scaffold generation complete.")
    return 0


def main() -> int:
    args = parse_args()
    if args.list_workflows:
        for workflow in sorted(WORKFLOWS):
            print(workflow)
        return 0
    return generate(args)


if __name__ == "__main__":
    sys.exit(main())

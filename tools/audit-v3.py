#!/usr/bin/env python3
"""Audit the sanitized Version 3 documentation repository."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

EXPECTED_FILES = {
    ".github/pull_request_template.md",
    ".github/workflows/documentation-audit.yml",
    ".gitignore",
    ".markdownlint.json",
    "CONTRIBUTING.md",
    "README.md",
    "SECURITY.md",
    "docs/README.md",
    "docs/architecture/network-architecture.md",
    "docs/architecture/physical-topology.md",
    "docs/architecture/service-architecture.md",
    "docs/decisions/README.md",
    "docs/decisions/adr-0001-defer-unknown-wireless-devices.md",
    "docs/decisions/adr-0002-select-beelink-eq14.md",
    "docs/history/changelog.md",
    "docs/implementation/docker-vm.md",
    "docs/implementation/jellyfin.md",
    "docs/implementation/nas-lxc.md",
    "docs/implementation/proxmox-host.md",
    "docs/implementation/samba-systemd-automount.md",
    "docs/operations/operations-guide.md",
    "docs/operations/troubleshooting.md",
    "docs/planning/future-exploration.md",
    "docs/planning/roadmap.md",
    "docs/reference/hardware-profile.md",
    "docs/reference/inventory-summary.md",
    "docs/reference/network-addressing-policy.md",
    "docs/release/README.md",
    "docs/release/clean-history-publication.md",
    "docs/release/publication-checklist.md",
    "docs/release/repository-release-validation.md",
    "docs/services/README.md",
    "docs/services/jellyfin.md",
    "docs/services/pihole.md",
    "docs/services/samba.md",
    "docs/standards/documentation-standard.md",
    "docs/standards/public-private-boundary.md",
    "docs/standards/templates/architecture-template.md",
    "docs/standards/templates/decision-template.md",
    "docs/standards/templates/implementation-template.md",
    "docs/standards/templates/service-template.md",
    "docs/standards/templates/validation-template.md",
    "docs/validation/docker-vm.md",
    "docs/validation/infrastructure-baseline.md",
    "docs/validation/jellyfin.md",
    "docs/validation/nas-lxc.md",
    "docs/validation/proxmox-host.md",
    "tools/audit-v3.py",
}

LEGACY_FILES = {
    "docs/architecture-decisions.md",
    "docs/changelog.md",
    "docs/hardware-reference.md",
    "docs/inventory.md",
    "docs/ip-plan.md",
    "docs/network-architecture.md",
    "docs/network.md",
    "docs/operations.md",
    "docs/physical-topology.md",
    "docs/proxmox-validation.md",
    "docs/readmev2.md",
    "docs/roadmap.md",
    "docs/service-architecture.md",
    "docs/services.md",
    "docs/troubleshoooting.md",
    "readme.md",
}

DOCUMENT_STATUSES = {
    "Draft",
    "Current",
    "Needs Review",
    "Superseded",
    "Archived",
}
SYSTEM_STATUSES = {
    "Idea",
    "Planned",
    "In Progress",
    "Implemented",
    "Validated",
    "Operational",
    "Paused",
    "Blocked",
    "Retired",
    "Rejected",
}
VALIDATION_STATUSES = {
    "Not Started",
    "In Progress",
    "Passed",
    "Failed",
    "Blocked",
    "Not Applicable",
    "Passed with Exception",
}
DECISION_STATUSES = {
    "Proposed",
    "Accepted",
    "Rejected",
    "Superseded",
    "Deprecated",
}

LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
PRIVATE_IP_RE = re.compile(
    r"\b(?:10(?:\.\d{1,3}){3}|192\.168(?:\.\d{1,3}){2}|"
    r"172\.(?:1[6-9]|2\d|3[01])(?:\.\d{1,3}){2})\b"
)
MAC_RE = re.compile(r"\b(?:[0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}\b")
PRIVATE_KEY_BLOCK_RE = re.compile(
    r"-----BEGIN ([A-Z0-9 ]*PRIVATE KEY)-----"
    r".+?"
    r"-----END \1-----",
    re.DOTALL,
)
SHELL_PROMPT_RE = re.compile(
    r"^[A-Za-z0-9._-]+@[A-Za-z0-9._-]+:[^`\n]*[$#]\s+",
    re.MULTILINE,
)

STATUS_FIELDS = {
    "Document status": DOCUMENT_STATUSES,
    "System status": SYSTEM_STATUSES,
    "Service status": SYSTEM_STATUSES,
    "Validation status": VALIDATION_STATUSES,
    "Decision status": DECISION_STATUSES,
}


def strip_code_fences(text: str) -> str:
    """Remove fenced-code contents while preserving ordinary prose."""
    output: list[str] = []
    in_fence = False

    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if not in_fence:
            output.append(line)

    return "\n".join(output)


def metadata_table(text: str) -> str:
    """Return the first Field/Value metadata table near the document title."""
    lines = text.splitlines()
    start = None

    for index, line in enumerate(lines[:30]):
        if re.match(r"^\|\s*Field\s*\|\s*Value\s*\|\s*$", line):
            start = index
            break

    if start is None:
        return ""

    table_lines: list[str] = []
    for line in lines[start:]:
        if not line.startswith("|"):
            break
        table_lines.append(line)

    return "\n".join(table_lines)


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: audit-v3.py REPOSITORY_PATH", file=sys.stderr)
        return 2

    root = Path(sys.argv[1]).resolve()

    if not root.is_dir():
        print(f"ERROR: repository tree does not exist: {root}", file=sys.stderr)
        return 2

    errors: list[str] = []
    warnings: list[str] = []

    for rel in sorted(EXPECTED_FILES):
        if not (root / rel).exists():
            errors.append(f"Missing expected file: {rel}")

    for rel in sorted(LEGACY_FILES):
        if (root / rel).exists():
            errors.append(f"Legacy file still present: {rel}")

    direct_docs_md = {
        str(path.relative_to(root))
        for path in (root / "docs").glob("*.md")
        if path.is_file()
    }
    if direct_docs_md != {"docs/README.md"}:
        errors.append(
            "Unexpected Markdown directly under docs/: "
            + ", ".join(sorted(direct_docs_md))
        )

    markdown_files = sorted(root.rglob("*.md"))

    for path in markdown_files:
        rel = str(path.relative_to(root))
        text = path.read_text(encoding="utf-8")

        if not text.strip():
            errors.append(f"Empty Markdown file: {rel}")
            continue

        visible = strip_code_fences(text)

        h1_count = sum(
            1 for line in visible.splitlines()
            if line.startswith("# ")
        )
        if h1_count != 1:
            errors.append(f"{rel}: expected exactly one H1, found {h1_count}")

        if re.search(
            r"^#{1,6}\s+Revision History\s*$",
            visible,
            re.MULTILINE,
        ):
            errors.append(f"{rel}: per-file Revision History heading remains")

        metadata = metadata_table(text)
        for field, allowed in STATUS_FIELDS.items():
            pattern = re.compile(
                rf"^\|\s*{re.escape(field)}\s*\|\s*([^|]+?)\s*\|$",
                re.MULTILINE,
            )
            for match in pattern.finditer(metadata):
                value = match.group(1).strip()
                if value not in allowed:
                    errors.append(
                        f"{rel}: invalid {field!r} value {value!r}"
                    )

        if PRIVATE_IP_RE.search(text):
            matches = sorted(set(PRIVATE_IP_RE.findall(text)))
            errors.append(f"{rel}: private IPv4 address detected: {matches}")

        if MAC_RE.search(text):
            matches = sorted(set(MAC_RE.findall(text)))
            errors.append(f"{rel}: MAC address detected: {matches}")

        if PRIVATE_KEY_BLOCK_RE.search(text):
            errors.append(f"{rel}: complete private-key block detected")

        prompt_scan_text = text
        if rel == "docs/standards/documentation-standard.md":
            prompt_scan_text = prompt_scan_text.replace(
                "rohan@docker:/opt/docker/jellyfin$ docker compose ps",
                "",
            )

        if SHELL_PROMPT_RE.search(prompt_scan_text):
            errors.append(f"{rel}: copied shell prompt detected")

        if rel.startswith("docs/standards/templates/"):
            continue

        for raw_target in LINK_RE.findall(visible):
            target = raw_target.strip()

            if (
                not target
                or target.startswith("#")
                or target.startswith(("http://", "https://", "mailto:"))
                or "<" in target
                or ">" in target
            ):
                continue

            target = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not target:
                continue

            resolved = (path.parent / target).resolve()

            try:
                resolved.relative_to(root)
            except ValueError:
                errors.append(
                    f"{rel}: local link escapes repository: {raw_target}"
                )
                continue

            if not resolved.exists():
                errors.append(f"{rel}: broken local link: {raw_target}")

    all_files = {
        str(path.relative_to(root))
        for path in root.rglob("*")
        if path.is_file() and ".git" not in path.parts
    }

    unexpected_baselines = sorted(
        rel
        for rel in all_files
        if rel in {
            "public-repo-baseline.txt",
            "public-repo-baseline.tar.gz",
            "private-repo-baseline.txt",
        }
    )
    if unexpected_baselines:
        warnings.append(
            "Local baseline artifact present in working tree: "
            + ", ".join(unexpected_baselines)
        )

    print("Version 3 documentation audit")
    print("=============================")
    print(f"Repository: {root}")
    print(f"Markdown files checked: {len(markdown_files)}")
    print(f"Expected active files: {len(EXPECTED_FILES)}")
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")

    if warnings:
        print("\nWarnings:")
        for warning in warnings:
            print(f"- {warning}")

    if errors:
        print("\nErrors:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("\nAudit passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

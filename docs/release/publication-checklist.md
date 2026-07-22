# Publication Checklist

| Field | Value |
|---|---|
| Document status | Current |
| Validation status | Not Started |
| Visibility | Public |
| Last reviewed | 2026-07-22 |
| Source of truth for | Pre-publication review of the sanitized repository |

## Purpose

This checklist must be completed before creating the employer-facing repository.

It verifies that the source branch is technically accurate, internally consistent, and free from intentionally excluded operational details.

## Source Requirements

- [ ] The source repository is the approved development repository.
- [ ] The source branch is the reviewed Version 3 branch.
- [ ] The working tree is clean.
- [ ] All intended Batch 9 files are committed.
- [ ] The branch has been pushed to the private development remote.
- [ ] Public release content is not being assembled from uncommitted local files.

Commands:

```bash
git branch --show-current
git status --short
git log -1 --oneline
```

## Structure Requirements

- [ ] Root `README.md` exists.
- [ ] `docs/README.md` exists.
- [ ] Architecture, decisions, implementation, validation, services, operations, reference, planning, history, standards, and release directories exist.
- [ ] Permanent `tools/audit-v3.py` exists.
- [ ] GitHub Actions documentation audit exists.
- [ ] Legacy Version 2 files are absent.
- [ ] No empty Markdown placeholders remain.
- [ ] No unexpected Markdown file exists directly under `docs/`.

Run:

```bash
python3 tools/audit-v3.py .
```

Expected:

```text
Errors: 0
Audit passed.
```

## Accuracy Requirements

- [ ] Proxmox is marked `Operational`.
- [ ] NAS LXC is marked `Operational`.
- [ ] Samba is marked `Operational`.
- [ ] Docker VM is marked `Operational`.
- [ ] Pi-hole is marked `Operational`.
- [ ] Jellyfin is marked `In Progress`.
- [ ] Immich is marked `Planned`.
- [ ] Pi-hole migration is marked `Paused`.
- [ ] Plex and Home Assistant remain ideas.
- [ ] No document claims Jellyfin is running or validated.

## Privacy Requirements

- [ ] No exact production private IP address appears.
- [ ] No MAC address appears.
- [ ] No serial number appears.
- [ ] No disk UUID appears.
- [ ] No household-member name appears.
- [ ] No personal-device name appears.
- [ ] No exact physical port or cable map appears.
- [ ] No raw identifying command output appears.
- [ ] No administrative URL appears.
- [ ] No detailed recovery secret appears.

## Secret Requirements

- [ ] No password appears.
- [ ] No access token appears.
- [ ] No API key appears.
- [ ] No private key appears.
- [ ] No recovery code appears.
- [ ] No credential file appears.
- [ ] No secret `.env` file appears.
- [ ] No workflow secret is required by the documentation audit.

Review tracked files:

```bash
git ls-files
git grep -nEi \
  'password|passwd|api[_ -]?key|access[_ -]?token|secret|private[_ -]?key|credentials' \
  -- '*.md' '*.yml' '*.yaml' '*.json' '*.py' || true
```

Every result must be reviewed. Explanatory security text may legitimately match.

## Link and Formatting Requirements

- [ ] Local Markdown links resolve.
- [ ] Each Markdown document has exactly one real H1.
- [ ] Metadata statuses use controlled vocabulary.
- [ ] No per-file revision-history heading remains.
- [ ] No copied shell prompt remains in reusable instructions.
- [ ] JSON configuration parses.
- [ ] No trailing whitespace is present.

Commands:

```bash
python3 tools/audit-v3.py .
python3 -m json.tool .markdownlint.json >/dev/null
git diff --check
```

## Workflow Requirements

- [ ] Workflow uses read-only contents permission.
- [ ] Workflow runs on pull requests and pushes.
- [ ] Workflow does not use `pull_request_target`.
- [ ] Workflow does not require secrets.
- [ ] Workflow runs the repository-local audit tool.
- [ ] Workflow run passes on the source branch.

## Export Requirements

- [ ] Export is created from tracked files, not by copying the working directory.
- [ ] The export contains no `.git` directory.
- [ ] The export contains no local baseline output.
- [ ] The export contains no batch ZIP files.
- [ ] The export contains no private repository files.
- [ ] The exported audit passes before Git initialization.

## New Repository Requirements

- [ ] A new empty GitHub repository has been created.
- [ ] No automatically generated README, license, or `.gitignore` conflicts with the export.
- [ ] Repository visibility is reviewed before the first push.
- [ ] The new remote URL is correct.
- [ ] The first commit contains only sanitized Version 3 content.
- [ ] The old development remote is not configured in the release clone.

## Post-Push Requirements

- [ ] Root README renders correctly.
- [ ] Mermaid diagrams render.
- [ ] Documentation navigation works.
- [ ] GitHub Actions audit passes.
- [ ] No legacy files appear.
- [ ] Security and contribution documents appear.
- [ ] Repository description and topics contain no private values.
- [ ] Release validation record is updated with observed results.

## Approval

| Field | Result |
|---|---|
| Source audit | Not Started |
| Privacy review | Not Started |
| Export audit | Not Started |
| Remote workflow | Not Started |
| Final publication approval | Not Started |

## Related Documentation

- [Clean-History Publication](clean-history-publication.md)
- [Repository Release Validation](repository-release-validation.md)
- [Security Policy](../../SECURITY.md)
- [Public and Private Information Boundary](../standards/public-private-boundary.md)

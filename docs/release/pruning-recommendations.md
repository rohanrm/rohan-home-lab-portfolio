# Pruning Recommendations

| Field | Value |
|---|---|
| Document status | Current |
| Visibility | Public |
| Last reviewed | 2026-10-02 |
| Source of truth for | Pruning Recommendations |



## Scope

These are recommendations, not automatic deletions. V4 preserves the original file paths so existing references and historical decisions remain reviewable. No legacy Version 2 files are present in the audited source tree.

| Candidate | Recommendation | Reason / condition |
|---|---|---|
| `tools/audit-v3.py` | Retain as compatibility wrapper now; remove after callers migrate | V4 is the canonical checker; wrapper avoids an abrupt workflow break |
| July `docs/validation/infrastructure-baseline.md`, `proxmox-host.md`, `nas-lxc.md`, `docker-vm.md` | Move into a historical validation directory later, updating links | Useful dated evidence; misleading if treated as current results |
| July batch-by-batch changelog entries | Condensed in V4; retain originals in Git | Detailed editorial batch history obscured technical milestones |
| `docs/reference/inventory-summary.md` | Consider merging into service catalogue/hardware profile | Overlapping inventory can drift; retain only if navigation value justifies it |
| `docs/release/clean-history-publication.md` | Retain, with separate new-repo and existing-repo paths | Private-history protection is still relevant |
| `docs/standards/templates/` | Optional removal from public portfolio only | Helpful authoring tools but secondary to employer evidence; private copies can support maintenance |
| Original ADR-0001 and ADR-0002 | Keep | Historical reasoning remains useful; later design needs new decisions |
| Separate implementation/service/validation pages | Keep where responsibilities differ | Procedure, operation and evidence serve distinct purposes |
| `.gitignore` test line | Removed | No useful ignore rule or documentation value |
| Old no-container troubleshooting case | Keep as historical symptom pattern | Reusable diagnosis; explicitly not current Jellyfin state |

## High-priority cleanup rule

When new evidence arrives, update its primary record and references rather than copying a status statement across many documents. Prefer links to the service catalogue and V4 baseline. Never prune operational data or working configuration based solely on documentation suggestions.

See [file audit](v4-document-audit.md) for the complete source inventory and [index](../README.md) for navigation.

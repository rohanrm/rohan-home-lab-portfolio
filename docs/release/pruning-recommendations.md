# Documentation Pruning Review

| Field | Value |
|---|---|
| Document status | Current |
| Visibility | Public |
| Last reviewed | 2026-10-02 |
| Source of truth for | Applied cleanup and retained documentation rationale |

## Applied after publication

| Candidate | Applied treatment | Reason |
|---|---|---|
| July commissioning validation pages | Moved to `archive/commissioning-2026-07/` | Preserve dated proof outside current-state records |
| Large older troubleshooting knowledge base | Archived; replaced live guide with current diagnostic matrix | Keep useful examples while removing obsolete live claims |
| Duplicate inventory summary | Removed; links point to catalogue/hardware reference | Reduce repeated lifecycle and inventory maintenance |
| V3 audit wrapper | Removed; V4 checker is canonical | No active caller requires it |
| V3/V4 working branches | Archive tips, then remove after ancestry checks | `main` is the only live branch |

## Retained deliberately

Architecture decisions preserve reasoning. Authoring templates still support maintenance. Separate architecture, implementation, service and validation documents answer different questions. Publication and privacy policies remain required. No operational configuration, private evidence database, or user data is deleted by this documentation cleanup.

See [cleanup record](cleanup-record.md), [archive](../../archive/README.md), and [documentation index](../README.md).

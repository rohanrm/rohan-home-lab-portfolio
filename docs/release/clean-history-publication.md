# Separated-History Publication

| Field | Value |
|---|---|
| Document status | Current |
| Visibility | Public |
| Last reviewed | 2026-10-02 |
| Source of truth for | Separated-History Publication |



## Repository separation

The private blueprint contains development history; it remains private. The employer-facing portfolio has its own sanitized history. Copy reviewed public file content into a branch based on the portfolio's own current commit. Do not create a public branch from a private commit, add private history as a merge parent, or push the private companion directory.

## Publication sequence

1. Inventory the source tree and reconcile current facts with dated evidence.
2. Build the sanitized public tree separately from private additions.
3. Run the public audit, inspect diagrams and all changed content, and validate links.
4. Create public commits whose parents exist only in the portfolio's history.
5. Verify the remote tree, visibility, and automation results separately.
6. Merge the public branch through the normal reviewed release process when ready.

For a wholly new public repository, initialize fresh history from the audited sanitized export. For the existing portfolio, retaining its already public sanitized ancestry avoids unnecessary history replacement.

## Credentials and historical limits

Use the authorized GitHub connection; never place a token in Git configuration, command output, or files. Removing private data from a working tree does not erase earlier commits. This V4 tree audit is not a comprehensive historical forensic scan.

See [boundary](../standards/public-private-boundary.md), [checklist](publication-checklist.md), and [validation](repository-release-validation.md).

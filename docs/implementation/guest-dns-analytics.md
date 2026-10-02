# Guest DNS Analytics Implementation

| Field | Value |
|---|---|
| Document status | Current |
| Visibility | Public |
| Last reviewed | 2026-10-02 |
| Source of truth for | Guest DNS Analytics Implementation |
| System status | In Progress |


## Data pipeline

Pi-hole FTL snapshots are filtered to guest-network clients and exported as JSONL for a dedicated SQLite archive. The monitoring guest has a restricted service account with distinct application, configuration, state, log, and import directories.

The archive uses unique event keys and an import log to support idempotent ingestion. A domain catalogue separates enrichment from raw events. Internal names, reverse queries, and resolver infrastructure are classified independently from public domains.

## Recorded progress

The initial backfill imported 77,644 records; repeating it added zero. A later capture contained 110,182 records, with 32,538 genuinely new records in preflight. These are dated import milestones, not the final coverage or count after all enrichment batches.

Reviewed rules match exact FQDNs or base domains to service families and owners. Batch 4 was reported committed. Its final row/rule totals and full precedence implementation require inspection; this record does not invent them. Backups before rule batches and integrity checks support reversible enrichment.

## Delivery still to verify

Confirm the suffix-aware base-domain implementation, exact rule precedence, current counters, ingestion from both resolvers, collection schedule, date/client filters, retention, and final dashboard separately. Preserve provenance and treat unclassified names as unknown.

## Publication boundary

No raw database, JSONL, client history, client-associated domain list, or private snapshot is included in the public repository. Demonstrate methods and aggregate milestones without identifying browsing behavior. Query counts are not visit counts.

See [service and pipeline illustration](../services/guest-dns-analytics.md), [V4 evidence](../validation/v4-baseline.md), and [roadmap](../planning/roadmap.md).

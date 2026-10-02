# Caddy DMZ Implementation

| Field | Value |
|---|---|
| Document status | Current |
| Visibility | Public |
| Last reviewed | 2026-10-02 |
| Source of truth for | Caddy DMZ Implementation |
| System status | Operational |


## Implemented pattern

The reverse proxy was placed in a dedicated DMZ LXC. WAN web ingress reaches Caddy, which terminates HTTPS and uses the permitted media-service upstream. External media access was validated in the segmented design.

## Change method

Record the prior proxy configuration privately. Confirm DNS and certificate requirements, validate the candidate Caddy configuration, and verify the upstream application before reloading. Test from an external network as well as internally; local access alone does not establish the WAN path.

Only approved application traffic should cross the DMZ/server boundary. Router forwarding is not a substitute for application authentication. Exact domains, endpoints, upstream paths, and routed rules remain private.

## Rollback and recovery

Restore the previous validated proxy configuration and narrow forwarding policy if a change fails. Preserve certificate/application state through protected backup procedures and re-test external access. Do not broaden access merely to make a failing test pass.

See [Caddy service](../services/caddy.md) and [V4 baseline](../validation/v4-baseline.md).

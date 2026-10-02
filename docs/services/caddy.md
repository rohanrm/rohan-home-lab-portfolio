# Caddy Reverse Proxy

| Field | Value |
|---|---|
| Document status | Current |
| Visibility | Public |
| Last reviewed | 2026-10-02 |
| Source of truth for | Caddy Reverse Proxy |
| Service status | Operational |


## Current state

Caddy runs in a dedicated DMZ LXC and terminates HTTPS for the approved media application. Router forwarding reaches the proxy; its permitted upstream dependency reaches Jellyfin in the server zone. External access was validated after the DMZ migration.

## Trust boundary

The proxy separates public ingress from application hosting. Keep direct management, Samba, and DNS services internal. TLS protects transport; it does not replace Jellyfin authentication or restrict upstream permissions automatically. Domain names, exact destinations, and routed rules remain private.

## Inspection and change control

On the proxy guest, inspect service state and validate a candidate configuration before reload:

```bash
systemctl is-active caddy
caddy validate --config <caddy-config-path> --adapter caddyfile
```

Then check authenticated service access from an external network and the internal upstream path. Preserve the prior configuration and certificate-related persistent state through protected backup procedures. Do not paste access logs or credential-bearing configuration into public documentation.

See [proxy implementation](../implementation/caddy-dmz.md) and [network architecture](../architecture/network-architecture.md).

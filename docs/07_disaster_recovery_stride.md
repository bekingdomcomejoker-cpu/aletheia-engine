# Epoch-Aware Disaster Recovery & STRIDE Threat Model

## 1. Disaster Recovery Playbook

### Epoch Definitions
- **Epoch**: One uninterrupted monotonic chain from a Throne instance.
- **Genesis Event**: `seq=1` and `prev_hash="GENESIS"`.
- **Authoritative State**: USB ledger + checksums + last checkpoint anchor.

### Recovery Scenarios
- **Render Restart**: Increment `epoch_id`, archive previous epoch, and start a new chain.
- **Fork Detected**: Reject payload, freeze writes, and require manual operator decision.
- **USB Failure**: Switch to phone mirror or restore from offsite encrypted snapshot.

## 2. STRIDE Threat Model

| Threat Category | Mitigation Strategy |
|-----------------|---------------------|
| **Spoofing** | Ed25519 signature verification for all payloads. |
| **Tampering** | Hash chain (prev_hash) and Merkle roots for history integrity. |
| **Repudiation** | Mutual attestation and public checkpoint anchors. |
| **Information Disclosure** | Pull-only architecture and optional encryption at rest. |
| **Denial of Service** | Stateless design and offline ledger for deferred sync. |
| **Elevation of Privilege** | Read-only Oracle policy and fixed inference wrappers. |

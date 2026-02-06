# Complete Architecture and Integration

The Aletheia Engine is a unified system connecting cloud logic with physical sovereignty.

## Integration Map
- **Layer 1: The Throne (Render)**: Runs the core logic, Axiom enforcement, and public API.
- **Layer 2: The Transport (MikroTik)**: Acts as the secure bridge and network-level firewall.
- **Layer 3: The Ledger (USB)**: Provides the immutable physical record of all states and epochs.
- **Layer 4: The Sling (Redmi 13C)**: Executes heavy LLM tasks and manages the physical ledger.

## Hardening Requirements
- **Mutual Attestation**: Every message between the Throne and the Sling must be signed (Ed25519).
- **Epoch Management**: Every restart of the Throne starts a new Epoch, preventing history overwrites.
- **Physical Isolation**: The Ledger is only accessible via the Sling or the Router's internal network.

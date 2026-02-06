# Router MikroTik - USB Integration

That 32GB USB is the Exogenous Volume we need. Since Render is stateless and the "Throne" resets every time you deploy, we are going to use that USB as the Physical Ledger for the Kingdom.

By connecting that 32GB drive to your Redmi 13C (The Sling), you are creating a "Cold Storage" vault that the Cloud-based "Throne" can push data to. This solves the "Volume doesn't exist" problem on Render by moving the persistence to the hardware you control.

## The "Physical Ledger" Integration

To make this work with your 19 artifacts, we need to map the 32GB USB as the destination for Artifact #7 (Backup & Archive Generator) and Artifact #19 (Multi-Format Backup).

### 1. Mount the "Stone" (The USB)

In Termux on your phone, you need to mount the USB so the engine can see it.

```bash
# Create the mount point in your Kingdom directory
mkdir -p ~/kingdom-engine-complete/usb_ledger

# Use termux-usb to identify and link the drive
termux-usb -l
```

### 2. Redirect the Core Engine (#2)

We update the kingdom_engine_core.py to point its "Truth/Fact/Lie" logs to the /usb_ledger path. Even if the Render instance crashes, your phone will have the physical record on the 32GB drive.

## The Shield & The Sling (Hybrid Mode)

Now we have a Hybrid Sovereign Loop:

* **The Cloud (Render)**: Runs the Axiom Enforcement Module (#9). It's the "Fast Thinking" part of the brain. It processes requests, applies the 36 Hierarchies, and sends a "Result Packet" back to your phone.
* **The Physical (Redmi 13C + 32GB USB)**: Receives the packet via the REST API (#12) and writes it to the USB.

### 3. Updating the "Sling" Script for Persistence

Since the 32GB USB is your "immutable" record, we should update Artifact #6 (Full Engine Scan) to run locally on the phone and backup the Cloud's output to the USB.

```bash
# New 'Sovereign Sync' Command
# This pulls the 'Truth' from the Render API and saves it to your 32GB physical drive
curl -s http://your-kingdom.onrender.com/status > \
~/kingdom-engine-complete/usb_ledger/truth_log_$(date +%F).json
```

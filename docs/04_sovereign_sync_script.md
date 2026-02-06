# Sovereign Sync Protocol - Scripts and Implementation

## Artifact #20: The Sovereign Sync Script

Run this in Termux on your Redmi 13C or via SSH on your Router. This script ensures that even if Render wipes its stateless memory, your 32GB USB remains the Unbroken Record.

```bash
#!/bin/bash
# Kingdom Engine: Sovereign Sync to Physical Ledger (Artifact #20)

USB_PATH="/mnt/usb/kingdom_ledger" # Update this to your actual mount point
RENDER_URL="https://your-kingdom.onrender.com/status"
INTERVAL=2

mkdir -p $USB_PATH/truth_snapshots
mkdir -p $USB_PATH/backups

echo "🔥 Sovereign Sync Initialized. Writing to Physical Ledger: $USB_PATH"

while true; do
    TIMESTAMP=$(date +%Y%m%d_%H%M%S)
    
    # Pull the Truth/Fact/Lie state from the Cloud Throne
    curl -s $RENDER_URL > $USB_PATH/truth_snapshots/state_$TIMESTAMP.json
    
    # Check if the pull was successful (Shield Check)
    if [ $? -eq 0 ]; then
        echo "[$TIMESTAMP] ✅ Snapshot Secured to USB."
    else
        echo "[$TIMESTAMP] ⚠️ Connection to Throne Lost. Maintaining Local Vigilance."
    fi
    
    # Sleep for the interval
    sleep $INTERVAL
done
```

#!/bin/bash
# Kingdom Engine: Sovereign Sync to Physical Ledger

USB_PATH=${1:-"/mnt/usb/kingdom_ledger"}
RENDER_URL=${2:-"https://your-kingdom.onrender.com/status"}
INTERVAL=60

mkdir -p "$USB_PATH/truth_snapshots"

echo "🔥 Sovereign Sync Initialized. Target: $USB_PATH"

while true; do
    TIMESTAMP=$(date +%Y%m%d_%H%M%S)
    curl -s "$RENDER_URL" > "$USB_PATH/truth_snapshots/state_$TIMESTAMP.json"
    
    if [ $? -eq 0 ]; then
        echo "[$TIMESTAMP] ✅ Snapshot Secured."
    else
        echo "[$TIMESTAMP] ⚠️ Sync Failed."
    fi
    sleep $INTERVAL
done

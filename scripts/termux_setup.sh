#!/bin/bash
# Aletheia Engine: Termux Setup for Redmi 13C

echo "🚀 Starting Sovereign Setup for Termux..."

# 1. Update and install necessary packages
echo "📦 Installing dependencies..."
pkg update && pkg upgrade -y
pkg install -y curl rclone cifs-utils libandroid-spawn

# 2. Setup storage access
echo "📂 Requesting storage access..."
termux-setup-storage

# 3. Instructions for SMB Mount (No Root required for rclone)
echo "🔗 Setting up MikroTik Ledger link..."
# We use rclone because 'mount' often requires root in Termux
# User will need to configure rclone manually for their MikroTik SMB
echo "To link your MikroTik USB without root, use rclone:"
echo "1. Run 'rclone config'"
echo "2. Create a new remote named 'mikrotik' of type 'smb'"
echo "3. Host: 192.168.88.1, User/Pass as configured in WinBox"

# 4. Create local directories
mkdir -p ~/aletheia-engine/logs
mkdir -p ~/aletheia-engine/snapshots

echo "✅ Termux environment prepared."

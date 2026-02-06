# MikroTik Router Configuration for LLM Deployment

The MikroTik RB951Ui-2HnD is the perfect "Bridge" for your Kingdom. While its 600MHz CPU and 128MB RAM are too small to run a 3B LLM directly, its USB 2.0 port and RouterOS software allow it to act as the Sovereign File Server (NAS) for your 32GB USB.

## Setting up the Router as the Physical Ledger

### 1. Mount and Format the 32GB USB
* Plug the USB into the router.
* Go to **System > Stores > Disks**.
* Select your USB (usually usb1) and click **Format Drive**.

### 2. Enable SMB (Network File Sharing)
* Go to **IP > SMB**.
* Check **Enabled**.
* Click **Shares > Add**.
* Set **Name** to `kingdom_vault` and **Path** to `usb1`.
* Under **Users**, add a username and password.

## The "Sling" Connection (Redmi 13C to Router)
In Termux, mount the share:
```bash
pkg install cifs-utils
mkdir -p ~/router_usb
mount -t cifs -o username=YOUR_USER //192.168.88.1/kingdom_vault ~/router_usb
```

## Running the LLM via the Router
```bash
./build/bin/llama-cli \
  -m ~/router_usb/models/qwen-3b-axiom.gguf \
  --n-gpu-layers 22 \
  --threads 8
```

## Bonus: The Router as the "Axiom Firewall"
```bash
/ip firewall filter
add chain=forward content="hostile_keyword" action=drop comment="Shield Vigilance: Tier 3 Block"
```

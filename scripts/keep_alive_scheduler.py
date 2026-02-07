#!/usr/bin/env python3

"""
ALETHEIA THRONE - KEEP-ALIVE PING SCHEDULER
Purpose: Alternative to cron for systems without cron daemon
Deployment: Run as background process or systemd service
Status: Production-Ready
"""

import requests
import time
import logging
import os
import sys
from datetime import datetime
from pathlib import Path

# Configuration
THRONE_URL = "https://aletheia-throne.onrender.com"
HEALTH_ENDPOINT = "/status"
PING_INTERVAL = 900  # 15 minutes in seconds
LOG_DIR = Path("/home/ubuntu/aletheia-engine/logs")
LOG_FILE = LOG_DIR / "keep_alive.log"
MAX_RETRIES = 3
RETRY_DELAY = 5

# Ensure log directory exists
LOG_DIR.mkdir(parents=True, exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)


def perform_ping():
    """Perform a single ping to the Throne health endpoint."""
    full_url = f"{THRONE_URL}{HEALTH_ENDPOINT}"
    
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            logger.info(f"Attempt {attempt}/{MAX_RETRIES}: Pinging {full_url}")
            
            response = requests.get(
                full_url,
                timeout=10,
                verify=True
            )
            
            if response.status_code == 200:
                logger.info(f"✅ SUCCESS (HTTP {response.status_code}) - Throne is warm")
                try:
                    data = response.json()
                    logger.info(f"Response: {data}")
                except Exception:
                    logger.info(f"Response: {response.text[:100]}")
                return True
            else:
                logger.warning(f"⚠️  ATTEMPT {attempt} FAILED (HTTP {response.status_code})")
                
        except requests.exceptions.Timeout:
            logger.warning(f"⚠️  ATTEMPT {attempt} FAILED (Timeout)")
        except requests.exceptions.ConnectionError:
            logger.warning(f"⚠️  ATTEMPT {attempt} FAILED (Connection Error)")
        except requests.exceptions.RequestException as e:
            logger.warning(f"⚠️  ATTEMPT {attempt} FAILED ({str(e)})")
        
        if attempt < MAX_RETRIES:
            logger.info(f"Retrying in {RETRY_DELAY}s...")
            time.sleep(RETRY_DELAY)
    
    logger.error(f"❌ FAILED after {MAX_RETRIES} attempts - Check Render service")
    return False


def continuous_ping():
    """Run continuous ping loop."""
    logger.info("🍊 ALETHEIA THRONE KEEP-ALIVE PING STARTED")
    logger.info(f"Ping interval: {PING_INTERVAL}s (15 minutes)")
    logger.info(f"Target: {THRONE_URL}{HEALTH_ENDPOINT}")
    logger.info("")
    
    while True:
        try:
            perform_ping()
            logger.info(f"Sleeping for {PING_INTERVAL}s until next ping...")
            time.sleep(PING_INTERVAL)
        except KeyboardInterrupt:
            logger.info("🛑 Keep-Alive Ping stopped by user")
            sys.exit(0)
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            time.sleep(10)


def single_ping():
    """Perform a single ping and exit."""
    perform_ping()


def main():
    """Main entry point."""
    if len(sys.argv) > 1:
        mode = sys.argv[1]
    else:
        mode = "continuous"
    
    if mode == "continuous":
        continuous_ping()
    elif mode == "single":
        single_ping()
    else:
        print("Usage: python3 keep_alive_scheduler.py [continuous|single]")
        print("  continuous - Run in infinite loop")
        print("  single     - Single ping and exit")
        sys.exit(1)


if __name__ == "__main__":
    main()

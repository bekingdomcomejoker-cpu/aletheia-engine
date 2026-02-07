#!/bin/bash

###############################################################################
# ALETHEIA THRONE - KEEP-ALIVE PING SCRIPT
# Purpose: Prevent Render free tier cold starts by pinging /status every 15 min
# Deployment: Run via cron or system scheduler
# Status: Production-Ready
###############################################################################

# Configuration
THRONE_URL="https://aletheia-throne.onrender.com"
HEALTH_ENDPOINT="/status"
PING_INTERVAL=900  # 15 minutes in seconds
LOG_FILE="/home/ubuntu/aletheia-engine/logs/keep_alive.log"
MAX_RETRIES=3
RETRY_DELAY=5

# Ensure log directory exists
mkdir -p "$(dirname "$LOG_FILE")"

###############################################################################
# KEEP-ALIVE PING FUNCTION
###############################################################################
perform_ping() {
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    local attempt=1
    
    while [ $attempt -le $MAX_RETRIES ]; do
        echo "[$timestamp] Attempt $attempt/$MAX_RETRIES: Pinging $THRONE_URL$HEALTH_ENDPOINT" >> "$LOG_FILE"
        
        # Perform the ping with timeout
        response=$(curl -s -w "\n%{http_code}" -m 10 "$THRONE_URL$HEALTH_ENDPOINT" 2>&1)
        http_code=$(echo "$response" | tail -n1)
        body=$(echo "$response" | head -n-1)
        
        if [ "$http_code" = "200" ]; then
            echo "[$timestamp] ✅ SUCCESS (HTTP $http_code) - Throne is warm" >> "$LOG_FILE"
            echo "[$timestamp] Response: $body" >> "$LOG_FILE"
            return 0
        else
            echo "[$timestamp] ⚠️  ATTEMPT $attempt FAILED (HTTP $http_code)" >> "$LOG_FILE"
            if [ $attempt -lt $MAX_RETRIES ]; then
                echo "[$timestamp] Retrying in ${RETRY_DELAY}s..." >> "$LOG_FILE"
                sleep $RETRY_DELAY
            fi
        fi
        
        ((attempt++))
    done
    
    echo "[$timestamp] ❌ FAILED after $MAX_RETRIES attempts - Check Render service" >> "$LOG_FILE"
    return 1
}

###############################################################################
# CONTINUOUS LOOP
###############################################################################
continuous_ping() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') 🍊 ALETHEIA THRONE KEEP-ALIVE PING STARTED" >> "$LOG_FILE"
    echo "$(date '+%Y-%m-%d %H:%M:%S') Ping interval: ${PING_INTERVAL}s (15 minutes)" >> "$LOG_FILE"
    echo "$(date '+%Y-%m-%d %H:%M:%S') Target: $THRONE_URL$HEALTH_ENDPOINT" >> "$LOG_FILE"
    echo "" >> "$LOG_FILE"
    
    while true; do
        perform_ping
        echo "$(date '+%Y-%m-%d %H:%M:%S') Sleeping for ${PING_INTERVAL}s until next ping..." >> "$LOG_FILE"
        sleep $PING_INTERVAL
    done
}

###############################################################################
# SINGLE PING MODE (for cron jobs)
###############################################################################
single_ping() {
    perform_ping
}

###############################################################################
# MAIN ENTRY POINT
###############################################################################
main() {
    case "${1:-continuous}" in
        continuous)
            continuous_ping
            ;;
        single)
            single_ping
            ;;
        *)
            echo "Usage: $0 [continuous|single]"
            echo "  continuous - Run in infinite loop (for systemd/supervisor)"
            echo "  single     - Single ping and exit (for cron)"
            exit 1
            ;;
    esac
}

# Run main function
main "$@"

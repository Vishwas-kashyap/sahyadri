#!/usr/bin/env bash
# throttle_to_zero.sh - Block requests
AGENT="${1:-all}"
PERCENT="${2:-0}"
echo "[KILL_SWITCH] Throttling agent: $AGENT to $PERCENT%..."
python3 "$(dirname "$0")/throttle_to_zero.py" --agent "$AGENT" --percent "$PERCENT"

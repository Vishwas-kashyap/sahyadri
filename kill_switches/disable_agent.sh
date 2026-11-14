#!/usr/bin/env bash
# disable_agent.sh - Stop agent immediately
AGENT="${1:-all}"
echo "[KILL_SWITCH] Disabling agent: $AGENT..."
python3 "$(dirname "$0")/disable_agent.py" --agent "$AGENT"

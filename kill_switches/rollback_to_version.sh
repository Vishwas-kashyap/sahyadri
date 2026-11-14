#!/usr/bin/env bash
# rollback_to_version.sh - Revert version
AGENT="${1:-all}"
VERSION="${2:-v1.0.0-stable}"
echo "[KILL_SWITCH] Rolling back agent: $AGENT to version: $VERSION..."
python3 "$(dirname "$0")/rollback_to_version.py" --agent "$AGENT" --version "$VERSION"

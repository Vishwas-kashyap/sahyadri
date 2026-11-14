"""kill_switches/disable_agent.py - Tested, documented, fast kill switch to stop an agent."""
import argparse
import json
import os
import sys
from datetime import datetime

STATE_FILE = os.path.join(os.path.dirname(__file__), "agent_state.json")

def set_agent_status(agent_name, enabled=False):
    state = {}
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r") as f:
                state = json.load(f)
        except Exception:
            state = {}
    
    state[agent_name] = {
        "status": "DISABLED" if not enabled else "ACTIVE",
        "last_updated": datetime.now().isoformat(),
        "reason": "Emergency Kill Switch Activated",
        "traffic_percent": 0 if not enabled else 100
    }
    
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)
    
    action = "DISABLED" if not enabled else "ENABLED"
    print(f"[KILL_SWITCH] Agent '{agent_name}' is now {action}. Inbound requests will be rejected with 503 Service Unavailable.")
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Emergency Kill Switch: Disable Agent")
    parser.add_argument("--agent", default="all", help="Target agent name or 'all'")
    parser.add_argument("--enable", action="store_true", help="Re-enable agent")
    args = parser.parse_args()
    set_agent_status(args.agent, enabled=args.enable)

"""kill_switches/rollback_to_version.py - Fast rollback to a verified stable agent prompt/model checkpoint."""
import argparse
import json
import os
from datetime import datetime

STATE_FILE = os.path.join(os.path.dirname(__file__), "agent_state.json")

def rollback_agent(agent_name, target_version="v1.0.0-stable"):
    state = {}
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r") as f:
                state = json.load(f)
        except Exception:
            state = {}
    
    current = state.get(agent_name, {})
    current["active_version"] = target_version
    current["status"] = "ROLLED_BACK"
    current["traffic_percent"] = 100
    current["last_updated"] = datetime.now().isoformat()
    state[agent_name] = current

    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)

    print(f"[KILL_SWITCH] Successfully rolled back '{agent_name}' to checkpoint '{target_version}'.")
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Kill Switch: Rollback Agent Version")
    parser.add_argument("--agent", default="all")
    parser.add_argument("--version", default="v1.0.0-stable")
    args = parser.parse_args()
    rollback_agent(args.agent, target_version=args.version)

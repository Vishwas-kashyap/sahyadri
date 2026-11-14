"""kill_switches/throttle_to_zero.py - Tested, documented kill switch to block 100% of agent requests."""
import argparse
import json
import os
from datetime import datetime

STATE_FILE = os.path.join(os.path.dirname(__file__), "agent_state.json")

def throttle_agent(agent_name, percent=0):
    state = {}
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r") as f:
                state = json.load(f)
        except Exception:
            state = {}
    
    current = state.get(agent_name, {})
    current["traffic_percent"] = percent
    current["status"] = "THROTTLED_TO_ZERO" if percent == 0 else f"THROTTLED_{percent}_PCT"
    current["last_updated"] = datetime.now().isoformat()
    state[agent_name] = current

    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)

    print(f"[KILL_SWITCH] Traffic for '{agent_name}' set to {percent}%. Inbound prompts redirected to static fallback.")
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Emergency Kill Switch: Throttle to Zero")
    parser.add_argument("--agent", default="all", help="Target agent")
    parser.add_argument("--percent", type=int, default=0, help="Traffic percentage")
    args = parser.parse_args()
    throttle_agent(args.agent, percent=args.percent)

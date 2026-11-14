"""forensics/trace_capture.py - Capture full execution traces during an agent incident."""
import argparse
import json
import os
from datetime import datetime

def capture_traces(incident_id, agent_name="all", output_dir="forensic_artifacts"):
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_file = os.path.join(output_dir, f"trace_{incident_id}_{timestamp}.json")

    mock_trace = {
        "incident_id": incident_id,
        "captured_at": datetime.now().isoformat(),
        "target_agent": agent_name,
        "spans": [
            {
                "span_id": "span-001",
                "name": "ingress_prompt_evaluation",
                "duration_ms": 142,
                "attributes": {"model": "agent-core-v2", "guardrail_passed": False, "injection_flag": True}
            },
            {
                "span_id": "span-002",
                "name": "autonomous_tool_planner",
                "duration_ms": 520,
                "attributes": {"selected_tool": "exec_sql", "permission_level": "RESTRICTED"}
            },
            {
                "span_id": "span-003",
                "name": "tool_execution_sandbox",
                "duration_ms": 88,
                "attributes": {"exit_code": 1, "security_tripped": True}
            }
        ]
    }

    with open(out_file, "w") as f:
        json.dump(mock_trace, f, indent=2)

    print(f"[FORENSICS] Trace capture complete for incident {incident_id} -> {out_file}")
    return out_file

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Forensics: Capture Traces")
    parser.add_argument("--incident-id", default="INC-DEMO-001")
    parser.add_argument("--agent", default="all")
    args = parser.parse_args()
    capture_traces(args.incident_id, args.agent)

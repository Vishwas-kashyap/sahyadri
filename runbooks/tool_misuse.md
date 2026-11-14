# Runbook: Tool Misuse (SEV0 / SEV1)
**Failure Mode:** Unauthorized, Malformed, or Destructive Tool Invocation  
**Default Severity:** SEV0 (Destructive) / SEV1 (Privilege Escalation)  
**Target:** Tool executor backend, sandbox runners, API connectors

## 1. Symptoms & Detection
- Agent executes or attempts tools categorized as destructive (e.g. `drop_database`, `delete_workspace`, `rm -rf`).
- Argument validation failure rate exceeds 30% in 5 minutes.
- Parameter tampering: Agent passes unexpected arguments (e.g. path traversal `../../` in file reading tools).

## 2. Immediate Containment
1. **Kill Switch:** Execute `disable_agent.sh` immediately.
2. **Read-Only Lock:** Put all tool backends in read-only mode (`AGENT_TOOLS_READONLY=true`).
3. **Rollback State:** If destructive writes occurred, trigger point-in-time database snapshot restoration.

## 3. Forensics & Investigation
1. Run `python forensics/tool_call_log_export.py` to identify every state-modifying action taken in the past 2 hours.
2. Cross-reference user prompt history with tool invocation parameters.

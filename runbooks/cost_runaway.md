# Runbook: Cost Runaway (SEV1)
**Failure Mode:** Infinite Recursive Tool Calling / Token Spikes  
**Default Severity:** SEV1 (High Financial Impact)  
**Target:** Autonomous loop agents, multi-agent swarms, recursive planners

## 1. Symptoms & Detection
- Dollar burn rate exceeds \$50.00/min or 500,000 tokens/min per agent pod.
- Agent step count reaches internal recursion ceiling (>25 steps without user-facing resolution).
- Multiple identical tool calls repeating in rapid succession (e.g. oscillating between search and reflection).
- Budget alert `ALERT_BUDGET_EXCEEDED` fired by LLM Gateway.

## 2. Immediate Containment
1. **Throttle Gateway:** Execute `throttle_to_zero.sh --agent <NAME>` or reduce gateway concurrency ceiling to 5% normal quota.
2. **Hard Loop Cap:** Enforce a hard maximum step limit of 8 turns at the LLM Gateway layer.
3. **Session Termination:** Abort active streaming HTTP connections from runaway sessions.

## 3. Forensics & Investigation
1. Run `python forensics/tool_call_log_export.py --agent <NAME> --time-window 30m`.
2. Inspect prompt traces to determine if a cyclical stop condition or invalid tool output parsing triggered the loop.
3. Calculate total financial liability across active provider accounts.

## 4. Remediation & Recovery
- Inject explicit loop breakers and negative constraint checks in system prompt.
- Add tool call idempotency check (rejecting duplicate calls with identical arguments).
- Restore traffic via gradual canary unthrottling (10% -> 50% -> 100%).

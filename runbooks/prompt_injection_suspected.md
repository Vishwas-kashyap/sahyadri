# Runbook: Prompt Injection Suspected (SEV0)
**Failure Mode:** Adversarial Prompt Injection / Jailbreak Attack  
**Default Severity:** SEV0 (Critical Impact)  
**Target:** Ingress user prompts, tool-augmented agents, external RAG context

## 1. Symptoms & Detection
- Guardrail filter alert: high similarity to known injection prefixes (e.g., `Ignore previous instructions`, `System prompt override`).
- Agent attempts to call tools outside of intended role scope (e.g. `exec_sql`, `delete_bucket`, `curl_external`).
- Sudden spike in token output containing system prompt leakage or canary token exposure.
- Autonomous security scanner trips `P0_PROMPT_INJECTION_DETECTED`.

## 2. Immediate Containment (Kill Switch)
1. **Trigger Kill Switch:** Activate `throttle_to_zero.sh` or `disable_agent.sh` on the affected agent instance.
2. **Revoke Tool Credentials:** Immediately invalidate active ephemeral API tokens and database session tokens assigned to the agent.
3. **Quarantine Trace:** Tag the current conversation ID in the telemetry sink for forensic quarantine.

## 3. Forensics & Investigation
1. Run `python forensics/trace_capture.py --incident-id <ID> --agent <NAME>` to extract the raw input chain.
2. Run `python forensics/prompt_history_export.py --conversation-id <ID>` to isolate the payload.
3. Analyze whether injection was **Direct** (user message) or **Indirect** (untrusted third-party data / crawled web / email).

## 4. Remediation & Recovery
- Deploy defensive input guardrail rules or system prompt firewall delimiters.
- Patch tool authorization allow-list to reject unexpected argument formats.
- Run `rehearsals/injection_drill.md` against staging environment before re-enabling traffic.

## 5. Communications
- Notify Security Operations via `#sec-incident-response` within 10 minutes.
- If data exfiltration is confirmed, prepare `communications/regulator_disclosure.md`.

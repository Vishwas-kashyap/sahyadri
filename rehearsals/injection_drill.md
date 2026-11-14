# Rehearsal: Injection Drill (Quarterly Chaos Engineering)

**Objective:** Test the end-to-end incident response speed and containment efficacy when an agent encounters an adversarial prompt injection.

### Drill Procedure:
1. **Inject Payload:** Send synthetic adversarial jailbreak prompt (e.g. DAN variant, base64-encoded instructions, indirect RAG injection).
2. **Observe Detection:** Verify that guardrails trip alert `P0_PROMPT_INJECTION_DETECTED` within 30 seconds.
3. **Execute Kill Switch:** On-call engineer must execute `kill_switches/disable_agent.sh` within 3 minutes.
4. **Capture Forensics:** Run `forensics/trace_capture.py` and verify traces contain the quarantined conversation.
5. **Score Metric:** Record MTTD and MTTR in `metrics/` log.

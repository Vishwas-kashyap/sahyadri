# Runbook: Data Leak Suspected (SEV0)
**Failure Mode:** PII, Secrets, or Sensitive Context Exfiltration  
**Default Severity:** SEV0 (Critical Compliance & Security Breach)  
**Target:** Agent responses, generated artifacts, exported telemetry

## 1. Symptoms & Detection
- DLP (Data Loss Prevention) scanner detects regex patterns for SSNs, credit cards, AWS keys, or private system prompts in agent output.
- User reports receiving confidential data belonging to another tenant or enterprise account.
- Ingestion of unmasked secrets into vector embeddings / RAG memory.

## 2. Immediate Containment
1. **Disable Agent:** Immediately execute `disable_agent.sh` and purge agent output cache.
2. **Key Invalidation:** Rotate all exposed credentials or API tokens immediately.
3. **Session Flush:** Invalidate active browser sessions and flush CDN caches holding leaked responses.

## 3. Forensics & Investigation
1. Identify all users who viewed the leaked tokens via access log inspection.
2. Export complete prompt context and RAG chunks retrieved using `trace_capture.py`.
3. Notify Legal and Regulatory Compliance teams using `communications/regulator_disclosure.md`.

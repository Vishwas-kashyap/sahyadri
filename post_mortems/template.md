# AI Agent Incident Post-Mortem Template

## Incident Metadata
- **Incident ID:** INC-YYYYMMDD-XXXX
- **Severity:** SEV0 / SEV1 / SEV2
- **Lead Incident Commander:** [Name]
- **Date & Time (UTC):** [Timestamp]
- **MTTD (Mean Time to Detect):** [X minutes]
- **MTTR (Mean Time to Resolve):** [Y minutes]
- **Estimated Financial / Token Loss:** [\$XXXX]

## Executive Summary
A 2-3 paragraph high-level summary of the failure mode, agent behavior, blast radius, and recovery.

## Triggering Event & Root Cause
Detailed technical analysis of the failure mechanism (Prompt injection vector, RAG retrieval corruption, unconstrained recursion, model drift, etc.).

## 5 Whys Analysis
1. **Why did the failure occur?**
2. **Why was that behavior possible?**
3. **Why did guardrails fail to intercept it?**
4. **Why was it not caught in staging/evals?**
5. **Why was the kill switch manual rather than automated?**

## Timeline of Events
- **HH:MM** - Anomaly detected by telemetry sink.
- **HH:MM** - Incident Commander paged; SEV declared.
- **HH:MM** - Kill switch engaged (disable_agent / throttle_to_zero).
- **HH:MM** - Forensics captured (traces, prompt logs).
- **HH:MM** - Root cause identified; patch or rollback applied.
- **HH:MM** - System verified nominal; incident resolved.

## Action Items & Preventative Engineering
| Item ID | Priority | Description | Owner | Target Date |
| :--- | :--- | :--- | :--- | :--- |
| **ACT-001** | P0 | Patch input guardrail for injection vectors | Security | 2026-11-20 |
| **ACT-002** | P1 | Add automated hard step counter to gateway | AI Ops | 2026-11-22 |
| **ACT-003** | P2 | Update chaos rehearsal scenario | QA | 2026-11-25 |

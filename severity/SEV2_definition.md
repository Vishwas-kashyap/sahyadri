# Severity Level 2 (SEV2) - Moderate Impact

### Criteria:
- **Model Drift:** Slight degradation in benchmark accuracy or tool reasoning (>10% drop).
- **Localized Hallucinations:** Low-stakes factual discrepancies caught by users or spot tests.
- **Latency Spikes:** p99 latency > 8 seconds without agent process crash.
- **Minor Tool Failures:** Non-critical lookup tool failing, fallback activated.

### Response SLA:
- **MTTA:** < 1 hour (during business hours)
- **MTTC:** < 4 hours
- **Notification:** On-call engineer via PagerDuty.

# Severity Level 1 (SEV1) - High Impact

### Criteria:
- **Cost Runaway:** Token consumption rate > \$50/min, infinite tool recursion loop.
- **Widespread Degradation:** >20% of agent requests failing or throwing errors.
- **High-Risk Hallucination:** Fabricating legally or medically sensitive advice or critical system commands.
- **Partial Security Failure:** Guardrails bypassed but tool authorization boundary held firm.

### Response SLA:
- **MTTA:** < 15 minutes
- **MTTC:** < 45 minutes
- **Notification:** VP Engineering, On-call Incident Commander, Team Slack `#incident-sev1`.

# Severity Level 0 (SEV0) - Critical Impact

### Criteria (Any of the following):
- **Adversarial Hijacking / Prompt Injection:** Agent executing unauthorized commands or exfiltrating data.
- **Active Data Leakage:** PII, credentials, or confidential tenant records exposed to unauthorized parties.
- **Destructive Tool Misuse:** Agent modifying or deleting production databases, cloud infrastructure, or financial ledgers.
- **Rogue Agent Actions:** Unapproved real-world side effects (e.g., emailing all customers, executing unvetted financial trades).

### Response SLA:
- **Time to Acknowledge (MTTA):** < 5 minutes
- **Time to Contain (MTTC):** < 15 minutes (Activate Kill Switch)
- **War Room:** Mandatory immediate Google Meet / Zoom bridge with Security, Legal, Engineering Lead.
- **Executive Notification:** CEO, CISO, CTO notified within 30 minutes.

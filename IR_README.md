# AI Agent Incident Response (AIR) Blueprint

> Operational framework for detecting, triaging, containing, and learning from incidents caused by or affecting autonomous AI agents. Based on the architecture by Sivasankar Natarajan.

## Folder Overview
- **`01. runbooks/`**: Failure-mode-specific procedures (Injection, Cost Runaway, Tool Misuse, Drift, Data Leak, Hallucination).
- **`02. severity/`**: SEV0, SEV1, SEV2 definitions and the triage decision tree.
- **`03. kill_switches/`**: Fast, tested scripts to disable, throttle, or roll back agents.
- **`04. forensics/`**: Tools to capture traces, export prompt history, and dump tool call logs.
- **`05. communications/`**: Slack/Teams notification templates and regulatory disclosure guides.
- **`06. post_mortems/`**: Standard post-mortem templates, 5 Whys, and action item trackers.
- **`07. rehearsals/`**: Chaos engineering drills (Injection, Cost Spike, Drift).
- **`08. metrics/`**: Historical MTTD and MTTR tracking logs.

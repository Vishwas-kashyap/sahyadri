# Runbook: Drift Detected (SEV2)
**Failure Mode:** Model Behavioral Drift, Latency Degradation, or Semantic Alignment Loss  
**Default Severity:** SEV2 (Moderate Impact)  
**Target:** Upstream LLM provider updates, system prompt changes, data distribution shifts

## 1. Symptoms & Detection
- Evaluation benchmark score drops by >15% on daily golden test dataset.
- Tool selection accuracy declines; increase in agent retry steps.
- p99 token generation latency increases by >50%.

## 2. Containment & Remediation
1. Pin model version explicitly (e.g. `claude-3-5-sonnet-20241022` or `gpt-4o-2024-08-06`) instead of generic alias (`latest`).
2. Run `rollback_to_version.sh` to revert to previous validated prompt/config commit.
3. Schedule `rehearsals/drift_drill.md` to establish updated baseline benchmarks.

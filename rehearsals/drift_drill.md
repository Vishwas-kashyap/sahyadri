# Rehearsal: Drift Drill (Monthly Chaos Engineering)

**Objective:** Validate that degradation in model outputs or benchmark regressions trigger automated rollback to the last known-good checkpoint.

### Drill Procedure:
1. **Simulate Degradation:** Inject a perturbed model checkpoint or corrupted system prompt with missing guardrails.
2. **Observe Benchmark Alarm:** Automated evaluation pipeline alerts on accuracy drop > 15%.
3. **Execute Rollback:** Run `kill_switches/rollback_to_version.sh --version v1.0.0-stable`.
4. **Verify Recovery:** Re-run golden evaluation suite and verify benchmark scores return to baseline.

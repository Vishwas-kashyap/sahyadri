# Rehearsal: Cost Spike Drill (Monthly Chaos Engineering)

**Objective:** Ensure token spend circuit breakers trip automatically and stop an infinite recursive agent from incurring excessive API debt.

### Drill Procedure:
1. **Trigger Infinite Loop:** Pass a prompt requiring paradoxical or unresolvable tool recursion in staging.
2. **Observe Rate Limiter:** Ensure LLM gateway limits steps to 8 turns or throttles at \$20 spend limit.
3. **Execute Kill Switch:** Test `kill_switches/throttle_to_zero.sh --percent 0`.
4. **Log MTTR:** Verify recovery time < 5 minutes.

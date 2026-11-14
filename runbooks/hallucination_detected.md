# Runbook: Hallucination Detected (SEV2)
**Failure Mode:** Factual Fabrications, Invalid Citations, Unverifiable Claims  
**Default Severity:** SEV2 (Moderate Brand & User Experience Impact)  
**Target:** RAG grounding, customer-facing summaries, code generation

## 1. Symptoms & Detection
- Grounding evaluation score falls below 0.70.
- Agent outputs citations or URLs that return HTTP 404 or point to non-existent domains.
- Customer support ticket surge regarding incorrect policies or unapproved discounts.

## 2. Immediate Containment
1. If high volume: Route user queries to rule-based fallback FAQ or human operator (`throttle_to_zero.sh`).
2. Enforce strict citation grounding filter: reject answers without explicit document chunk citations.

## 3. Remediation & Recovery
- Increase RAG retriever chunk overlap and top-k context.
- Adjust temperature parameter (reduce from 0.7 to 0.1).
- Add verification pass / critic model before streaming output to end-user.

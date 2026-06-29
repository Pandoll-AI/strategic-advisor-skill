# Fact-check Workflow

Use when verifying a memo, article, deck, proposal, claim list, code comment, product statement, or important assertion.

## Claim statuses

- `Verified`: strong evidence directly supports the claim.
- `Partially supported`: evidence supports part of the claim or a weaker version.
- `Unsupported`: no adequate evidence found.
- `Contradicted`: credible evidence conflicts with the claim.
- `Outdated`: the claim was once true or source is stale for the current use.
- `Needs expert judgement`: evidence exists but interpretation requires domain/legal/clinical judgement.
- `Needs live verification`: current-fact claim could not be checked because live search or a necessary source was unavailable.

## Process

1. Extract atomic claims.
2. Prioritise claims by decision impact and risk.
3. Identify claim type: current, historical, numerical, causal, legal/regulatory, medical/scientific, product/software, market, personal/company.
4. Search/review evidence.
5. Assess source quality and freshness.
6. Check for contradiction.
7. Assign status and confidence.
8. Rewrite unsafe or overstrong claims in safer wording.
9. Summarise decision impact.

## Output table

| # | Claim | Type | Status | Evidence | Confidence | Safer wording | Decision impact |
|---|---|---|---|---|---|---|---|

## Rules

- Do not collapse multiple claims into one status.
- A precise number needs a precise source.
- A universal claim such as "always", "never", "best", "safe", "compliant", or "proven" needs strong evidence or safer wording.
- Marketing claims require extra scepticism.
- For healthcare AI, separate model capability claims from clinical outcome claims.

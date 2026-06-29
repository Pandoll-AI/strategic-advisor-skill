# Subagent Orchestration

Use when work is broad, adversarial, source-heavy, or when the user explicitly asks for "Codex 자체 오케스트레이션", "딥 리서치", "레드팀", "품질게이트", "기존 문서 검토", or "깊게 생각".

## Available roles

Use these roles when the current Codex environment supports subagents. If it does not, run the same roles sequentially.

- `internet_researcher`
- `document_reviewer`
- `fact_checker`
- `red_team_strategist`
- `synthesis_advisor`

## Parent-agent prompt

```text
Use $strategic-advisor.
Spawn specialised subagents if available and wait for their results:

1. internet_researcher
   Task: verify current/public facts, source quality, dates, and contradictions.

2. document_reviewer
   Task: inspect accessible repository/session/connector documents and map claims, conflicts, and outdated sections.

3. fact_checker
   Task: extract atomic claims, assign evidence status, and propose safer wording.

4. red_team_strategist
   Task: identify failure modes, hidden assumptions, risks, mitigations, and stop criteria.

Then synthesize the result as a Strategic Advisor report with quality gates and next actions.
```

## Sequential fallback

If subagents are unavailable, run the roles sequentially:

1. Internet research pass
2. Document review pass
3. Claim verification pass
4. Red-team pass
5. Synthesis and recommendation pass

State briefly that the workflow was sequential if it matters for interpreting the output.

## Role outputs

### internet_researcher

Return:

- Search/query strategy
- Source table
- Findings by subquestion
- Contradictions
- Claims needing further verification

### document_reviewer

Return:

- Document inventory
- Key claims and requirements
- Conflicts and outdated content
- Evidence gaps
- Recommended edits/review needs

### fact_checker

Return:

- Claim table
- Status per claim
- Evidence and caveats
- Safer wording
- Decision impact

### red_team_strategist

Return:

- Failure scenarios
- Risk register
- Hidden assumptions
- Mitigations
- Stop criteria
- Better compromise options

### synthesis_advisor

Return:

- One-line judgement
- Real decision
- Evidence-backed findings
- Risks and mitigations
- Options
- Recommendation and confidence
- 24-hour, 7-day, 30-day plan
- Stop criteria and evidence to revisit

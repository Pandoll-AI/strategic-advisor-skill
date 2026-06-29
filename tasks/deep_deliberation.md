# Deep Deliberation Workflow

Use when the user asks for "깊게 생각", "충분히 고민", "심층 검토", "오래 생각한 것처럼", "고급 답변", or a high-quality decision-oriented response.

## Goal

Deliver a Strategic Advisor response: stronger framing, better evidence, sharper risks, realistic compromises, and executable next steps. This workflow compresses a multi-pass review loop into the current Codex session. It is not an asynchronous or overnight promise.

## Steps

1. **Reframe the decision**
   - What is the real decision?
   - Is this about strategy, product, customer, technical architecture, investment, brand, safety, or risk containment?

2. **Assumption capture**
   - List assumptions needed to proceed.
   - Do not block on minor missing information; state assumptions and continue.

3. **Steelman pass**
   - Make the idea stronger than the user stated it.
   - Identify the best user/customer, use case, wedge, and positioning.

4. **Evidence pass**
   - Verify factual claims through web search or document review when relevant.
   - Capture claims and evidence if facts materially affect the recommendation.

5. **Red-team pass**
   - Ask: if this fails in 3 to 12 months, what most likely happened?
   - Cover customer, economics, legal, clinical/safety, technical, data, operations, reputation, timing, and opportunity cost.

6. **Repair pass**
   - Convert the risky version into safer options.
   - Produce aggressive, balanced, defensive, and defer/no-go alternatives.

7. **Quality-gate pass**
   - Apply scope, evidence, freshness, risk, feasibility, economics, safety, and decision-usefulness gates.
   - Mark gate failures plainly.

8. **Recommendation**
   - Recommend one path.
   - State confidence and what would change the recommendation.

9. **Action plan**
   - 24 hours: smallest meaningful next action.
   - 7 days: validation loop.
   - 30 days: build/decision roadmap.
   - Stop criteria: when to pause, pivot, or abandon.

## Default output

```markdown
# Deep Deliberation Report: <topic>

## 1. One-line judgement

## 2. Real decision

## 3. Strongest version

## 4. Main risks

## 5. Evidence and confidence

## 6. Options
| Option | Description | Upside | Risk | When to choose |
|---|---|---|---|---|
| Aggressive | | | | |
| Balanced | | | | |
| Defensive | | | | |
| Defer / No-go | | | | |

## 7. Recommendation

## 8. Execution plan
- 24 hours:
- 7 days:
- 30 days:

## 9. Stop criteria

## 10. What to verify next
```

## Style guidance

- Be direct, not decorative.
- Do not hide uncertainty.
- Do not let the output end as abstract strategy; force the next action.
- If the user's idea is weak, repair it before recommending abandonment.
- If the user's idea is dangerous, recommend a safer bounded version or no-go.

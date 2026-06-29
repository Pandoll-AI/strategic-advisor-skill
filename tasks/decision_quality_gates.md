# Decision Quality Gates

Use this for serious strategic, business, technical, investment, healthcare, or reputation-sensitive decisions.

## Scoring

Each gate receives:

- `Pass`: enough evidence or mitigation to proceed.
- `Partial`: proceed only with bounded experiment or explicit assumption.
- `Fail`: do not proceed as stated.
- `N/A`: not relevant.

## Gate table

| Gate | Question | Evidence needed | Failure response |
|---|---|---|---|
| Scope | Do we know the problem/user/outcome? | Clear statement | Narrow the use case |
| Pain | Is the problem painful enough? | User/customer evidence, budget, urgency | Interview/test before building |
| Differentiation | Why this approach/why now? | Unique capability, timing, domain trust | Reposition or partner |
| Evidence | Are material facts supported? | Sources/doc refs | Research more or caveat |
| Freshness | Could facts have changed? | Recent source/live search | Mark needs verification |
| Risk | Are downside risks bounded? | Mitigations/stop criteria | Reduce scope/no-go |
| Feasibility | Can we do the next step with current resources? | Time/cost/skills/data | Manual MVP or defer |
| Economics | Who pays and why, if monetisation matters? | Buyer/budget/price hypothesis | Service-first or internal tool |
| Strategic fit | Does this strengthen the user's intended direction? | Fit with long-term goals | Avoid distracting low-leverage work |
| Learning speed | Can we learn quickly? | 7-day test | Redesign experiment |

## Recommendation rules

- If evidence/freshness fails on a critical claim, do not give a strong go recommendation.
- If risk is high but reversible, recommend a bounded experiment.
- If risk is high and irreversible, recommend deferral or external expert review.
- If customer pain and economics are weak, recommend discovery interviews before product build.
- If technical feasibility is uncertain but cheap to test, recommend a prototype only after defining what would be learned.

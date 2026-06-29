# Risk Taxonomy

Use this taxonomy during red-team and quality-gate work.

| Risk class | Examples | Typical mitigation |
|---|---|---|
| User/customer | No budget, weak pain, wrong buyer | Discovery interviews, paid pilot |
| Market | Too small, slow procurement, crowded | Narrow wedge, differentiated positioning |
| Product | Nice-to-have, poor UX, unclear workflow | Manual MVP, workflow mapping |
| Technical | Data access, reliability, latency, integration | Prototype, architecture review |
| Data | Quality, privacy, bias, missing labels | Data audit, minimisation, governance |
| Legal/regulatory | Compliance, liability, jurisdiction | Expert review, bounded use, documentation |
| Clinical/safety | Patient harm, overreliance, validation gaps | Human-in-loop, retrospective validation, escalation |
| Security | Leakage, credentials, supply chain | Threat model, least privilege |
| Operational | Support burden, maintenance, monitoring | Scope reduction, runbooks |
| Economic | Low willingness to pay, poor unit economics | Service-first, pricing tests |
| Reputation | Overclaiming, trust loss, visible failure | Conservative claims, pilots, evidence |
| Opportunity cost | Distracts from bigger strategy | Portfolio gating |

Severity levels: Low / Medium / High / Critical.
Probability levels: Low / Medium / High.
Critical risks require explicit mitigation or a no-go/defer recommendation.

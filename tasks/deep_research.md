# Deep Research Workflow

Use for internet search, market research, literature/policy review, current facts, competitor analysis, or anything where the answer depends on external evidence.

## Trigger words

- internet search, web search, 최신, 근거 찾아줘
- deep research, 딥 리서치, 조사해줘
- verify, fact-check, 사실 검증
- 시장, 가격, 규제, 법, 소프트웨어 버전, 경쟁사, 논문, 가이드라인

## Research protocol

1. **Question decomposition**
   - Main question
   - Subquestions
   - Jurisdiction/market/language boundaries
   - Time horizon and freshness need

2. **Source strategy**
   - Primary sources first: government, regulator, standards body, official documentation, company filings, original data, peer-reviewed papers.
   - Secondary sources: reputable news, respected analysts, expert commentary.
   - Tertiary sources: encyclopaedias, blogs, forums. Use mainly for orientation, not final proof.

3. **Search passes**
   - Pass A: broad orientation queries.
   - Pass B: primary-source targeted queries.
   - Pass C: disconfirming/contradiction queries.
   - Pass D: date-specific/latest queries for time-sensitive facts.

4. **Open and inspect**
   - Do not rely on snippets alone.
   - Capture publication/update dates and access date.
   - For PDFs/reports, inspect relevant pages/tables/figures where possible.

5. **Source log**
   - Record source title, URL/path, date, type, reliability grade, key evidence, and limitations.

6. **Claim/evidence matrix**
   - Extract material claims.
   - Link each claim to evidence.
   - Mark status and confidence.

7. **Contradiction handling**
   - Actively look for sources that would make the preferred answer weaker.
   - If sources disagree, explain who says what, why they may differ, and what that means for the decision.

8. **Synthesis**
   - Summarise findings by subquestion.
   - Separate facts, interpretations, and recommendations.
   - End with implications and next verification steps.

## Minimum source requirements

| Situation | Minimum evidence expectation |
|---|---|
| Current fact | Recent authoritative source or live search disclosure |
| Legal/regulatory | Official law/regulator/government source plus caveat |
| Medical/scientific | Guideline/regulator/systematic review/original paper where possible |
| Business/market | Primary filings/data or multiple reputable secondary sources |
| Product/software | Official docs/changelog/release notes |
| Claim affects major recommendation | At least one strong source and preferably corroboration |

## Output skeleton

```markdown
# Research Memo: <topic>

## Scope
- Main question:
- Boundaries:
- Freshness requirement:

## Method
- Search/document sources used:
- Limits:

## Source table
| Source | Type | Date | Reliability | Evidence used | Limitations |
|---|---|---|---|---|---|

## Findings
### Subquestion 1
### Subquestion 2
### Subquestion 3

## Contradictions / uncertainty

## Claim verification
| Claim | Status | Evidence | Confidence | Notes |
|---|---|---|---|---|

## Implications

## Next verification steps
```

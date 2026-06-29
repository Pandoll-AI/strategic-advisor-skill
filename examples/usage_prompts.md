# Usage Prompts

## Deep idea loop

```text
Use $strategic-advisor. 다음 아이디어를 스틸맨, 레드팀, 절충안, 품질게이트, 7일 실행계획까지 돌려줘:
<idea>
```

## Deep deliberation

```text
이 아이디어를 충분히 깊게 고민해서 답해줘. 필요한 최신 사실은 직접 인터넷 검색으로 확인하고, 기존 문서가 있으면 먼저 검토해. 최종 답변은 근거, 리스크, 절충안, 실행계획까지 포함해줘.
<idea>
```

## Deep research

```text
Use $strategic-advisor for deep research. 이 주제에 대해 최신 근거를 검색하고, 주장-근거 매트릭스와 충돌하는 견해까지 포함해서 의사결정 메모를 만들어줘:
<topic>
```

## Existing document review

```text
이 저장소의 문서들을 검토해서 현재 전략과 충돌하거나 오래된 내용, 근거가 약한 주장, 다음 의사결정에 필요한 공백을 찾아줘. 문서 위치와 근거를 함께 표시해.
```

## Fact-check a draft

```text
다음 제안서의 사실관계를 검증해줘. 주장별로 Verified / Partially supported / Unsupported / Contradicted / Outdated / Needs live verification 상태를 붙이고 더 안전한 문구를 제안해:
<draft>
```

## Subagent fan-out

```text
Use $strategic-advisor with Codex 자체 오케스트레이션. 가능하면 research, document review, fact-check, red-team 역할을 병렬로 돌리고, 마지막에 하나의 deep deliberation으로 통합해줘.
<task>
```

## Healthcare AI safety

```text
의료 AI 안전성 관점에서 이 서비스를 검토해줘. 임상 안전성, 개인정보, 책임소재, human-in-the-loop, 검증 데이터, 과장 표현 리스크를 품질게이트로 평가하고 MVP 범위를 제안해.
<service idea>
```

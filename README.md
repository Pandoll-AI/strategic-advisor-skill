<h1 align="center">Strategic Advisor</h1>

<p align="center">
  <img alt="Codex Skill" src="https://img.shields.io/badge/Codex-Skill-111827?style=for-the-badge">
  <img alt="MIT License" src="https://img.shields.io/badge/License-MIT-0f766e?style=for-the-badge">
</p>

<p align="center"><strong>v0.2.0</strong> · Global Codex Skill · Python 3 · MIT</p>

<p align="center">
  <img alt="Strategic Advisor generated pixel dot hero with Pandoll" src="assets/hero.png">
</p>

<p align="center"><strong>Strategic Advisor는 중요한 결정을 근거, 리스크, 선택지, 실행계획으로 정리합니다.</strong></p>

<p align="center">막연한 질문을 결정 가능한 문제로 바꾸고, 주장과 근거와 해석을 연결해 권고안까지 설명하는 Codex 전략 자문 스킬입니다.</p>

## 왜 필요한가

중요한 결정에는 순서가 필요합니다. 먼저 실제로 결정할 문제를 좁히고, 그 다음 근거와 리스크와 실행 조건을 확인해야 합니다.

Strategic Advisor는 그 순서를 Codex가 따라갈 수 있는 작업 흐름으로 제공합니다.

```text
실제 결정 정의 -> 스틸맨 -> 근거 확인 -> 레드팀 -> 절충안 -> 품질게이트 -> 실행계획
```

제품 전략, 시장 진입, 기술 선택, 조직 운영, 민감한 서비스 기획처럼 “무엇을 해야 하는가”를 정해야 하는 상황에 맞습니다.

## 핵심 기능

- 사용자의 질문을 실제 결정 단위로 다시 잡습니다.
- 강한 버전의 아이디어를 먼저 만든 뒤, 실패 시나리오로 공격합니다.
- 출처 품질, 날짜, 충돌 근거, 주장별 검증 상태를 분리합니다.
- 문서, 저장소, 업로드 파일, 웹 근거를 함께 검토하도록 지시합니다.
- 주장마다 근거, 해석, 한계, 결정 영향을 설명하도록 요구합니다.
- 공격적 / 균형 / 방어적 / 보류 옵션을 비교합니다.
- 품질게이트를 통과하지 못한 결정에는 강한 추천을 제한합니다.
- 24시간, 7일, 30일 실행계획과 중단 기준을 남깁니다.
- 출처, 통계, 기관명, 논문명, 링크는 확인 가능한 근거가 있을 때만 사용하도록 지시합니다.

## 사용 범위

- 전문 검토가 필요한 영역에서는 자료 정리, 리스크 구조화, 검토 질문 설계에 초점을 맞춥니다.
- 웹 검색이나 외부 자료 접근이 필요한 사실은 도구 사용 가능 여부와 검증 상태를 함께 표시합니다.
- 현재 세션에서 접근 가능한 문서, 저장소, 웹 근거, 템플릿을 사용해 조사와 검토를 진행합니다.
- 산출물은 권고안, 대안, 실행계획, 중단 기준까지 이어지도록 구성합니다.
- 한국어 산출물은 사용자가 다르게 요청하지 않는 한 존대말을 기본으로 합니다.

## 설치

Codex 글로벌 스킬 폴더에 클론합니다.

```bash
git clone https://github.com/Pandoll-AI/strategic-advisor-skill.git ~/.codex/skills/strategic-advisor
```

이미 체크아웃한 폴더가 있다면 심볼릭 링크로 등록해도 됩니다.

```bash
ln -s /path/to/strategic-advisor-skill ~/.codex/skills/strategic-advisor
```

Codex에서 이렇게 요청합니다.

```text
Use $strategic-advisor. 이 아이디어를 스틸맨, 레드팀, 품질게이트, 7일 실행계획까지 검토해줘.
```

## 로컬 실행

전략 자문 작업 폴더를 만들 수 있습니다.

```bash
python3 scripts/new_advisory_pack.py "new product wedge" --out /tmp/advisory-pack
```

claim, evidence, source, risk 표를 채운 뒤 품질 게이트를 실행합니다.

```bash
python3 scripts/quality_gate.py /tmp/advisory-pack
```

스킬 패키지 검증:

```bash
python3 scripts/evaluate_skill.py --root .
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py .
```

## 주요 워크플로

- `deep_deliberation`: 깊은 전략 판단, 어려운 의사결정, 실행 권고안.
- `deep_research`: 웹 근거, 시장/경쟁/정책/문헌 조사.
- `fact_check`: 주장별 검증 상태와 더 안전한 문구.
- `document_review`: 기존 문서, 저장소, PDF, 표, 슬라이드 검토.
- `decision_quality_gates`: 범위, 근거, 신선도, 리스크, 실행 가능성, 경제성 검토.
- `subagent_orchestration`: 병렬 역할 또는 순차 역할로 조사/검토/레드팀/종합 수행.

## v0.2.0 산출물 기준

Strategic Advisor의 기본 산출물은 결론만 빠르게 제시하는 메모가 아니라, 독자가 판단 과정을 따라갈 수 있는 설명형 리포트입니다.

핵심 주장은 다음 다섯 요소를 함께 포함합니다.

```text
주장 -> 근거 -> 해석 -> 한계 -> 결정 영향
```

한국어 리포트는 존대말을 기본으로 하며, 표는 보조 수단으로만 사용합니다. 핵심 판단은 문단으로 설명합니다.

대표 샘플은 [RAG 메모리 vs grep 메모리 리포트](examples/strategic_advisor_rag_vs_grep_memory.md)에서 확인할 수 있습니다.

## 예시 요청

```text
Use $strategic-advisor. 이 SaaS 아이디어를 시장 진입 전략 관점에서 검토해줘.
스틸맨, 레드팀, 경쟁/가격 근거, 공격적/균형/방어적/보류 옵션,
7일 검증 계획과 중단 기준까지 포함해.
```

```text
Use $strategic-advisor for deep research. 이 정책 민감 제품의 공개 근거를 확인하고,
주장-근거 매트릭스와 리스크 레지스터를 만든 뒤 출시 가능 범위를 추천해줘.
```

## 감사

Strategic Advisor의 히어로 이미지는 이미지 생성 도구로 만든 Pandoll pixel dot 스타일 PNG입니다.

좋은 스킬 배포 구조와 README 스타일은 Publish Skill 레포의 형식을 참고했습니다.

## 변경 기록

변경 사항은 [CHANGELOG.md](CHANGELOG.md)를 확인하세요.

## 라이선스

MIT

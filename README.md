<h1 align="center">Strategic Advisor</h1>

<p align="center">
  <img alt="Codex Skill" src="https://img.shields.io/badge/Codex-Skill-111827?style=for-the-badge">
  <img alt="MIT License" src="https://img.shields.io/badge/License-MIT-0f766e?style=for-the-badge">
</p>

<p align="center"><strong>v0.1.0</strong> · Global Codex Skill · Python 3 · MIT</p>

<p align="center">
  <img alt="Strategic Advisor pixel dot hero with Pandoll" src="assets/hero.png">
</p>

<p align="center"><strong>Strategic Advisor는 빠른 의견을 멋지게 포장하는 스킬이 아닙니다.</strong></p>

<p align="center">판단이 필요한 문제를 실제 의사결정으로 재정의하고, 근거와 리스크와 실행 가능성을 통과한 뒤 권고안을 내는 전략 자문 워크플로입니다.</p>

## 왜 필요한가

중요한 결정은 대개 답보다 순서가 문제입니다. 아이디어를 바로 좋다/나쁘다로 판정하면 고객, 시장, 기술, 법적 리스크, 실행 비용, 중단 기준이 뒤늦게 드러납니다.

Strategic Advisor는 판단 순서를 늦춥니다.

```text
실제 결정 정의 -> 스틸맨 -> 근거 확인 -> 레드팀 -> 절충안 -> 품질게이트 -> 실행계획
```

제품 전략, 시장 진입, 기술 선택, 의료/규제 민감 서비스, 조직 운영, 투자성 의사결정처럼 “무엇을 해야 하는가”가 중요한 상황에 맞습니다.

## 핵심 기능

- 사용자의 질문을 실제 결정 단위로 다시 잡습니다.
- 강한 버전의 아이디어를 먼저 만든 뒤, 실패 시나리오로 공격합니다.
- 최신성, 출처 품질, 충돌 근거, 주장별 검증 상태를 분리합니다.
- 문서, 저장소, 업로드 파일, 웹 근거를 함께 검토하도록 지시합니다.
- 공격적 / 균형 / 방어적 / 보류 옵션을 비교합니다.
- 품질게이트를 통과하지 못한 결정에는 강한 추천을 제한합니다.
- 24시간, 7일, 30일 실행계획과 중단 기준을 남깁니다.
- 근거 없는 출처, 통계, 기관명, 논문명, 링크를 만들지 않습니다.

## 하지 않는 일

- 전문 자격을 대신하지 않습니다. 의료, 법률, 금융, 규제 판단은 의사결정 보조와 리스크 검토로 제한합니다.
- 웹 검색이 불가능한 환경에서 최신 사실을 검증된 것처럼 말하지 않습니다.
- 사용자가 원하지 않는 비동기 작업을 약속하지 않습니다.
- 체크리스트만 던지고 끝내지 않습니다. 현재 세션에서 가능한 조사, 검토, 검증을 직접 수행하도록 설계되어 있습니다.

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
- `deep_research`: 최신 근거, 시장/경쟁/정책/문헌 조사.
- `fact_check`: 주장별 검증 상태와 더 안전한 문구.
- `document_review`: 기존 문서, 저장소, PDF, 표, 슬라이드 검토.
- `decision_quality_gates`: 범위, 근거, 신선도, 리스크, 실행 가능성, 경제성 검토.
- `subagent_orchestration`: 병렬 역할 또는 순차 역할로 조사/검토/레드팀/종합 수행.

## 예시 요청

```text
Use $strategic-advisor. 이 SaaS 아이디어를 시장 진입 전략 관점에서 검토해줘.
스틸맨, 레드팀, 경쟁/가격 근거, 공격적/균형/방어적/보류 옵션,
7일 검증 계획과 중단 기준까지 포함해.
```

```text
Use $strategic-advisor for deep research. 이 규제 민감 제품의 최신 정책 근거를 확인하고,
주장-근거 매트릭스와 리스크 레지스터를 만든 뒤 출시 가능 범위를 추천해줘.
```

## 감사

Strategic Advisor의 히어로 이미지는 Pandoll이 전략 보드 앞에서 근거, 리스크, 결정을 연결하는 pixel dot 스타일로 제작했습니다.

좋은 스킬 배포 구조와 README 스타일은 Publish Skill 레포의 형식을 참고했습니다.

## 변경 기록

변경 사항은 [CHANGELOG.md](CHANGELOG.md)를 확인하세요.

## 라이선스

MIT

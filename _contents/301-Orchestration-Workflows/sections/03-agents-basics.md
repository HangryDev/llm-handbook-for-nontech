# 2. Agent의 이해

## 개요

Orchestration, RAG, 도구 호출, 평가 등 AI Agent의 기본 개념을 학습합니다.

---

## 2.1 Orchestration

여러 AI 모델과 도구를 조합하여 작업을 수행하는 것입니다.

<!-- INFORAPHIC PLACEHOLDER: Orchestration 구조 -->
![Orchestration](_assets/orchestration-structure.png)
*디자인 필요: Orchestrator가 여러 도구를 조율하는 구조*

### Orchestration 예시

```
┌─────────────────────────────────────┐
│         Orchestrator                │
│    (작업 계획 및 도구 조율)          │
└───────┬─────────┬─────────┬─────────┘
        │         │         │
   ┌────▼────┐ ┌──▼──────┐ ┌▼──────┐
   │   LLM   │ │ RAG     │ │ Tools │
   │ (생성)  │ │ (검색)  │ │(실행) │
   └─────────┘ └─────────┘ └───────┘
```

---

## 2.2 RAG 기초

Retrieval-Augmented Generation을 이해합니다.

### RAG 작동 원리

<!-- DEMO VIDEO PLACEHOLDER -->
[DEMO VIDEO: RAG 작동 원리 (3분)]

### 단계

1. **문서 로드**
   - PDF, 텍스트, 웹페이지

2. **청킹 (Chunking)**
   - 문서를 작은 단위로 분할

3. **임베딩 (Embedding)**
   - 텍스트를 벡터로 변환

4. **벡터 DB 저장**
   - 벡터 데이터베이스에 저장

5. **검색 (Retrieval)**
   - 질문과 관련된 문서 검색

6. **생성 (Generation)**
   - 검색된 문서를 바탕으로 답변 생성

---

## 2.3 도구 호출: API와 MCP

AI가 외부 도구를 사용하는 방법입니다.

### Function Calling

```python
# Function Calling 예시
tools = [
    {
        "name": "get_weather",
        "description": "현재 날씨를 가져옵니다",
        "parameters": {
            "location": "도시 이름",
            "unit": "온도 단위"
        }
    }
]
```

### MCP (Model Context Protocol)

AI 모델과 도구 간의 표준 통신 프로토콜입니다.

<!-- INFORAPHIC PLACEHOLDER: MCP 구조 -->
![MCP 구조](_assets/mcp-structure.png)
*디자인 필요: AI Model ↔ MCP Server ↔ Tools*

---

## 2.4 평가 (Evaluation)

AI Workflow의 성능을 측정하는 방법입니다.

### 평가가 왜 중요한가?

- 정확성 보장
- 개선 방향 파악
- 비용 효율화

### 평가 방법

1. **자동 평가**
   - LLM as a Judge
   - 메트릭 기반 평가

2. **수동 평가**
   - 인간 평가
   - A/B 테스트

---

## 2.5 AI Workflow의 평가란 무엇이고 왜 중요한가

### Eval UI

평가 결과를 시각화하는 대시보드입니다.

<!-- DEMO VIDEO PLACEHOLDER -->
[DEMO VIDEO: Eval UI 사용법 (2분)]

---

## 2.6 지표 세우고 평가하기

### 주요 지표

| 지표 | 설명 |
|------|------|
| 정확도 | 올바른 답변 비율 |
| 관련성 | 질문과 답변의 관련성 |
| 완결성 | 답변의 완결성 |
| 속도 | 응답 시간 |
| 비용 | API 호출 비용 |

### 평가 프롬프트

```
다음 답변을 평가해주세요:

질문: [질문]
답변: [답변]
정답: [정답]

평가 기준:
1. 정확도 (1-5점)
2. 관련성 (1-5점)
3. 완결성 (1-5점)

총점: /15점
```

---

## 2.7 프롬프트 A/B 테스팅

두 프롬프트의 성능을 비교하는 방법입니다.

### 테스트 설계

1. **가설 세우기**
   - "구조화된 프롬프트가 더 나은 결과를 줄 것이다"

2. **테스트 케이스 준비**
   - 10-20개 질문

3. **실행 및 평가**
   - 두 프롬프트 실행
   - 결과 비교

4. **결론 도출**
   - 승자 결정

<!-- INFORAPHIC PLACEHOLDER: A/B 테스트 결과 -->
![A/B 테스트](_assets/ab-testing.png)
*디자인 필요: 두 프롬프트의 성능 비교 차트*

---

## 요약

- **Orchestration**: 여러 도구 조합
- **RAG**: 문서 기반 검색 및 생성
- **도구 호출**: API, MCP
- **평가**: 정확도, 관련성, 완결성, 속도, 비용
- **A/B 테스트**: 프롬프트 비교

---

## 다음: 연습 문제

배운 내용을 연습해봅시다.

→ [연습 문제 풀기](../exercises.md)

# 1. Orchestration Tool 문법 익히기

## 개요

n8n, Zapier, Make, Dify 등 오케스트레이션 도구의 기본을 학습합니다.

---

## 1.1 오케스트레이션이란?

여러 서비스와 도구를 연결하여 자동화된 워크플로우를 만드는 것입니다.

<!-- INFORAPHIC PLACEHOLDER: 오케스트레이션 개념 -->
![오케스트레이션](_assets/orchestration.png)
*디자인 필요: 개별 도구 vs 오케스트레이션 비교*

---

## 1.2 주요 도구 비교

| 도구 | 특징 | 가격 | 추천 사용자 |
|------|------|------|-------------|
| **n8n** | 오픈소스, 자체 호스팅 가능 | 무료/유료 | 개발자, 기업 |
| **Zapier** | 가장 많은 통합 | 유료 | 비개발자 |
| **Make** | 시각적 인터페이스 | 유료 | 비개발자 |
| **Dify** | LLM 워크플로우 특화 | 오픈소스 | AI 개발자 |

---

## 1.3 n8n 기본 UI

<!-- DEMO VIDEO PLACEHOLDER -->
[DEMO VIDEO: n8n 기본 UI (4분)]

### 주요 요소

1. **노드 (Node)**
   - 트리거: 워크플로우 시작
   - 액션: 수행할 작업

2. **연결 (Connection)**
   - 노드 간 데이터 전송

3. **데이터 흐름**
   - JSON 형식으로 전달

---

## 1.4 데이터 넘기기

노드 간 데이터를 전달하는 방법입니다.

### 예시: Gmail → Google Sheets

```
┌─────────────┐    ┌──────────────┐
│   Gmail     │───▶│ Google Sheets│
│ (New Email) │    │   (Add Row)  │
└─────────────┘    └──────────────┘
     데이터              데이터
    {subject,          {subject,
     body,              body,
     from}              from}
```

### 데이터 접근

```javascript
// 이전 노드의 데이터 접근
{{ $json.subject }}
{{ $json.body }}
{{ $json.from.address }}
```

---

## 1.5 제어 노드

### Loop

반복 작업을 수행합니다.

<!-- DEMO VIDEO PLACEHOLDER -->
[DEMO VIDEO: Loop 노드 사용법 (2분)]

### Switch

조건에 따라 다른 경로로 분기합니다.

### If

단순 조건 분기입니다.

---

## 1.6 Agentic Node

AI가 자율적으로 작업을 수행하는 노드입니다.

### AI Agent 노드

- 목표 설정
- 도구 선택
- 결과 평가
- 반복 실행

<!-- INFORAPHIC PLACEHOLDER: Agentic Node 작동 -->
![Agentic Node](_assets/agentic-node.png)
*디자인 필요: Agent가 목표를 달성하는 과정*

---

## 1.7 HTTP Requests / API

외부 서비스와 연결하는 방법입니다.

### API 기본

```
Method: GET, POST, PUT, DELETE
URL: https://api.example.com/endpoint
Headers: Authentication, Content-Type
Body: Request data
```

<!-- DEMO VIDEO PLACEHOLDER -->
[DEMO VIDEO: HTTP Request 노드 (3분)]

### API Key 설정

```javascript
// Header에 API Key 추가
{
  "Authorization": "Bearer YOUR_API_KEY",
  "Content-Type": "application/json"
}
```

---

## 1.8 MCP 디렉토리

Model Context Protocol 서비스를 찾는 방법입니다.

### MCP란?

AI 모델이 외부 도구와 상호작용하는 표준 프로토콜입니다.

### MCP 서비스

- 파일 시스템 접근
- 데이터베이스 연결
- API 호출

---

## 요약

- **오케스트레이션**: 여러 서비스 연결 자동화
- **주요 도구**: n8n, Zapier, Make, Dify
- **기본 요소**: 노드, 연결, 데이터
- **제어 노드**: Loop, Switch, If
- **Agentic Node**: AI 자율 실행
- **HTTP/API**: 외부 서비스 연결

---

## 다음: 자주 쓰이는 도구들

실제로 자주 쓰이는 도구들을 연동해봅시다.

→ [다음 섹션으로](../02-commonly-used-tools.md)

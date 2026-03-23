# 1-1. 자주 쓰이는 도구들

## 개요

Google, Microsoft, Airtable 등 주요 서비스와 n8n을 연동합니다.

---

## 1. Google 계열

### Gmail

이메일을 자동화합니다.

<!-- DEMO VIDEO PLACEHOLDER -->
[DEMO VIDEO: Gmail + n8n (3분)]

### 사용 예시

- 새 이메일 알림
- 이메일 자동 분류
- 이메일 요약

### n8n 노드

```
Gmail Trigger (New Email)
    │
    ▼
AI Agent (Summary)
    │
    ▼
Slack (Send Message)
```

### API Key 설정

```bash
# Google Cloud Console
1. 프로젝트 생성
2. Gmail API 활성화
3. OAuth 2.0 클라이언트 ID 생성
4. n8n에 연결
```

---

### Google Sheets

스프레드시트를 자동화합니다.

### 사용 예시

- 데이터 자동 입력
- 데이터 분석
- 보고서 생성

### n8n 노드

```
Google Sheets (Read)
    │
    ▼
AI Agent (Analyze)
    │
    ▼
Google Sheets (Write)
```

---

### Google Slide

프레젠테이션을 자동화합니다.

### 사용 예시

- 템플릿 기반 슬라이드 생성
- 데이터 시각화 자동화

---

### Google Calendar

일정을 자동화합니다.

### 사용 예시

- 이메일에서 일정 추출
- 회의 일정 자동 예약

---

### Todoist

할 일을 관리합니다.

### 사용 예시

- 이메일에서 할 일 추출
- 일정 기반 할 일 생성

---

## 2. Microsoft 계열

### Word, Excel, PPT

Microsoft 365와 연동합니다.

### Graph API

```javascript
// Microsoft Graph API
GET https://graph.microsoft.com/v1.0/me/messages
GET https://graph.microsoft.com/v1.0/me/drive/items
```

---

## 3. Airtable

데이터베이스를 자동화합니다.

### 사용 예시

- CRUD 작업 자동화
- 데이터 동기화

---

## 4. Kaggle?

데이터셋을 활용합니다.

### 사용 예시

- 데이터셋 다운로드 자동화
- 데이터 분석 워크플로우

---

## 5. Playwright

웹 자동화를 수행합니다.

### 사용 예시

- 웹 스크래핑
- 자동 테스트

<!-- DEMO VIDEO PLACEHOLDER -->
[DEMO VIDEO: Playwright + n8n (3분)]

---

## 요약

| 도구 | 용도 | 자동화 예시 |
|------|------|-------------|
| Gmail | 이메일 | 자동 분류, 요약 |
| Sheets | 데이터 | 분석, 보고서 |
| Slides | 프레젠테이션 | 자동 생성 |
| Calendar | 일정 | 자동 예약 |
| Todoist | 할 일 | 자동 생성 |
| MS 365 | 오피스 | 문서 자동화 |
| Airtable | 데이터베이스 | CRUD 자동화 |
| Playwright | 웹 | 스크래핑 |

---

## 다음: Agent의 이해

AI Agent의 기본 개념을 알아봅시다.

→ [다음 섹션으로](../03-agents-basics.md)

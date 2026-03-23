# 3. AI Assisted Coding - Framework

## 개요

Claude Code의 고급 기능을 학습합니다.

---

## 3.1 Claude Code Hooks

자동화된 행동을 설정하는 기능입니다.

### Hooks 종류

| Hook | 타이밍 | 용도 |
|------|---------|------|
| prePrompt | 프롬프트 전 | 컨텍스트 로드 |
| postResponse | 응답 후 | 결과 정리 |
| preEdit | 편집 전 | 백업 |
| postEdit | 편집 후 | 테스트 |

### Hooks 설정

```json
// .claude/settings.json
{
  "hooks": {
    "prePrompt": "현재 프로젝트의 구조를 파악하고 README를 읽으세요",
    "postResponse": "변경된 파일을 요약하고 commit 메시지를 제안해주세요"
  }
}
```

<!-- DEMO VIDEO PLACEHOLDER -->
[DEMO VIDEO: Claude Code Hooks 설정 (3분)]

---

## 3.2 Plan

복잡한 작업을 계획하는 기능입니다.

### Plan 모드

1. 작업 분석
2. 단계별 계획 수립
3. 사용자 확인
4. 순차적 실행

---

## 3.3 AI Coding 프레임워크

### 프레임워크 선택

| 프레임워크 | 용도 | 난이도 |
|------------|------|--------|
| LangChain | LLM 앱 | 중 |
| LangGraph | Agent | 상 |
| LlamaIndex | RAG | 중 |
| Flowise | 시각적 | 하 |

---

## 요약

- **Hooks**: 자동화된 행동 설정
- **Plan**: 작업 계획 및 실행
- **프레임워크**: LangChain, LangGraph, LlamaIndex, Flowise

---

## 다음: What's After This

개발자로서의 다음 단계를 알아봅시다.

→ [다음 섹션으로](../04-whats-next.md)

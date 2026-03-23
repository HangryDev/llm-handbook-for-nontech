# 3. 모든 것의 시작: LLM과 대화하기

## 개요

ChatGPT, Claude 등 대화형 AI의 기본 기능을 실습합니다.

---

## 3.1 UI (User Interface)

### 주요 대화형 AI 도구

| 도구 | 특징 | URL |
|------|------|-----|
| **ChatGPT** | OpenAI의 대표 LLM | https://chat.openai.com |
| **Claude** | Anthropic의 안전한 LLM | https://claude.ai |
| **Gemini** | Google의 멀티모달 LLM | https://gemini.google.com |

### 기본 UI 구조

<!-- INFORAPHIC PLACEHOLDER: LLM UI 구조 -->
![LLM UI 구조](_assets/llm-ui-structure.png)
*디자인 필요: 대화형 AI의 주요 UI 요소 표시*

1. **채팅 입력창**: 프롬프트 입력
2. **대화 기록**: 이전 대화 히스토리
3. **모델 선택**: GPT-4, Claude 3.5 등 모델 선택
4. **설정**: Temperature, 시스템 프롬프트 등

---

## 3.2 캔버스 (Canvas)

### 캔버스란?

캔버스는 생성된 텍스트를 직접 편집할 수 있는 기능입니다. ChatGPT의 Advanced Data Analysis, Claude의 Artifacts 등이 있습니다.

<!-- DEMO VIDEO PLACEHOLDER -->
[DEMO VIDEO: 캔버스 기능 사용법 (2분)]

### 캔버스 활용법

1. **실시간 편집**: AI가 생성한 텍스트를 직접 수정
2. **버전 관리**: 수정 내역을 추적
3. **협업**: 팀원과 공유하며 작업

---

## 3.3 딥 리서치 (Deep Research)

### 딥 리서치란?

AI가 인터넷을 검색하고, 정보를 수집하고, 종합하여 보고서를 작성하는 기능입니다.

### 딥 리서치 도구

| 도구 | 특징 |
|------|------|
| Perplexity | AI 기반 검색 엔진 |
| Claude's Artifacts | 연구 결과를 문서로 정리 |
| ChatGPT with Browse | 웹 검색 기능 |

### 사용 예시

```
프롬프트: "2024년 AI 산업 동향을 조사하여 보고서를 작성해주세요.
주제: 생성형 AI 시장 규모, 주요 기업, 기술 동향
```

---

## 3.4 데이터 분석 & Code Interpreter

### Code Interpreter란?

AI가 Python 코드를 실행하여 데이터를 분석하고 시각화하는 기능입니다.

<!-- DEMO VIDEO PLACEHOLDER -->
[DEMO VIDEO: Code Interpreter로 데이터 분석하기 (3분)]

### 활용 사례

- CSV/엑셀 데이터 분석
- 통계 분석 및 시각화
- 데이터 클리닝

### 실습 예시

```python
# 예시: Code Interpreter로 데이터 분석
import pandas as pd
import matplotlib.pyplot as plt

# 데이터 로드
df = pd.read_csv('sales_data.csv')

# 기본 통계
print(df.describe())

# 시각화
df.plot(kind='bar')
plt.show()
```

### API Key 설정

Code Interpreter를 사용하려면 API Key가 필요할 수 있습니다.

```bash
# .env 파일
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxx
ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxxxxxxx
```

---

## 3.5 이미지 생성

### DALL-E 3

ChatGPT Plus 내에서 이미지를 생성할 수 있습니다.

```
프롬프트: "빨간색 티셔츠를 입고 귀여운 강아지와 함께 걷고 있는
        20대 여성의 모습을 그려주세요. 애니메이션 스타일로"
```

<!-- INFORAPHIC PLACEHOLDER: 이미지 생성 프롬프트 구조 -->
![이미지 생성 프롬프트 구조](_assets/image-prompt-structure.png)
*디자인 필요: Subject + Action + Style + Details 구조*

---

## 3.6 GPTs

### GPTs란?

사용자가 커스터마이징한 ChatGPT 버전입니다. 특정 작업에 최적화된 AI 어시스턴트를 만들 수 있습니다.

<!-- DEMO VIDEO PLACEHOLDER -->
[DEMO VIDEO: GPT 생성 및 사용법 (2분)]

### GPTs 생성 단계

1. **목적 정의**: 무엇을 위한 GPT인가?
2. **프롬프트 작성**: 시스템 프롬프트 작성
3. **지식 추가**: 문서 업로드 (선택)
4. **테스트**: 성능 확인
5. **공유**: 링크로 공개

---

## 요약

- **UI**: 입력창, 대화 기록, 모델 선택
- **캔버스**: 생성된 텍스트 직접 편집
- **딥 리서치**: AI 기반 정보 수집 및 정리
- **Code Interpreter**: 데이터 분석 및 시각화
- **이미지 생성**: DALL-E 3로 이미지 생성
- **GPTs**: 커스터마이즈된 AI 어시스턴트

---

## 다음: 분야별 도구

이미지, 음성, 영상 등 다양한 AI 도구를 더 알아봅시다.

→ [다음 섹션으로](../04-domain-specific-tools.md)

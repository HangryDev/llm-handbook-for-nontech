# 4. 분야별 / 기능별 도구

## 개요

이미지, 음성, 영상, 음악, 검색, 요약, RAG, PPT, 코딩 등 다양한 AI 도구를 실습합니다.

---

## 4.1 이미지 생성

### Midjourney

고품질 이미지 생성의 대표주자입니다.

<!-- DEMO VIDEO PLACEHOLDER -->
[DEMO VIDEO: Midjourney 기본 사용법 (3분)]

### 드리미나 (Driimina)

한국형 이미지 생성 서비스입니다.

### Image Prompting 공식

```
[Subject] + [Action] + [Environment] + [Style] + [Technical Specs]
```

**예시:**
```
A young woman walking a cute dog in the park,
sunny afternoon, anime style,
4k, high detail, vibrant colors
```

### Reverse Engineering

원하는 이미지가 있을 때, 그 스타일을 분석하여 프롬프트를 만드는 기술입니다.

### Inpainting & Outpainting

- **Inpainting**: 이미지의 일부를 수정
- **Outpainting**: 이미지 외부를 확장

<!-- INFORAPHIC PLACEHOLDER: Inpainting/Outpainting 비교 -->
![Inpainting/Outpainting](_assets/inpainting-outpainting.png)
*디자인 필요: Inpainting과 Outpainting의 차이를 시각화*

### Meme Mapping

밈(meme) 이미지의 스타일을 분석하고 재활용하는 기술입니다.

---

## 4.2 음성 (Voice)

### ElevenLabs

가장 자연스러운 음성 합성 서비스입니다.

<!-- DEMO VIDEO PLACEHOLDER -->
[DEMO VIDEO: ElevenLabs로 음성 생성하기 (2분)]

### 음성 생성 활용 사례

- 오디오북 제작
- 비디오 내레이션
- 포드캐스트
- 가상 어시스턴트

### API 사용 예시

```bash
# ElevenLabs API
curl -X POST https://api.elevenlabs.io/v1/text-to-speech \
  -H "xi-api-key: YOUR_API_KEY" \
  -d "안녕하세요, AI입니다."
```

---

## 4.3 영상 (Video)

### Veo 3

Google의 고성능 영상 생성 AI입니다.

### 영상 생성 프롬프트 구조

```
[Subject] + [Action] + [Camera Movement] + [Style] + [Duration]
```

**예시:**
```
A cat playing with a ball of yarn,
slow motion zoom in, cinematic style, 5 seconds
```

---

## 4.4 음악 (Music)

### SUNO AI

텍스트 프롬프트로 음악을 생성할 수 있습니다.

<!-- DEMO VIDEO PLACEHOLDER -->
[DEMO VIDEO: SUNO로 음악 생성하기 (2분)]

### 음악 생성 프롬프트

```
[Genre] + [Mood] + [Instruments] + [Tempo]
```

**예시:**
```
Upbeat K-pop, energetic mood,
synthesizer and drums, 120 BPM
```

---

## 4.5 검색 (Search)

### 퍼플렉시티 (Perplexity)

AI 기반 검색 엔진으로, 출처를 명시하며 답변을 제공합니다.

<!-- DEMO VIDEO PLACEHOLDER -->
[DEMO VIDEO: Perplexity 사용법 (2분)]

### 특징

- 출처 표기
- 팔로우업 질문 가능
- 검색 기록 저장

---

## 4.6 요약 (Summary)

### 릴리스 (Kome)

긴 텍스트나 영상을 요약합니다.

### 요약 활용 사례

- 유튜브 영상 요약
- 긴 문서 요약
- 회의록 요약

---

## 4.7 개인 문서 RAG

### NotebookLM

Google의 개인 문서 기반 Q&A 서비스입니다.

<!-- DEMO VIDEO PLACEHOLDER -->
[DEMO VIDEO: NotebookLM 실습 (3분)]

### RAG란?

Retrieval-Augmented Generation의 약자로, 개인 문서에서 정보를 검색하여 답변을 생성합니다.

### 사용 방법

1. 문서 업로드 (PDF, 텍스트, 웹사이트)
2. 질문 입력
3. 문서 기반 답변 생성

<!-- INFORAPHIC PLACEHOLDER: RAG 작동 원리 -->
![RAG 작동 원리](_assets/rag-principle.png)
*디자인 필요: 문서 → 벡터 DB → 검색 → LLM → 답변*

---

## 4.8 프레젠테이션 (PPT)

### Gamma / Genspark

AI로 PPT를 자동 생성합니다.

<!-- DEMO VIDEO PLACEHOLDER -->
[DEMO VIDEO: Gamma로 PPT 생성하기 (2분)]

### PPT 생성 과정

1. 주제 입력
2. 슬라이드 구조 자동 생성
3. 디자인 적용
4. 다운로드

---

## 4.9 AI 코딩 (바이브 코딩)

### Lovable, Cursor, Antigravity

AI로 코드를 생성하는 도구입니다.

### 바이브 코딩이란?

코딩 지식 없이 AI와 대화하며 소프트웨어를 만드는 방식입니다.

<!-- DEMO VIDEO PLACEHOLDER -->
[DEMO VIDEO: 바이브 코딩 실습 (3분)]

---

## 요약

| 도구 분야 | 대표 서비스 | 핵심 기능 |
|-----------|------------|----------|
| 이미지 | Midjourney, Driimina | 고품질 이미지 생성 |
| 음성 | ElevenLabs | 자연스러운 음성 합성 |
| 영상 | Veo 3 | 영상 생성 |
| 음악 | SUNO AI | 음악 생성 |
| 검색 | Perplexity | 출처 기반 검색 |
| 요약 | Kome | 텍스트/영상 요약 |
| RAG | NotebookLM | 개인 문서 Q&A |
| PPT | Gamma | 프레젠테이션 생성 |
| 코딩 | Lovable, Cursor | AI 보조 코딩 |

---

## 다음: 연습 문제

배운 내용을 연습해봅시다.

→ [연습 문제 풀기](../exercises.md)

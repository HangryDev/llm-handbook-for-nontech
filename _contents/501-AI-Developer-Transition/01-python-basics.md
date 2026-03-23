# 1. 파이썬 기초: '디버깅을 위한' 공부

## 개요

AI 개발을 위한 Python 기초를 배웁니다.

---

## 1.1 왜 Python인가?

- AI/ML 표준 언어
- 풍부한 라이브러리
- 간결한 문법

---

## 1.2 기본 문법

### 변수와 자료형

```python
# 변수
name = "Claude"
age = 3
is_ai = True

# 자료형
text = "Hello"          # 문자열
number = 42             # 정수
pi = 3.14               # 실수
items = [1, 2, 3]       # 리스트
person = {"name": "HK"} # 딕셔너리
```

### 조건문

```python
if age >= 18:
    print("성인")
else:
    print("미성년자")
```

### 반복문

```python
# for문
for i in range(5):
    print(i)

# while문
count = 0
while count < 5:
    print(count)
    count += 1
```

### 함수

```python
def greet(name):
    return f"Hello, {name}!"

result = greet("World")
print(result)  # Hello, World!
```

---

## 1.3 에러 코드 읽기

### 주요 에러 타입

| 에러 | 설명 | 해결 방법 |
|------|------|-----------|
| SyntaxError | 문법 오류 | 코드 수정 |
| NameError | 정의되지 않은 변수 | 변수 확인 |
| TypeError | 타입 불일치 | 타입 변환 |
| IndexError | 인덱스 초과 | 범위 확인 |
| KeyError | 딕셔너리 키 없음 | 키 확인 |

<!-- DEMO VIDEO PLACEHOLDER -->
[DEMO VIDEO: 에러 디버깅 실습 (3분)]

### 에러 읽는 방법

```python
# 에러 메시지 예시
Traceback (most recent call last):
  File "script.py", line 5, in <module>
    print(items[10])
IndexError: list index out of range

# 분석
1. 에러 위치: script.py, 5번째 줄
2. 에러 타입: IndexError
3. 에러 원인: 리스트 인덱스 초과
```

---

## 1.4 디버깅 방법

### print 디버깅

```python
def calculate(x, y):
    print(f"입력: x={x}, y={y}")  # 중간 확인
    result = x + y
    print(f"결과: {result}")       # 결과 확인
    return result
```

### 디버거 사용

```python
import pdb

def buggy_function(x):
    pdb.set_trace()  # 중단점
    result = x / 0   # 에러 발생
    return result
```

---

## 요약

- **변수**: name, age, is_ai
- **자료형**: 문자열, 정수, 실수, 리스트, 딕셔너리
- **제어문**: if, for, while
- **함수**: def
- **에러 타입**: SyntaxError, NameError, TypeError, IndexError, KeyError

---

## 다음: Vibe Coding

AI 코딩 도구를 활용해봅시다.

→ [다음 섹션으로](../02-vibe-coding.md)

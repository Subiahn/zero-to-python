# 📝 Python 기초 문법 정리

> 학습 기간: 2026년 2월 | 프로젝트: [budget_cli](./budget_cli/) · [lotto](./lotto/) · [number_game](./number_game/) · [vocabulary](./vocabulary/)

---

## 1. 변수와 자료형

```python
name = "김파이썬"       # str
age = 25               # int
score = 98.5           # float
is_student = True      # bool

# f-string 출력
print(f"이름: {name}, 나이: {age}세")

# 타입 변환
int("42")    # → 42
str(42)      # → "42"
float("3.14") # → 3.14
```

---

## 2. 리스트 (List)

```python
fruits = ["사과", "바나나", "포도"]

fruits[0]       # 사과 (첫 번째)
fruits[-1]      # 포도 (마지막)
fruits[0:2]     # ["사과", "바나나"] (슬라이싱)

fruits.append("망고")   # 추가
fruits.remove("사과")   # 삭제
len(fruits)             # 길이

# 리스트 컴프리헨션
squares = [x**2 for x in range(1, 6)]  # [1, 4, 9, 16, 25]
```

---

## 3. 딕셔너리 (Dictionary)

```python
student = {
    "name": "김파이썬",
    "age": 25,
    "scores": [90, 85, 95]
}

student["name"]          # 김파이썬
student.get("age")       # 25 (안전한 접근)
student["grade"] = "A"   # 새 키 추가

student.keys()           # 키 목록
student.values()         # 값 목록
```

---

## 4. 조건문

```python
score = 78

if score >= 90:
    print("A 학점")
elif score >= 70:
    print("C 학점")   # ← 실행됨
else:
    print("D 이하")

# 한 줄 조건문
status = "합격" if score >= 60 else "불합격"
```

---

## 5. 반복문

```python
# for 루프
for fruit in fruits:
    print(fruit)

# range
for i in range(5):      # 0, 1, 2, 3, 4
    print(i)

# enumerate (인덱스 + 값)
for idx, fruit in enumerate(fruits):
    print(f"{idx}: {fruit}")

# while
count = 0
while count < 3:
    print(count)
    count += 1
```

---

## 6. 함수

```python
# 기본 함수
def greet(name):
    return f"안녕하세요, {name}님!"

# 기본값 매개변수
def power(base, exp=2):
    return base ** exp

power(3)      # 9
power(2, 10)  # 1024

# 여러 값 반환
def stats(nums):
    return min(nums), max(nums), sum(nums) / len(nums)

lo, hi, avg = stats([10, 20, 30])

# lambda
double = lambda x: x * 2
list(map(double, [1, 2, 3]))  # [2, 4, 6]
```

---

## 7. 파일 I/O & 예외처리

```python
import json
import os

# 파일 쓰기
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# 파일 읽기
if os.path.exists("data.json"):
    with open("data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

# 예외처리
try:
    amount = int(input("금액: "))
except ValueError:
    print("숫자만 입력해주세요!")
finally:
    print("항상 실행됨")
```

---

## 8. random 모듈

```python
import random

# 정수 하나 랜덤 추출 (1~100 사이)
random.randint(1, 100)        # 예: 42

# 리스트에서 중복 없이 k개 추출
numbers = list(range(1, 46))
random.sample(numbers, 6)     # 예: [3, 12, 24, 31, 38, 45]

# 리스트에서 랜덤하게 하나 선택
items = ["사과", "바나나", "포도"]
random.choice(items)          # 예: "바나나"
```

---

## 9. 리스트 심화 — append vs extend

```python
# append: 항목 하나 추가
a = [1, 2, 3]
a.append([4, 5])    # [1, 2, 3, [4, 5]]  ← 리스트가 통째로 들어감

# extend: 여러 항목을 풀어서 추가
b = [1, 2, 3]
b.extend([4, 5])    # [1, 2, 3, 4, 5]  ← 각각 들어감

# 파일 불러올 때 extend 쓰는 이유
data = json.load(f)
vocabulary.extend(data)  # 기존 목록에 불러온 데이터 이어붙이기
```

---

## 10. 자주 쓰는 내장 함수

| 함수            | 설명                  | 예시                        |
| --------------- | --------------------- | --------------------------- |
| `len()`         | 길이                  | `len([1,2,3])` → 3          |
| `range()`       | 숫자 범위             | `range(0, 5)`               |
| `sum()`         | 합계                  | `sum([1,2,3])` → 6          |
| `min() / max()` | 최솟/최댓값           | `max([1,2,3])` → 3          |
| `sorted()`      | 정렬된 새 리스트 반환 | `sorted([3,1,2])` → [1,2,3] |
| `int() / str()` | 타입 변환             | `int("42")` → 42            |
| `enumerate()`   | 인덱스+값             | `enumerate(list)`           |
| `map()`         | 일괄 변환             | `map(func, list)`           |
| `type()`        | 타입 확인             | `type(42)` → int            |

---

## 🔗 실습 프로젝트

- [가계부 CLI 앱](./budget_cli/) — 변수, 딕셔너리, 함수, 파일 I/O
- [로또 번호 생성기](./lotto/) — random, 리스트 컴프리헨션, sorted
- [숫자 맞추기 게임](./number_game/) — random, while, 조건문
- [단어장 앱](./vocabulary/) — 딕셔너리 심화, random.choice, extend

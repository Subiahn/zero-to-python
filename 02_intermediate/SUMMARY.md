# 📝 Python 클래스 (OOP) 정리

> 학습 기간: 2026년 2월 | 프로젝트: [budget_refactoring_1](./budget_refactoring_1/) · [budget_refactoring_2](./budget_refactoring_2/)

---

## 1. 클래스 기본 구조

```python
class BudgetApp:
    def __init__(self):
        self.transacrions = []  # 인스턴스 변수 — 객체마다 독립적

    def add_income(self, amount, memo):
        self.transacrions.append({"type": "수입", "amount": amount, "memo": memo})

    def show_summary(self):
        income = sum(r['amount'] for r in self.transacrions if r["type"] == "수입")
        print(f"수입: {income}")

# 사용
app = BudgetApp()       # 객체(인스턴스) 생성
app.add_income(50000, "알바비")
app.show_summary()
```

---

## 2. `__init__` — 초기 세팅

```python
class BudgetApp:
    def __init__(self):
        self.transacrions = []  # 객체 생성 시 자동 실행
```

- 객체가 만들어질 때 **딱 한 번** 자동 실행됨
- 초기 변수들을 여기서 정의

---

## 3. `self` — 나 자신

```python
class BudgetApp:
    def add_income(self, amount, memo):
        self.transacrions.append(...)  # self = 이 객체 자신
```

- 클래스 안에서 자기 변수/메서드에 접근할 때 항상 붙임
- 클래스 안의 모든 메서드 첫 번째 파라미터는 반드시 `self`

---

## 4. 클래스 변수 vs 인스턴스 변수

```python
class BudgetApp:
    count = 0           # 클래스 변수 — 모든 객체가 공유

    def __init__(self):
        self.transacrions = []  # 인스턴스 변수 — 객체마다 독립

        BudgetApp.count += 1    # 앱이 만들어질 때마다 카운트 +1

app1 = BudgetApp()
app2 = BudgetApp()

print(BudgetApp.count)   # 2 — 두 개 만들었으니까
print(app1.transacrions) # [] — app1 것만
print(app2.transacrions) # [] — app2 것만
```

| 구분          | 선언 위치                  | 공유 여부        |
| ------------- | -------------------------- | ---------------- |
| 클래스 변수   | 클래스 바로 아래           | 모든 객체가 공유 |
| 인스턴스 변수 | `__init__` 안에 `self.` 로 | 객체마다 독립    |

---

## 5. 상속 (Inheritance)

```python
class FamilyBudgetApp(BudgetApp):   # BudgetApp 을 상속
    def __init__(self, owner):
        super().__init__()           # 부모의 __init__ 실행
        self.owner = owner           # 추가 변수

    def owner_show(self):
        print(f'[{self.owner}의 가계부]')
        super().show_summary()       # 부모 메서드 호출
        super().show_all()

app = FamilyBudgetApp("김철수")
app.add_income(50000, "알바비")     # 부모 메서드 그대로 사용 가능
app.owner_show()                    # 자식 메서드 사용
```

---

## 6. `super()` — 부모 클래스 호출

```python
super().__init__()       # 부모의 __init__ 실행
super().show_summary()   # 부모의 show_summary 실행
```

- `super()` 는 **부모 클래스**를 가리킴
- 부모의 기능을 유지하면서 자식에서 추가/변경할 때 사용

---

## 7. 오버라이딩 (Overriding)

```python
class FamilyBudgetApp(BudgetApp):
    def show_summary(self):              # 부모 메서드를 덮어씀
        print(f"[{self.owner}의 가계부]")
        super().show_summary()           # 부모 것도 함께 실행
```

- 부모 메서드와 **같은 이름**으로 자식에서 재정의
- `super()` 로 부모 것도 함께 실행 가능

---

## 8. 인스턴스 — 객체 찍어내기

```python
app1 = BudgetApp()   # 영어 가계부
app2 = BudgetApp()   # 일본어 가계부

app1.add_income(50000, "알바비")
app2.add_income(30000, "아르바이트")

# app1 이랑 app2 는 완전히 독립적
```

- 클래스 = 붕어빵 틀
- 인스턴스 = 찍어낸 붕어빵
- 각 인스턴스는 자기만의 데이터를 가짐

---


## 9. 모듈 (Module)
```python
# budget.py — 클래스 정의만
class BudgetApp:
    ...

if __name__ == "__main__":  # 직접 실행할 때만 동작
    app = BudgetApp()
```
```python
# main.py — import 해서 사용
from budget import FamilyBudgetApp

app = FamilyBudgetApp("김철수")
app.add_income(50000, "알바비")
```

- 파이썬 파일 하나 = 모듈 하나
- 클래스 정의와 실행 코드를 분리
- `if __name__ == "__main__"` — 직접 실행할 때만 동작, import 시엔 무시됨

### import 방법
```python
import budget                     # 모듈 전체
from budget import FamilyBudgetApp  # 특정 클래스만 (가장 많이 씀)
import budget as b                # 별명 붙이기
```



## 🔗 실습 프로젝트

- [가계부 클래스 리팩토링](./budget_refactoring_1/) — `__init__`, `self`, 메서드
- [가계부 상속](./budget_refactoring_2/) — 상속, `super()`, 오버라이딩
- [가계부 모듈 분리](./budget_modules/) — 모듈, `import`, `if __name__`
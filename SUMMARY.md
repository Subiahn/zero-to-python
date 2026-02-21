
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


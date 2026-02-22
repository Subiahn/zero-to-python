

class BudgetApp:
    def __init__(self) -> None:
        self.transacrions = [] # 거래 내역 리스트

    def add_income(self, amount: int, memo: str) -> None:
        self.transacrions.append({"type": "수입", "amount": amount, "memo": memo})


    def add_expense(self, amount: int, memo: str) -> None:
        self.transacrions.append({"type": "지출", "amount": amount, "memo": memo})

    def show_summary(self) -> None:
        income = sum(r['amount'] for r in self.transacrions if r["type"] == "수입")
        expense = sum(r['amount'] for r in self.transacrions if r["type"] == "지출")
        print(f"수입: {income}, 지출: {expense}, 잔액: {income - expense}")

    def show_all(self) -> None:
        for t in self.transacrions:
            print(f"{t['type']} | {t['memo']} | {t['amount']}원")

    # 여기 아래에 추가
    def income_transactions(self):
        for t in self.transacrions:
            if t["type"] == "수입":
                yield t

app = BudgetApp()

# 예제 코드
app.add_income(50000, "알바비")
app.add_income(30000, "용돈")
app.add_expense(12000, "점심")
app.add_expense(3500, "커피")
app.show_all()
app.show_summary()

# 여기 추가
print("\n[제너레이터 테스트]")
for t in app.income_transactions():
    print(t)
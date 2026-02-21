class BudgetApp:
    def __init__(self):
        self.transacrions = []

    def add_income(self, amount, memo):
        self.transacrions.append({"type": "수입", "amount": amount, "memo": memo})

    def add_expense(self, amount, memo):
        self.transacrions.append({"type": "지출", "amount": amount, "memo": memo})

    def show_summary(self):
        income = sum(r['amount'] for r in self.transacrions if r["type"] == "수입")
        expense = sum(r['amount'] for r in self.transacrions if r["type"] == "지출")
        print(f"수입: {income}, 지출: {expense}, 잔액: {income - expense}")

    def show_all(self):
        for t in self.transacrions:
            print(f"{t['type']} | {t['memo']} | {t['amount']}원")


class FamilyBudgetApp(BudgetApp):
    def __init__(self, owner):
        super().__init__()
        self.owner = owner

    def owner_show(self):
        print(f'[{self.owner}의 가계부]')
        super().show_summary()


if __name__ == "__main__":
    app = FamilyBudgetApp("테스트")
    app.add_income(50000, "알바비")
    app.owner_show()

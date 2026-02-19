import json
import os
from datetime import datetime

transacrions = []



class BudgetApp:
    def __init__(self):
        self.transacrions = [] # 거래 내역 리스트

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

app = BudgetApp()

# 예제 코드
app.add_income(50000, "알바비")
app.add_income(30000, "용돈")
app.add_expense(12000, "점심")
app.add_expense(3500, "커피")
app.show_all()
app.show_summary()

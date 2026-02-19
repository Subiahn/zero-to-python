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


class FamilyBudgetApp(BudgetApp): #BudgetApp 상속
    def __init__(self, owner):
        super().__init__()     # 부모의 __init__ 실행 (transacrions 세팅)
        self.owner = owner     # 소유자 이름 설정을 추가 함
        # `super()` 는 **"부모 클래스"** 를 가리킴
    
    def owner_show(self):
        print(f'[{self.owner}의 가계부]')
        super().show_summary()

app = FamilyBudgetApp("김철수")
# 예제 코드
app.add_income(50000, "알바비")
app.add_income(30000, "용돈")
app.add_expense(12000, "점심")
app.add_expense(3500, "커피")
app.owner_show()
app.show_all()
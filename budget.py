import json
import os
from datetime import datetime

transacrions = []

def add_transaction():
    memo = input ("메모: ")
    type_ = input("수입(i) / 지출(o): ")
    amount = int(input("금액: "))
    date = datetime.now().strftime("%Y-%m-%d")
    transacrions.append({
        "date": date,
        "type": type_,
        "memo": memo ,
        "amount": amount
    })
    print("추가 되었습니다!")


def show_all():
    for t in transacrions:
        print(f"{t['date']} | {t['type']} | {t['memo']} | {t['amount']}원")


def get_summary():
    income = sum(t['amount'] for t in transacrions if t['type'] == 'i')
    expense = sum(t['amount'] for t in transacrions if t['type'] == 'o')
    print(f"\n 수입: {income} 원")
    print(f"\n 지출: {expense}원")
    print(f"\n 잔액: {income - expense}원")


def save_to_file():
    with open("budget.json", "w", encoding="utf-8") as f:
        json.dump(transacrions, f, ensure_ascii=False, indent=2)
    print("저장 되었습니다.")


def load_from_file():
    if os.path.exists("budget.json"):
        with open("budget.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            transacrions.extend(data)
        print("불러왔습니다.")
# 메인 루프

load_from_file() # 프로그램 시작시 불러오기

while True:
    print("\n1. 추가 2. 목록 3. 요약 4. 종료")
    choice = input("선택: ")
    
    if choice == "1":
        add_transaction()
    elif choice =="2":
        show_all()
    elif choice == "3":
        get_summary()
    elif choice =="4":
        save_to_file()
        break


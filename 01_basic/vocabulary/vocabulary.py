import json
import os
import random
vocabularys = []

def add_vocabularys():
    word = input("단어: ")
    meaning = input("뜻: ")
    vocabularys.append({
        "word": word,
        "meaning": meaning
    })

def show_list():
    for t in vocabularys:
        print(f"{t['word']} | {t['meaning']}")


def save_to_file():
    with open("vocabulary.json", "w", encoding="utf-8") as f:
        json.dump(vocabularys, f, ensure_ascii=False, indent=2)
    print("저장 되었습니다.")


def load_from_file():
    if os.path.exists("vocabulary.json"):
        with open("vocabulary.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            vocabularys.extend(data)
        print("불러왔습니다.")


def quiz():
    item = random.choice(vocabularys)
    answer = input(f"{item['word']}의 뜻은? \n")
    if answer == item['meaning']:
        print("정답")
    else:
        print(f"오답! 정답은 {item['meaning']}")

load_from_file() # 프로그램 시작시 불러오기

while True:
    print("\n1. 단어 추가 2. 단어 목록 3. 퀴즈 4. 종료")
    choice = input("선택: ")
    if choice == "1":
        add_vocabularys()
    elif choice =="2":
        show_list()
    elif choice == "3":
        quiz()
    elif choice == "4":
        save_to_file()
        break
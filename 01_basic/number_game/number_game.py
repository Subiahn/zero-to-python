import random

answer = random.randint(1, 100)
print("1 ~ 100 사이의 숫자 중 정답을 맟춰 주세요.")

tries = 0 

while True:
    user_answer = int(input("답을 입력 하세요."))
    tries += 1
    if user_answer == answer:
        print(f"{user_answer} 정답입니다.")
        print(f"{tries}번 만에 맟췄어요!")
        break
    elif user_answer < answer:
        print(f"{user_answer} 보다 큽니다.")
    elif user_answer > answer:
        print(f"{user_answer} 보다 작습니다.")
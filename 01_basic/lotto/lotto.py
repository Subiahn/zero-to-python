import random
numbers = list(range(1,46))

count = int(input("몇 회차 뽑을까요?"))

for i in range(count):
    result = random.sample(numbers, 6)
    print(f"{i+1}회차: {sorted(result)}")





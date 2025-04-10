import random




count = 0
task = int(input("풀 문제 수를 정해주세요: "))

for n in range(1, 1+task):
    digit = random.randint(2,9)
    digit2 = random.randint(2,9)
    answer = int(input(f"{n}번 문제 : {digit} * {digit2} = "))
    if (answer == digit * digit2):
        print("정답입니다.")
        count+=1
    else:
        print(f"틀렸습니다. 답은 {digit * digit2}")

print(f"맞춘 정답의 갯수는 {count}개")    
start_num = int(input("시작 숫자를 입력해주세요: "))
count = 0

while(start_num != 1):

    if (start_num % 2 == 0):
      start_num = start_num / 2
    else:
     start_num = start_num * 3 + 1
    count +=1
    print(f"변환 중 현재 {start_num}")

print(f"변환 횟수 = {count}")

# 보물상자 암호 맞추기 1~100사이의 숫자 low high 알려줌 횟수 제한 x 맞추면 정답 메세지.
import random
count = 1
password = random.randint(1,100)
# print (password)
answer = 0
while(True):
    answer = int(input(f"비밀번호가 뭘까요? {count} 트 : "))
    if (answer == password):
        print('정답입니다. ㅠㅠ')
        break;

    if (answer > password):
        print('더 낮습니다. ㅋㅋ')

    if (answer < password):
        print('더 높습니다. ㅋㅋ')
    count += 1
# 먹이 m을 주어야함. 2번 이상 먹이를 주지 않으면 떠남. 굶은 날을 카운트 떠나기 전까지의 기간 카운트 


food , give= 0 ,0
day = 1
hungry, total_hungry = 0,0
food = int(input('줘야하는 먹이의 양 : '))

while(True):
    give = int(input(f'먹이를 주세요 {day} 일차 : '))
    if give < food:
        hungry +=1
        total_hungry +=1
    else:
        hungry = 0
    if hungry >=2:
        print('용이 떠났습니다.')
        break
    day +=1

print(f"{day}일 중 용이 굶주린 날은 {total_hungry}일 입니다.")
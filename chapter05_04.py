age = int(input('나이를 입력: '))

if age<19:
    print('집에 갈 시간이네요!')
else :
    print('협조 감사합니다.')



import random

com = random.choice(['가위','바위','보'])

user =input('가위 바위 보 중에 입력: ')

if com == '가위' and user == '가위':
    print ('비겼습니다.')
    if user == '바위':
        print('이겼습니다.')
        if user == '보':
            print('졌습니다.')
elif com == '바위' and user == '가위':
    print('졌습니다.')
    if user == '바위':
        print('비겼습니다.')
        if user == '보':
            print('이겼습니다.')
elif com == '보' and user == '가위':
    print ('이겼습니다.')
    if user == '바위':
        print('졌습니다.')
        if user == '보':
            print('비겼습니다.')

print(f'컴퓨터가 낸 것 : {com}')



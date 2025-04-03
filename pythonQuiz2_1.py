# 일주일 용돈 관리
# 입력 1. 하루 용돈으로 일정 금액으 받음
# 입력 2. 7일간의 지출 금액을 입력
# 출력 : 예산을 초과한 일 수
over_day = 0
daily = int(input('하루 용돈 =>'))
for n in range(1,8):
    paid = int(input(f'{n}일차 지출 금액 =>'))
    if paid > daily:
        over_day +=1

# paid1 = int(input('1일차 지출 금액 =>'))
# paid2 = int(input('2일차 지출 금액 =>'))
# paid3 = int(input('3일차 지출 금액 =>'))
# paid4 = int(input('4일차 지출 금액 =>'))
# paid5 = int(input('5일차 지출 금액 =>'))
# paid6 = int(input('6일차 지출 금액 =>'))
# paid7 = int(input('7일차 지출 금액 =>'))



# if paid1 > daily:
#     over_day +=1
# if paid2 > daily:
#     over_day +=1
# if paid3 > daily:
#     over_day +=1
# if paid4 > daily:
#     over_day +=1
# if paid5 > daily:
#     over_day +=1
# if paid6 > daily:
#     over_day +=1
# if paid7 > daily:
#     over_day +=1

print(f'예산을 초과한 날짜 수는 {over_day}일')
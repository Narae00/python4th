n1 = 200
n1 = n1 + 100
n1 += 100
print(n1)

total = 0
menu = input('구매 또는 판매한 메뉴 : ')
price = int(input('가격(판매 +, 구매 -):'))
count = int(input('갯수 : '))
total += price*count
print(f'{menu} {count}개를 {total}원에 구매했습니다.')
print(f'현재 매출 : {total}원')
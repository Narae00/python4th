
basic = 3000
distance = int(input("거리를 입력하세요.: "))

fee = basic + distance*1000

print(f'요금은{fee}입니다')

tempsup = int(input("섭씨 입력 : "))

temphwa = tempsup*9/5.0 + 32

print(f'화씨로 바꾸면 {temphwa}입니다')

# candy  = int(input("사탕 1개 가격 : "))
# money = int(input("가진 돈 입력 : "))
price_and_budget = input('사탕 가격과 가진 돈을 입력=>')
candy, money = map(int, price_and_budget.split(' ')) #map (int , .split) split이 적용된 문자에 전부 int를 적용하라는 map함수
money = int(money)
candy = int(candy)

count = money//candy
charge = money%candy

print(f'구매개수는 {count}개 남은 돈은 {charge}원')

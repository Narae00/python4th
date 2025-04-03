#ATM 현금 인출  50000, 10000, 5000, 1000원권 최소 지폐 개수 1000원 단위가 아닌 금액일시 다시 입력 요청


count1, count2, count3, count4 = 0 ,0,0,0
money =0
while(money == 0):
    money = int(input('인출할 금액 입력(1000원 단위로만)'))
    if (money%1000 != 0):
        print('올바른 값이 아닙니다. 다시 입력해주세요.')
    else :
        break

    if money > 50000:
        money = money % 50000
        count1 = money/50000
    if money > 10000:
        money = money % 10000
        count2 = money/10000
    if money > 5000:
        money = money % 5000
        count3 = money/5000
    if money > 1000:
        money = money % 1000
        count4 = money/1000

print(f'5만원권 {count1}개, 1만원권 {count2}개, 5000원권 {count3}개, 1000원권 {count4}개')

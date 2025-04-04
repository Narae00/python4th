
total = 0
while(True):
    purchase = int(input("구매한 물품들의 가격을 적어주세요 (다 적었으면 0입력)"))
    if purchase == 0:
        break
    total += purchase

if total >=100000:
    total *= 0.9
elif total >= 50000:
    total *= 0.95

print(f'최종 결제 금액은 {total} 원 입니다.')
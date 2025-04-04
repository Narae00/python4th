# 주유 횟수 계산 이동거리, 만땅 연료시 비거리


goal = int(input('이동할 거리는 : '))
fuel = int(input('연료가 가득 찼을 때 최대 달릴 수 있는 거리는 : '))

count = goal//fuel
if goal%fuel ==0:
    count -=1
print(f'필요한 주유는 {count}번')
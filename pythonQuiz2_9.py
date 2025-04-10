bag = int(input("가방의 무게는 : "))

N = int(input("발견한 아이템 갯 수"))

bag_weight = 0
bag_item_count = 0

for n in range(1, N+1):
    item_weight = int(input(f"{n}번째 아이템 무게 : "))
    if bag_weight + item_weight <= bag:
        bag_weight += item_weight
        bag_item_count +=1
    else:
        print('소지 무게 한도를 초과했습니다.')
        break


print(f'총 담은 아이템 갯수는 : {bag_item_count}')
print(f'남은 용량: {bag-bag_weight}')
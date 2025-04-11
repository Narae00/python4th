my_list = [1,2,'3', 4.2]

print(my_list[1])
for i in range(4):
    my_list[i] = int(input(f'인덱스 {i} => '))

hap = my_list[0] + my_list[1] + my_list[2] + my_list[3]
#hap = 0
#for i in range(4):
#   my_list[i] = int(input(f'인덱스 {i} => '))
#   hap += my_list[i]
print(my_list)
print(f'총합 : {hap}')

a = (100)
print(type(a))

#인덱스(첨자, index)
# 순서가 있는 데이터에서 특정 순서의 데이터를 참조하기 위한 숫자
# 예시 : 순서가 있는 데이터[값]
# 0부터 시작
# 음수 인덱스는 뒤에서부터 순서를 셈
my_list2 = [1,2,'테스트',222]
print(my_list2[2])
print(my_list2[-2])

# 슬라이스(slice)
# 순서가 있는 데이터 [시작인덱스 : 끝인덱스]
# 시작 인덱스 부터 끝 인덱스 전까지
print(my_list2[2:4])
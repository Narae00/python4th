F = int(input("피라미드의 층수 =>"))

#왼쪽 정렬 ver. (2n-1)

for n in range(1, F+1):
    for _ in range(2*n-1):
        print('*', end ='')
    print('')

for n in range(1, F+1):
    print('*'*(2*n-1))

#오른쪽 정렬 ver.
#    * = 공백 4 2*(F - n)
#  *** = 공백 2
#***** = 공백 0

for n in range(1, F+1):
    print('  '*(F-n), end= '')
    print('*'*(2*n-1))

for n in range(1, F+1):
    print(' '*(F-n), end= '')
    print('*'*(2*n-1))
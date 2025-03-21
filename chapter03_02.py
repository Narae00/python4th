# 튜플(tuple)
# => 하나의 정보체에 여러 개의 값을 담아둘 수 있는 자료형 중 하나
# 선언 방식 : (값1, 값2, 값3...)

mytuple = (5,15,25)

print(mytuple)
print(type(mytuple))

#파이썬은 하나의 정보체(변수)가 값울 여러 개 가지고 있을 때
#값의 개수만큼 변수를 제공하면 값을 각각 담아준다.(unpacking)

n1,n2,n3 = mytuple
print(f'n1={n1}, n2={n2}, n3={n3}')

a = 20
b = 50

a,b = b,a
#튜플 (a,b)가 생성
#언패킹으로 각 값을 b와 a에 대입

print(a,b)
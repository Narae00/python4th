#함수의 정의
# def 함수이름(매개변수1, 매개변수2....):
#    코드1
#    코드2
#    '''
# return 반환값

# 함수의 사용(호출, call)
# 함수이름(인자1, 인자2, ...) -반환값이 없는 경우
# 변수 = 함수이름(인자1,인자2...) - 반환값이 있는 경우

#매개변수(parameters, params)
# -> 함수의 정의에서 함수의 실행을 위해 전달 받아야 하는
# 정보를 담기 위한 변수들

# 인자 또는 인수(arguments, args)
# -> 함수를 호출할 때 실제로 전달 되는 정보 (값, 변수 등)

# 1. 매개변수 X, 반환값 X
# - 완전 수동적인 역할, 거의 안씀. 코드의 모듈화에 사용
# 전체 처리 코드가 1000줄
# def 처리1()
# def 처리2()...
def func1():
    print('안녕하세요~')
    print('func1 호출됨!')

func1()


#2. 매개변수 1개, 반환값 X

def func2(a):
    res = a + 10
    print(f'{a} + 10 = {res}')
    print('func2 호출됨!')

func2(22)

#3. 매개변수 3개, 반환값 X

def func3(a, b, c):
    res1 = a+b
    res2 = a-c
    print(f'{a} + {b} = {res1}')
    print(f'{a} - {c} = {res2}')

func3(15,3,8)
func3(20,10,6)

#부록 1. 매개변수의 기본값(default values)
#       매개변수에는 기본값을 설정할 수 있다!
#       기본값은 인자가 전달 되지 않았을 때 사용할 값
#       (주의) 기본값이 있는 매개변수는 기본값이 없는 매개변수보다 뒤에 있어야함.

def func4(a, b = 50, c = 99):
    res1 = a+b
    res2 = a-c
    print(f'{a} + {b} = {res1}')
    print(f'{a} - {c} = {res2}')

func4(10, 3)
func4(10)

# 4. 매개변수 X, 반환값 O
# 반환값은 return을 이용해서 지정

def func5():
    return 3.141592

mypi = func5()
print(f'mypi : {mypi}')

#부록2. return 에 대해서...
# 2-1. # 모든 프로그래밍 언어에서 함수는 하나의 정보만 반환 가능
# 그러나 파이썬은 튜플의 잠재적 문법으로 인해
# 콤마로 정보를 나열하여 여러 개의 반환값을 지원하는 것 처럼 보여질 수 있다.
def func8(a,b,c):
    res1 = a+b
    res2 = a-c
    return res1, res2
# , 는 튜플로 묶어서 전달한다는 의미

# 2.2 return이 실행되면 함수는 즉시 종료
def func9(c):
    if c== 'A':
        print('대문자 A 입력!!!')
        return
    print(f'입력된 문자 : {c}')
func9('A')

# 5. 매개변수 O , 반환값 O
def func10(r): #반지름 r이 주어졌을 때 원의 넓이를 반환
    return r **2*func5()

r = 7
area = func10(r)
print(f'반지름 {r}인 원의 넓이는 {area}입니다.')

# 전역변수(Gloval Variables)
# 지역변수(Local Variables)
# 과제 : 함수 내에서 b값을 99로 수정했는데 왜 호출 이후에 값이 5로 되돌아 왔을까?

b= 5 #들여쓰기 없이 선언된 변수 = > 전역변수

def func11(a):
    c = 10
    b = 99
    print(f'func11-b : {b}')
    return a+b+c
print(func11(8))
print(f'global b: {b}')
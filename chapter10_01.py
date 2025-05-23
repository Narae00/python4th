#객체지향 프로그래밍에서 클래스에 관한 코드를 작성할 때
#1. 객체의 속성(변수) 값을 클래스 외부에서 변경하는 것을 안좋아함(은닉성)

#Rabbit 클래스 정의
class Rabbit:
    shape = ''
    xPos = 0
    yPos = 0

    def goto(self,x,y):
        self.xPos = x
        self.yPos = y

    def __init__(self,shape, x=0, y=0): #생성자 - 초기 상태 값을 결정하는 용도
        print('생성자 호출됨!')
        self.shape = shape
        self.xPos = x
        self.yPos = y
    
    def setShape(self, shape):
        self.shape = shape

    
    def __del__(self):
        print(f'{self.setShape} 토끼는 스태프가 맛있게 먹었습니다.')


rabbitA = Rabbit('빨강')

print(f'Rabiit A - 모양: {rabbitA.shape},\
      x 위치 : {rabbitA.xPos}, y 위치 : {rabbitA.yPos}')

rabbitB = Rabbit('노랑',50,25)

print(f'Rabiit B - 모양: {rabbitB.shape},\
      x 위치 : {rabbitB.xPos}, y 위치 : {rabbitB.yPos}')


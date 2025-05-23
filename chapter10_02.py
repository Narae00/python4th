#Line 클래스 속성: 길이 메소드: 더하기 - 두선의 길이의 합,  비교 - 짧은 선을 삭제


class Line:
    def __init__(self,length):
        self.length = length
        print(f'길이 {self.length}인 선이 만들어 졌습니다.')
    xLen = 0
    yLen = 0

#짧은 선을 삭제
#other에는 line 인스턴스가 전달된다고 가정정
    def compare(self,other):
        if (self.length < other.length):
            print(f'길이가 {self.length}인 선이 작다.')
        elif self.length > other.length:
            print(f'길이가 {other.length}인 선이 작다.')
        else:
            print('두 선의 길이가 같습니다.')

    def __add__(self,other):
        return self.length + other.length
    


line_a = Line(10)
line_b = Line(5)
print(f'line_a + line_b = {line_a + line_b}')
line_a.compare(line_b)

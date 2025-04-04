students = int(input('학생 수 입력 : '))

for i in range(1,students+1):
    score = int(input(f'{i}번 학생의 점수 입력 : '))
    if score >=90:
        print(f'{i}번 학생의 성적은 A등급')
    elif score >=80:
        print(f'{i}번 학생의 성적은 B등급')
    elif score >=70:
        print(f'{i}번 학생의 성적은 C등급')
    elif score >=60:
        print(f'{i}번 학생의 성적은 D등급')    
    else:
        print(f'{i}번 학생의 성적은 F등급')
    
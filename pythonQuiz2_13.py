#초과 근무 수당 계산

#주 40시간까지는일반시급을적용, 40시간을초과한부분은시급의 1.5배로지급. 
#직원수 N과 각직원의 주간근무시간과 시급을입력, 직원별주급을계산

N = int(input("직원 수 => "))
for e in range(1, N+1):
    work_time, salary = map(int, input("주간 근무 시간과 시급을 입력(공백 구분) => ").split())
    #60 10000

    normal = min(work_time,40) * salary
    over = max(work_time -40, 0) *salary * 1.5
    total = normal + over

    print(f"{e}번 직원의 주급은 {total:.0f}원 입니다.")

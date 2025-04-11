# 5명의 심사위원
# 점수의 평균

scores = []

#평균 : 총합 / 심사위원 수
for i in range(5):
    scores.append(int(input(f"[{i+1}] 점수 입력 = > ")))

print(f'평균 점수 : {sum(scores)/len(scores) : .2f}')
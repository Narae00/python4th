emp_dict = {} # 정보가 없는 딕셔너리
emp_dict = {'사번' : 1000, '이름' : '홍길동', '부서': '케이팝'}


#데이터의 접근 - 딕셔너리[키]
print(emp_dict['사번'])
print(emp_dict['부서'])

#딕셔너리가 갖고 있는 키를 전부 알고 싶을 때
print(emp_dict.keys())
print(type(emp_dict.keys()))
for k in emp_dict.keys():
    print(k)

#딕셔너리가 갖고 잇는 값만 전부 알고 싶을 때
print(list(emp_dict.values()))

#딕셔너리에 새로운 아이템을 추가하는 방법
emp_dict['전화번호'] = '010-1234-5678'

#딕셔너리의 특정 아이템 값을 변경하고 싶을 때
emp_dict['부서'] = '재즈'
print(emp_dict)

#키를 이용해서 item을 제거하고 싶을 때
emp_dict.pop('부서')
print(emp_dict)

print('사번')
password =[]

while(True):
    password = input('만들 비밀번호를 입력해주세요.(단, 8자 이상 숫자와 영문자가 하나 이상 포함되어야 합니다. : )')

# import re  # 정규 표현식 사용

# while True:
#     password = input("만들 비밀번호를 입력해주세요 (8자 이상, 숫자와 영문자 포함): ")

#     # 비밀번호 조건 확인
#     if len(password) < 8:
#         print(" 비밀번호는 최소 8자 이상이어야 합니다.")
#         continue

#     if not re.search(r"[A-Za-z]", password):  # 영문자가 있는지 확인
#         print(" 비밀번호에 최소 하나의 영문자가 포함되어야 합니다.")
#         continue

#     if not re.search(r"[0-9]", password):  # 숫자가 있는지 확인
#         print(" 비밀번호에 최소 하나의 숫자가 포함되어야 합니다.")
#         continue
# char.isalpha char.isdigit
#     print(" 비밀번호가 설정되었습니다!")
#     break  # 조건 만족하면 반복문 종료

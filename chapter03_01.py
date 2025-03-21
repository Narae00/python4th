# 1lb = 0.453592kg
# 1kg = 2.204623lb
# 파운드 -> kg 변환
# kg -> 파운드 변환


lb_to_kg = 0.453592
kg_to_lb = 2.204623

#문자열(string, str) => ''또는 ""
#f-string 표현 방식 => f''또는 f""
input_lb = float(input('파운드(lb)를 입력'))
print(input_lb, "파운드(lb)는", input_lb*lb_to_kg, "kg입니다." )
print(f'{input_lb} 파운드(lb)는 {input_lb*lb_to_kg:.02f} kg입니다.' )

input_kg = float(input('킬로그램(kg)를 입력'))
print(input_kg, "파운드(lb)는", input_kg*kg_to_lb, "lb입니다." )
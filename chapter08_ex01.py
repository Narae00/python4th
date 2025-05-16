import os


hp_time = {'내과':['09:00','10:00','11:00'],'외과':['13:00','14:00','15:00'],
            '소아과':['10:00','11:00','12:00'],'정형외과':['14:00','15:00','16:00']}

hp_guests = {'내과':[0,0,0],'외과':[0,0,0],
            '소아과':[0,0,0],'정형외과':[0,0,0]}

hp_bookings = [{'이름':'김철수', '진료 과목': '외과', '진료 시간': '14:00'},
               {'이름':'김나래', '진료 과목': '외과', '진료 시간': '14:00'},
               {'이름':'이나래', '진료 과목': '외과', '진료 시간': '14:00'}]

def start_reservation():
    # 이름, 과목, 희망 ㅣ간대
    name = input('이름 : ')
    print('[ 진료 과목 ]')
    for idx, p in enumerate(hp_time.keys()):
        print(f'[{idx+1}] {p}')
    part_idx = int(input('진료 과목을 선택 하세요 : '))
    part_idx -=1
    part = list(hp_time.keys())[part_idx]


    time_table = hp_time[part]
    print('[ 진료 시간 ]')
    for idx, t in enumerate(time_table):
        print(f'[{idx+1}] {t} {'(마감)' if get_guest_count(part,t) == 3 else ''}')
    time_idx = int(input('진료 시간을 선택 하세요 : '))
    time_idx -=1
    time = time_table[time_idx]

    print(f'이름 : {name} 진료과목 : {part} 진료시간 : {time}')

    if get_guest_count(part,time) < 3:
        hp_bookings.append({'이름':name, '진료 과목': part, '진료 시간': time})
        print(f'[예약 완료] 이름: {name} 진료 과목 : {part} 진료시간 : {time}')

    else:
        print('[거부] 해당 시간에는 예약이 가득 찼습니다.')
    # 해당 진료 시간에는 3명까지만 예약이 가능
    # name : 이름
    # part : 진료 과목
    # time_idx : 진료 시간 인덱스
    # time : 진료 시간

def get_guest_count(part, time): # 과목과 시간대에 몇 명 예약했는지 반환
    count = 0
    for guest in hp_bookings:
        if guest['진료 과목'] == part and guest ['진료 시간'] == time:
            count +=1
    return count

def check_reservation():
    print(f'=========== 예약 정보({len(hp_bookings)}명)) =======')
    for b in hp_bookings:
        print(b)



while True:
    print('[1] 예약하기')
    print('[2] 예약 현황 출력')
    print('[3] 종료')
    
    choice = int(input('기능을 선택하세요 =>'))
    os.system("cls") #실행 쉘 내용 제거
    #예약 기능
    if choice ==1:
        print('예약 기능 선택')
        start_reservation()
    
    elif choice == 2:
        print('예약 현황 출력 선택')
        check_reservation()
    elif choice == 3:
        print('종료합니다.')
        break

# 각 시간대별로 최대 3명의 환자만 예약
# 사용자로부터 환자의 이름, 진료 과목, 희망 시간대를 입력 받습니다.

# 예약 기능(이름,과목,희망 시간대)
# 예약 가능 여부 판단
# 모든 예약 현황을 출력


    
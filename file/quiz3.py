# 문자를 계속 입력 받다가 0이 들어오면 종료하세요
# 예) 'aaa' -> 계속
# 예) 'bbb' -> 계속
# 예) '11' -> 계속
# 예) '0' -> 종료

# 반복문 for while
# for : list tuple range 등 데이터 개수만큼 반복 -> 반복횟수가 명확
# while : 조건이 참인 동안 반복 -> 반복횟수가 모호

while True:
    text = input('입력: ')
    if text == '0':
        break

    

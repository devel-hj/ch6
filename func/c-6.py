# 사람의 정보를 출력하는 함수 만들기
# 매개변수: 이름, 나이, 성별
# 초기값이 있는 매개변수는 항상 맨뒤에 배치해야됨
def info(name, age, gender='m' ):
    print(f'나의 이름은 {name}입니다')
    print(f'나이는 {age}살 입니다')
    if gender == 'm':
        print('남자')
    else:
        print('여자')

# 함수 호출
info('도우너', 8) # 성별 모름, gender의 초기값을 사용해서 '남자'
info('둘리', 10, 'f') # 입력값 그대로 '여자'
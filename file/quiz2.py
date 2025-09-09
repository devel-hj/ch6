# 시험 점수를 입력 받아 합격여부를 출력하세요
# 60점 이상 : 합격
# 60점 미만 : 불합격
quiz = input('시험 점수: ')
quiz = int(quiz)

if quiz >= 60 :
    print('합격')
else :
    print('불합격')

# 학생의 나이를 입력 받아 버스 요금을 계산하세요
# 어린이(0~12세) : 1000원
# 청소년(13~18세) : 1500원
# 성인(19세 이상) : 2000원

age = input('나이 입력: ')
age = int(age)

if 0 < age <= 12 :
    print('1000원')
elif 13 < age <=18 : 
    print('1500원')
else :
    print('2000원')


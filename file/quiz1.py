# 두 숫자를 입력받아 곱셈 결과를 출력하세요
# 예) 5,10 => 50
mul_1 = input('첫번쨰 숫자: ')
mul_2 = input('두번쨰 숫자: ')

sum = int(mul_1) * int(mul_2)
print(sum)


# 사용자로부터 이름과 나이를 입력받아 자기소개를 출력하세요
# 예) 둘리, 7 => '둘리님의 나이는 7세입니다'
user_name = input('이름 입력: ')
user_age = input('나이 입력: ')
user_age = int(user_age)

print(f'{user_name}님의 나이는 {user_age}세입니다')

# 사과 가격과 수량을 입력 받아 총 가격 계산하세요
# 예) 사과가격: 1500, 사과개수: 5 => 7500원
ap = input('사과 가격 입력: ')
ap = int(ap)
ap_cnt = input('사과 개수 입력: ')
ap_cnt = int(ap_cnt)

total = ap * ap_cnt
print('사과 가격:',total)
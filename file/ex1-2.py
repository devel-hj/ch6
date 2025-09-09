# 숫자 두개 입력받기
# input함수로 받은 값은 str
n1 = input('첫번째 숫자를 입력하세요: ')
n2 = input('두번째 숫자를 입력하세요: ')
# 두 수의 합 구하기
# 먼저 형변환을 하고 더하기
sum = int(n1) + int(n2) # '3' -> 3  '4' -> 4
print('결과:',sum)

# n1 n2 자료형 확인
print(type(n1),type(n2)) # str


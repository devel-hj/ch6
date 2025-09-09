# 함수 만들기
def func1(a):
    print(a)

# 함수 호출하기
func1(1)

# 값을 두 개 입력받고 호출하는 함수 만들기
def func2(a, b):
    print(a, b)

func2(1, 2)

# 값을 세 개 입력받고 호출하는 함수 만들기
def func3(a, b, c):
    print(a, b, c)

func3(1, 2, 3)


# 매개 변수의 개수가 달라져도 사용할 수 있는 함수 만들기
# 나머지 매개변수
# 나머지 매개 변수를 만들떄는 ** 별 두개
def func4(**kwargs):
    print(kwargs)

# 함수 호출
# 나머지 매개 변수는 딕셔너리 형태로 저장됨
# 따라서 마음대로 데이터를 추가할 수 있음
func4(a=1) # {'a': 1}
func4(a=1, b=2) # {'a': 1, 'b': 2}




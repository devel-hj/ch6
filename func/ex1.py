# 더하기 함수 만들기
# def 함수이름(매개변수): ...
# 매개변수 : 함수에 필요한 입력값 (예를 들어 숫자 2개)
# 반환값 : 결과
def add(a,b):
    return a + b # 반환값

# 함수 사용
sum = add(3,4) # 함수이름(입력값)
print('결과:', sum)





# 두 개의 숫자를 입력받아 곱한 값을 
# 반환하는 함수를 작성하고 호출하세요 
# 예) 2,5 => 10
def mul(a,b):
    return a * b

result = mul(2,5)
print('결과:', result)


# 함수의 여러가지 형태

# 입력값 없고, 반환값도 없는 함수
# 인사를 출력하는 함수 만들기
def hello() : 
    print('안녕하세요')
# 함수 호출
hello()


# 입력값 있고, 리턴값도 있는 함수
# 두 함수를 더하는 함수
def add(a,b):
    return a + b
# 함수를 호출할때, 두 숫자를 입력하고
# 호출이 끝난 후에, 결과를 받아야함
result = add(3,4)


# 입력값 없고, 리턴값만 있는 함수
# 인사를 반환하는 함수
def say():
    return 'hi'
# 리턴값이 있으면 결과를 받아야함
string = say()
print(string)

# 입력값 있고, 반환값은 없는 함수
# 두 수를 더하고 결과를 바로 출력하는 함수
# 매개변수, 입력값, 인자
# 함수를 정의할떄는 a와 b를 '매개변수'라고 부른다
def add(a,b):
    print(a+b)
# 매개변수가 있으면 개수에 맞게 입력
# 함수를 호출할때는 3과 4를 '인자'라고 부른다
add(3,4)





# 이름을 입력받아 환영 인사를 출력하는 함수를 작성하세요
# 예) '둘리'-> '둘리님, 환영합니다!'
def name() :
    return '둘리'

name = name()
print(name+'님, 환영합니다!')

# 이름과 인사말을 받아 '이름 + 인사말' 형태의 문자열을 
# 출력하는 함수를 작성하세요
# 예) '둘리', '안녕하세요' -> '둘리님, 안녕하세요'
# 예) '또치', 'hi~~~' -> '또치님, hi~~~'

def fun(name, msg) :
    # 문자열 연결 방법: + , f-str
    print(f'{name}님,{msg}')

fun('둘리', '안녕하세요')


# 함수 응용하기
# 입력한 숫자만큼 '안녕하세요' 출력하기
def hello(cnt) :
    # 3번 출력하기
    for _ in range(cnt) :
        print('안녕하세요')

# 매개변수가 있으면 입력값을 넣어서 함수를 호출
hello(5)












# 두 개의 숫자를 입력받아, 
# 첫 번째 수에서 두 번쨰 수까지의 합을 반환하는 함수를 작성하세요
# 예) 5,10 => 45

def sum(num1, num2):
    sum = 0
    for n in range(num1, num2 + 1):
       sum = sum + n 

    return sum

r = sum(5, 10)
print(r)

# 두 개의 숫자를 입력받아, 
# 첫번째 수에서 두번째 수를 뺀 결과를 반환하는 함수를 작성하세요
# 단, 첫번째 수가 두번째 수보다 작으면 -999를 반환하세요
# 예) 20,10 -> 10
# 예) 10,20 -> -999

# 함수 이름 : 내 마음대로~ fun sub 등
# 입력값: 숫자 두개
# 반환값: 첫 번째 수에서 두 번째 수를 뺀 결과

# 함수 내부에서 return 키워드 여러번 작성할 수 있지만,
# 함수 내부에서 return을 한번만 만날 수 있다
def sub(n1, n2):
    if n1 < n2 :
        return -999
    else:
        return n1 - n2

# result1 = sub(20,10)
# print(f'결과:{result1}')
result2 = sub(30,20)
print(f'결과:{result2}')


# 블록은 변수의 scrope
a = 10 # 전역 변수
if a%2 == 0 :
    b = 5 # 지역 변수
    print(b)

print(a)

for n in range(10):
    print(n) # 지역 변수

def fun(x,y):
    print(x,y) # 지역 변수

fun(2,3)
# print(x, y) 
# 함수 블록 안에서 선언된 x,y는 지역변수로
# 함수 밖에서는 사용할 수 없다

# 숫자를 입력 받아 짝수인지 홀수인지 알려주는 함수를 만드세요
# 예) 3 -> '홀수'
# 예) 10 -> '짝수'

def a(n):
    if n % 2 == 0 :
        return '짝수'
    else :
        return '홀수'

num1 = a(n)

n = 3
print(num1)

# 값을 하나 입력 받아 타입이 str이면 
# 문자입니다'를 출력하는 함수를 만드세요 
# 타입이 str이 아니면 아무것도 출력되지 않습니다

def tp(x):
    if type(x) == str :
        return '문자입니다'

tp = tp('d')
print(tp)



# 값을 하나 입력 받아 0 보다 크면 
# '양수입니다'를 출력하는 함수를 만드세요
# 예) 10 -> '양수입니다'
# 예) -5 -> x
def dif(num1):
    if 0 < num1 :
        return '양수입니다'
    else :
        pass

ndf = dif(3)
print(ndf)



# 리스트를 입력받아 첫 번째 값을 반환하는 함수를 만드세요
# 예) [10, 20, 30] -> 10
# 예) ['a', 'b', 'c'] -> 'a'


def lis(var) :
    return var[0]

v = lis(['a','b','c'])
print(v)

# 문자열을 입력받아 길이를 반환하는 함수를 만드세요
# 예) 'abc' -> 3
# 예) 'hello' -> 5

def cnt(text):
    return len(text)

cnt = cnt('hello')
print(cnt)

# 아래 코드에서 각 변수에 무엇이 저장되는지 주석을 작성하세요
# 리스트를 입력받아 첫 번째 값을 반환하는 함수 만들기
def func(lis): # lis : 함수의 매개변수로, 함수 내부에 선언됨
    return lis[0]

# my_lis : 함수에 전달하기 위한 리스트로, 메인에 선언됨
my_lis = [10,20,30]
# reslt : 함수의 결과를 저장하기 위한 변수로, 메인에 선언됨
result = func(my_lis) 
print(result)



















# 아래 코드에서 각 변수에 무엇이 저장되는지 주석을 작성하세요

# 문자열을 입력받아 길이를 반환하는 함수 만들기
def func(msg): # msg : 함수의 매개변수
    return len(msg)

# my_str1 : func 함수를 호출할때 입력할 문자열
my_str1 = 'abc' 
my_str2 = 'hello' 

# result1 : func함수의 결과. 'abc'의 길이를 저장할 변수
result1 = func(my_str1)
result2 = func(my_str2)








# 숫자를 입력받아 양수/음수/0을 판별하는 함수를 만드세요
# 예) 5 -> '양수'
# 예) -3 -> '음수'
# 예) 0 -> '0입니다'


def check(n):
    if n > 0:
        return '양수'
    elif n < 0:
        return '음수'
    else:
        return '0입니다'
    
nb = -99999999
number = check(nb)
print(number)


# 리스트를 입력받아 리스트 안의 숫자를 모두 더해
# 합을 반환하는 함수를 만드세요
# 예)[1,2,3,4,5] -> 15
# 예)[10,20,30] -> 60

def fun(lis):
    sum = 0
    for n in lis:
        sum = sum + n
    return sum

my_lis = [10,20,30]
result = fun(my_lis)

print(result)







# 단을 입력 받아 구구단을 출력하는 함수를 만드세요
# 예) 3 ->
# 3 x 1 = 3 
# 3 x 2 = 6
# 3 x 3 = 9 
# 3 x 4 = 12 
# 3 x 5 = 15
# 3 x 6 = 18
# 3 x 7 = 21
# 3 x 8 = 24
# 3 x 9 = 27

def mul(n) :
    for x in range(1, 9 + 1):
        print(f'{n} X {x} = {n*x}')

mul(9)

# 함수를 이용해서 2단부터 9단까지 출력
for i in range(2, 10):
    print(i)
    mul(i)



# 리스트를 입력받아 그 안에 
# 문자열(str) 자료형이 몇 개인지 세는 함수를 만드세요
# 예) [1, 'apple', 3.5, 'banana', 10, 'hi'] -> 3
# 예) ['a', 'b', 'c'] -> 3
# 예) [1, 2, 3] -> 0

def lis(a):
    i = 0
    for n in a:
        if type(n) == str:
            i = i + 1
            continue
    return i

lis1 = ['a', 'b', 'c']
r = lis(lis1)

print(r)
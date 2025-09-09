# 두 수를 더해서 합을 구하는 함수
# 입력된 값이 숫자가 아니면, 더하기 계산을 할 필요가 없음
def add(n1, n2):

    if type(n1) != int or type(n2) != int:
        print('숫자 아님 안돼')
        return
    else:
        print(f'{n1}+{n2}={n1+n2}')

# 함수 호출
add(3, 4)
add(10, 20)
add('aa', 'bb') # 문자를 입력하면 더하기 x 
# 함수 만들기
def func():
    a = 1
    b = 2
    c = 3
    # 반환값은 무조건 1개
    # 한번에 abc를 반환하면 어떻게 될까?
    return a, b, c
# return에 값을 여러개 쓰면 tuple로 묶어서 반환됨
print(func()) # (1, 2, 3)
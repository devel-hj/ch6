# 나머지 매개변수를 사용하여 입력받은
# 도시 이름과 인구 수를 모두 출력하세요 
# (인구 수는 만 명 단위)
# 결과) seoul 950, busan 340, incheon 300

def show_population(**kwargs):
    # 여기에 코드를 작성하세요
    for key, value in kwargs.items():
        print(key, value)

show_population(seoul=950, busan=340, incheon=300)


# 나머지 매개변수를 사용하여 입력받은 상품의 상품명만 출력하세요
# 결과) milk bread egg(가격은 무시하고 상품명만 출력)
# 딕셔너리에서 key만 꺼내는 문제!
dic = {'milk':2500, 'bread':2000, 'egg':3000}
print(dic.keys())
# 나머지 매개변수는 딕셔너리로 저장됨
def show_items(**kwargs):
    # 1
    for key in kwargs:
        print(key)

    # 2
    for key in kwargs.keys():
        print(key)

show_items(milk=2500, bread=2000, egg=3000)
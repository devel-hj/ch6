# # 나머지 매개변수를 사용하는 함수 만들기
# # 사람의 정보를 입력받아 출력하는 함수 만들기
# def info(**kwargs):
#     print(kwargs) 

# info(name = '둘리', age = 10) # 주소 모름
# # {'name': '둘리', 'age': 10} => dic 1개
# info(name = '도우너', age = 8, address = '서울')
# # {'name': '도우너', 'age': 8, 'address': '서울'} => dic 1개



# 딕셔너리의 함수들
dic = {'name' : '둘리', 'age' : 10}
# dict_items([('name', '둘리'), ('age', 10)])
print(dic.keys()) # dict_keys(['name', 'age']) => 이터러블 객체(순회 가능), 이터러블은 for문 사용 가능
print(dic.values()) # dict_values(['둘리', 10])
print(dic.items()) # dict_items([('name', '둘리'), ('age', 10)])

# 사람의 정보를 하나씩 꺼내기
def info(**kwargs):
    # item 객체에서 요소를 꺼내면 tuple
    # 구조분해로 변수 두개에 key value 저장
    # 딕셔너리 안에 있는 요소 하나씩 꺼내기
    for key, value in kwargs.items():
        print(key, value) 

info(name = '둘리', age = 10) # 주소 모름
info(name = '도우너', age = 8, address = '서울')
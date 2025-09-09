# 나머지 매개변수를 사용하여 
# 입력받은 과일의 이름만 출력하세요
# 예) apple, banana, orange

def calc(**kwargs):
    for c in kwargs.keys():
        print(c)

calc(apple=1200, banana=800, orange=1500)

# 나머지 매개변수를 사용하여 입력받은 학생의 점수만 출력하세요
# 결과) 90,85, 100

def show_scores(**kwargs):
    for v in kwargs.values():
        print(v)

# 함수 호출
show_scores(철수=90, 영희=85, 민수=100)
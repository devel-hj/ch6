# 반대로 파일의 내용 읽어오기

# 읽기모드로 파일 열기
# 파일이름, 모드(w,r)
f = open('새파일.txt','r')

# 파일의 내용 읽어오기
# 읽기 함수들 중에서
# readlines는 결과를 리스트로 반환
# 결과는 리스트로 저장됨
# lines = f.readline()
# print(lines)

# 읽기 함수중에서
# read는 파일의 내용을
# 문자열 하나로 반환
text = f.read()
print(text)

# 문자열 안에 있는 알파벳을 하나씩 꺼내기
# 함수의 인자: 구분자
# split 함수는 공백을 기준으로
# 문자열을 쪼개고 결과를 리스트로 반환
lis = text.split(' ')
print(lis)

# 알파벳을 하나씩 출력하기
for ch in lis:
    print(ch)

# 함수의 형태 
# 리턴값이 있을때
# lis = text.split(' ') # 변수에 담기
# 리턴값이 없을때
# lis.sort()

# 사용이 끝났으면 닫기
f.close()
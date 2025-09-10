# 반대로 파일의 내용 읽어오기
# 입력장치: 키보드 -> 파일

# 키보드에서 값 입력받기
# input()
# 파일에서 값 읽어오기
# f.read()

# 파일에서 내용 읽어오기
# 파일이름, 모드
f = open('file1.txt', 'r')

# read 함수로 내용 읽어오기
# 결과를 리스트로 반환
# 내용에는 줄바꿈이 포함됨 \n
lis = f.readlines()

# 한줄씩 출력하기
for line in lis:
    # end 매개변수 값 변경
    print(line, end='')

# print 함수에는 end라는 매개변수가 있고 
# 기본값이 \n
print('1', end='\n')
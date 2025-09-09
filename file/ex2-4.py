# file 입출력 문제

# test.txt 파일을 만들고 다음과 같이 쓰세요
# 'hello'
# 'hi'
# 출력 후 콘솔 x 파일을 열어서 확인
f = open('test.txt', 'w')
f.write(f'hello\nhi')
f.close()

# score.txt 파일을 만들고 다음과 같이 쓰세요
# '80 90 70 100 60'
f = open('score.txt', 'w')
f.write('80 90 70 100 60')
f.close()

# numbers.txt 파일을 만들고 다음과 같이 쓰세요
# 10
# 11
# ...
# 20

f = open('numbers.txt', 'w')

for i in range(10, 21):
    f.write(f'{i}\n')
f.close()
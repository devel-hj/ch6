# score.txt 파일을 읽고 
# 합계와 평균을 구하세요
f = open('score.txt', 'r')
lis = f.read()
lis = lis.split(' ')


sum = 0
for i in lis:
    sum = sum + int(i)
    avg = sum / len(lis)
print( '합계 :', sum)
print( '평균 :', avg)
f.close()
    

# numbers.txt 파일을 읽고 짝수만 출력하세요
f = open('numbers.txt', 'r')
lis1 = f.readlines()

# lis2 = []
for line in lis1:
    if int(line)%2==0:
        print(line, end='')
        # lis2.append(line)
# print(lis2)

f.close()
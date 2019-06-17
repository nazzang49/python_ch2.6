# 입출력
import sys

x = 0.2
s = "hello"
print(x)
print(s)
print(x, s)
# 문자열은 + 연산기호로 조합 가능
print(str(x)+' '+s)

# print 함수 호출
print(sep=' ', end='\n')

# file 파라미터 지정
print('hello world', file=sys.stdout)
print('error : hello world', file=sys.stderr)

# file 출력
f = open('hello.txt', 'w')
print(type(f))
print('hello world',file=f)
f.close()

# Java
sys.stdout.write('hello world')

















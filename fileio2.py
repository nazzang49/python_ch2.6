f = open('test.txt', 'rt', encoding='utf-8')
text = f.read()
print(text)
text = f.read()
print('---', text, '---')

# position 단위는 byte
pos = f.tell()
print(pos)

# 특정 pos 찾기
f.seek(16)
text = f.read()
print(text)

f.seek(16,0)
text = f.read()
print(text)

# text mode에서는 from_what은 시작 인덱스만 허용
# f.seek(-10,2)
# text = f.read()
# print(text)

# line 단위 읽기
f2 = open('fileio2.py', 'rt', encoding='utf-8')
linenum = 0
while True:
    line = f2.readline()
    if line == '':
        f2.close()
        break
    linenum+=1
    print('{0}:{1}'.format(linenum, line), end='')

f3 = open('fileio2.py', 'rt', encoding='utf-8')
lines = f3.readlines()
print(type(lines))
for linenum, line in enumerate(lines):
    print('{0}:{1}'.format(linenum, line), end='')

# read as 구문은 별도의 close 함수 명시 X
with open('fileio2.py', 'rt', encoding='utf-8') as f2:
    for linenum, line in enumerate(f2.readlines()):
        print('{0}:{1}'.format(linenum, line), end='')


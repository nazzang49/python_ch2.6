# w = write, r = read (t = textmode 생략 가능)
f = open('test.txt', 'wt', encoding='utf-8')
size = f.write('안녕하세요\n파이썬 테스트')
f.close()
print(size)

# binary mode
f = open('test2.txt', 'wb')
size = f.write(bytes('안녕하세요\n 파이썬 테스트',encoding='utf-8'))
f.close()
print(size)

# read test
f = open('test.txt', 'rt', encoding='utf-8')
text = f.read()
f.close()
print(text)

# binary read like picture
fsrc = open('python.png', 'rb')
data = fsrc.read()
fsrc.close()
print(type(data))

fdest = open('python2.png', 'wb')
fdest.write(data)
fdest.close()

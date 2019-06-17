f = open('123.txt', 'wb')
f.write(b'0123456789')
f.close()

f = open('123.txt', 'rb')
print(f.tell())

# n,1 / 현재 위치에서 n바이트 이동(양수 = 뒤로, 음수 = 앞으로)
# n,2 / 마지막 위치에서 n바이트 이동
f.seek(5,1)
data = f.read(2)
print(data)

# 포인터를 가장 끝으로 이동
f.seek(0,2)
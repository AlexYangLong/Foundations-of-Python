'''
title: BytesIO
time: 2018.04.13 18:22
author: 杨龙（Alex）
'''

'''
StringIO只能操作字符串,那如果要操作二进制,则需要BytesIO
'''

from io import BytesIO

f = BytesIO()
print(f)

# 一个汉字表示三个字节
value = f.write('杨龙'.encode('utf-8'))
print(value)

print(f.getvalue())

f.seek(0)
print(f.read().decode())

f = BytesIO(b'\xe6\x9d\xa8\xe9\xbe\x99')
print(f.read().decode())

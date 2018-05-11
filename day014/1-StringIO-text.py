'''
title: StringIO
time: 2018.04.13 17:36
author: 杨龙（Alex）
'''

'''
StringIO:就是在内存中读写字符串
通常IO一般是在文件中来读写的.
使用StringIO会比在文件中操作内容速度快一些
'''

from io import StringIO

# 创建StringIO对象
f = StringIO()
print(f)

# f.write() 返回写入字串的长度
value = f.write('床前明月光，疑似地上霜。\n举头望明月，低头思故乡。\n\n')
print(value)

# f.write() 此函数会将指针停留在每次写入的最后
value = f.write('')
value = f.write('qwerty')

print(f.getvalue())

# f.seek(0)  将指针放在下标为0的位置
# f.seek(0)

f = StringIO('hongfenghuang\nfenfenghuang\nhongfenhongfenghuang\n')

while 1:
    str1 = f.readline()
    if str1 == '':
        break
    print(str1.strip())
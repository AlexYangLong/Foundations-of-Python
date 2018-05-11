'''
title: 输入一个字符串，将字符串中的大写字母转小写，小写字母转大写
time: 2018.03.31 08:50
author: 杨龙（Alex）
'''

str1 = input('请输入一个字符串：')
res = ''
i = 0
while i < len(str1):
    if str1[i] >= 'A' and str1[i] <= 'Z':
        res += chr(ord(str1[i]) + 32)
    elif str1[i] >= 'a' and str1[i] <= 'z':
        res += chr(ord(str1[i]) - 32)
    else:
        res += str1[i]
    i += 1

print(res)


#有一个字符串函数可以直接实现
print(str1.swapcase())

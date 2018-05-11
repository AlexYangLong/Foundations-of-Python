'''
title: 字符串简单操作
time: 2018.04.14 16:02
author: 杨龙（Alex）
'''

import pyperclip

# 转义字符
print('I like \'Red and Black\'')
# r:让转移字符 \ 失效
print(r'I like \'Red and Black\'')

# 成员运算符 in
str1 = 'aaaasdfgwet'
print('aa' in str1)

# 查看字符串中是否只包含字母
print(str1.isalpha())
# 查看字符串中是否只包含数字和字母
str2 = '12345671a'
print(str2.isalnum())
# 查看字符串中是否只有数字
print(str2.isdecimal())

print(str2[:4].isalpha())
print(str2[:4].isdecimal())

print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')

# 将列表转换成字符串的形式,并且以-进行连接
list1 = ['A', 'B', 'C', 'D']
print('-'.join(list1))

str3 = 'you-can-you-up'
# 将字符串以空格分割转换成列表的形式
list2 = str3.split('-')
print(list2)

str4 = ' asdfghewsad1  23   '
print(str4)
# 去掉字符串两端的空格
print(str4.strip())
# 去掉str左边的空格
print(str4.lstrip())
# 去调str右边的空格
print(str4.rstrip())

print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')

# 将文本内容拷贝到系统的剪贴板中
pyperclip.copy('窈窕淑女,君子好逑')
# 将内容从剪贴板中拿出来
print(pyperclip.paste())

print('####################################')

# 将字符串进行反转,有几种方法
str5 = 'hello,world'

def fun1(str):
    return str[::-1]

print(fun1(str5))

def fun2(str):
    list1 = list(str)
    list1.reverse()
    return ''.join(list1)

print(fun2(str5))

def fun3(str):
    if len(str) <= 1:
        return str
    return fun3(str[1:]) + str[0:1]

print(fun3(str5))

def fun4(str):
    str1 = ''
    for i in str:
        str1 = i + str1
    return str1

print(fun4(str5))

from io import StringIO
def fun5(str):
    strIO = StringIO()
    str_len = len(str)
    for i in range(str_len-1, -1, -1):
        strIO.write(str[i])
    return strIO.getvalue()

print(fun5(str5))

def fun6(str):
    str1 = ''
    str_len = len(str)
    for i in range(str_len-1, -1, -1):
        str1 += str[i]
    return str1

print(fun6(str5))

def fun7(str):
    return ''.join(str[index] for index in range(len(str)-1, -1, -1))

print(fun7(str5))



'''
title:int()、float()函数练习
time：2018.03.29 16:30
author:杨龙（Alex）
'''

# int() 函数  转换成整数
# float() 函数  转换成浮点数

print(int(1234))
print(int(1234.234))
print(int('+12343'))
#print(int('123+43'))
print(float(12))
print(float(12.4567))
print(float('+12343.12'))
#print(float('123-43.12'))

str1 = input('请输入一个字符串：')
print(int(str1))
print(float(str1))

'''
总结:
 如果在数字字符串中夹杂一些无用的字符,程序直接会报错
 只要某一行代码报错,后边程序不再执行.
'''



'''
title:字符串格式化的练习
time：2018.03.29 18:40
author:杨龙（Alex）
'''

'''
第一种格式化:  使用 %
%s:     给字符串占位
%d:     给int类型占位
        %10d  共10位,其他位使用空格补齐
        %010d  共10位,其他位使用0补齐
%f:     给浮点类型占位,  默认保留6为小数
        %.2f:  保留两位小数
        %10.2f  共10位,保留两位小数,其他位使用空格补齐 (小数点也算一位)
        %010.2f  共10位,保留两位小数,其他位使用0补齐 (小数点也算一位)
%c:     一个字符
%o:     将十进制转换成八进制
%x:     将十进制转换成十六进制
'''
name = 'Alex'
height = 169
age = 22
print('My name is %s，my height is %d cm，I\'m %d years old!' % (name, height, age))

pi = 3.1415926
print('pi的圆周率是%f' % (pi))
print('pi的圆周率是%.2f' % (pi))
print('pi的圆周率是%10.2f' % (pi))
print('pi的圆周率是%010.2f' % (pi))

a = 'w'
print('%c' % (a))  # 一个字符

a = 16
print('%o' % a)  # 转换成八进制
print('%x' % a)  # 转换成十六进制


'''
第二种格式化： 使用{}
'''
name = 'Alex'
height = 169
age = 22
print('My name is {}，my height is {} cm，I\'m {} years old!' .format(name, height, age))
print('My name is {name}，my height is {height} cm，I\'m {age} years old!' .format(age = age, name = name, height = height))
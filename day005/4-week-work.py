'''
title: 输入两个数，求这两个数的最大公约数
time: 2018.03.31 08:50
author: 杨龙（Alex）
'''

#辗转相除法实现
a = int(input('请输入第一个整数：'))
b = int(input('请输入第二个整数：'))

if a < b:
    tep = b
    b = a
    a = tep

while a % b != 0:
    temp = a % b
    a = b
    b = temp

print('最大公约数为：%d'%(b))




'''
title: 打印九九乘法表
time: 2018.03.31 08:50
author: 杨龙（Alex）
'''

for i in range(1,10):
    for j in range(1,i+1):
        print('%d * %d = %d'%(j, i, j * i), end='  ')
    print()
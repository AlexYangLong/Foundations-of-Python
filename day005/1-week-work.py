'''
title: 判断一个输入的数是否是质数
time: 2018.03.31 08:50
author: 杨龙（Alex）
'''

num = int(input('请输入一个整数：'))
i = 2
while i <= num // 2:
    if num % i == 0:
        print('不是质数')
        break
    i += 1
else:
    print("是质数")



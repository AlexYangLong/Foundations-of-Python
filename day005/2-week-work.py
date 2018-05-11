'''
title: 打印出所有三位数中的水仙花数
time: 2018.03.31 08:50
author: 杨龙（Alex）
'''

start = 100
while start < 1000:
    bw = start // 100
    sw = start // 10 % 10
    gw = start % 10
    if bw ** 3 + sw ** 3 + gw ** 3 == start:
        print(start)
    start += 1
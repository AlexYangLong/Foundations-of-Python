'''
title: 偏函数
time: 2018.04.04 17:00
author: 杨龙（Alex）
'''
'''
偏函数:
在python中定义函数时,我们可以使用默认参数,来降低调用函数时的难度,同样的使用偏函数也可以达到这样的效果
需要引入  
import functools
functools.partical 就是用来创建一个新的函数.不需要我们自行定义函数.直接将结果赋值给一个变量,而这个变量就是一个函数.这个函数的目的是将默认参数给固定住
'''
# 使用封装
# def int2(x, base = 2):
#     return int(x, base)

# print(int2('10001001111'))
# print(int2('2345',base = 8))

# 使用偏函数
import functools
int2 = functools.partial(int, base = 2)
print(int2('10001001111'))














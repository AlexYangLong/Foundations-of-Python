'''
title: 回调函数
time: 2018.04.04 17:07
author: 杨龙（Alex）
'''
'''
回调函数: 在定义函数时,将函数名作为参数传递过来,然后再函数里边再次调用函数.
'''
def my_callback_sum(num1, num2):
    print(num1 + num2)

def my_sum(num1, num2, fn):
    return fn(num1, num2)

my_sum(12, 45, my_callback_sum)















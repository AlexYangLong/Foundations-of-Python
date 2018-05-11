'''
title: 引入自定义模块2
time: 2018.04.09 18:45
author: 杨龙（Alex）
'''
# from 模块名 import function1, function2, ....
# from mymodule import add, sub, mul, div
from mymodule import *

print(add(2, 4))


# 如果模块中和引入执行的文件中定义了相同的函数,那么在执行时,执行文件中的函数警徽覆盖模块中的函数
def mul(num1, num2, num3):
    print(num1 * num2 *num3)

mul(3, 5, 7)




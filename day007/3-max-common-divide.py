'''
title: 求最大公约数 练习
time：2018.04.03 18:45
author: 杨龙（Alex）
'''

# 辗转相除法 while循环
def theMaxCommonDivideByWhile(num1, num2):
    if num1 < num2:
        num1, num2 = num2, num1

    while num1 % num2 != 0:
        tmp = num1 % num2
        num1 = num2
        num2 = tmp

    return num2

print(theMaxCommonDivideByWhile(4, 6))

# 辗转相除法 递归
def theMaxCommonDivideByRecursion(num1, num2):
    if num1 < num2:
        num1, num2 = num2, num1

    if num1 % num2 == 0:
        return num2
    else:
        return theMaxCommonDivideByRecursion(num2, num1 % num2)

print(theMaxCommonDivideByRecursion(4, 6))












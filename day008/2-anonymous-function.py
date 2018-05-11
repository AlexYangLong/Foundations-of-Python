'''
title: 匿名函数
time: 2018.04.04 16:50
author: 杨龙（Alex）
'''
'''
匿名函数: 没有名字的函数就是匿名函数
关键字: lambda
格式: lambda 形式参数1, 形式参数2,...,参数n:expression
调用: 变量 = lambda 形式参数1, 形式参数2,...,参数n:expression
      变量()
'''
sum1 = lambda num1, num2: num1 + num2
print(sum1(2, 45))


def calculate(num1, num2, fn):
    return fn(num1, num2)

print(calculate(5, 2, lambda n1, n2: n1 + n2))
print(calculate(5, 2, lambda n1, n2: n1 - n2))
print(calculate(5, 2, lambda n1, n2: n1 / n2))
print(calculate(5, 2, lambda n1, n2: n1 % n2))
print(calculate(5, 2, lambda n1, n2: n1 // n2))
print(calculate(5, 2, lambda n1, n2: n1 ** n2))













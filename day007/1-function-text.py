'''
title: 函数的定义，调用，有参、无参、有返回值、无返回值 练习
time：2018.04.03 17:30
author: 杨龙（Alex）
'''

'''
函数的优点：
1、减少代码重复率,增加程序的运行效率
2、便于修改，修改某个功能时,直接将整个项目的功能全部修改
设计模式：单例模式  工厂模式  门面模式  适配器
'''

# 函数定义 使用 def
'''
    def 函数名([参数1, 参数2, ...]):
        代码块
        [return]
'''
def func1():
    print('这是一个函数！！！')

#函数的调用
func1()

# 定义一个无参数无返回值的函数
def func2():
    print('这是一个无参无返回值的函数！！！')

func2()

#定义一个有参数无返回值的函数
def func3(name, age):
    print('My name is %s, i am %d years old!' % (name, age))

func3('Alex', 22)

#定义一个无参数又返回值得函数
def func4():
    list1 = []
    for i in range(10):
        list1.append(i)
    return list1

print(func4())

#定义一个有参数有返回值的函数
def func5(num1, num2):
    add = num1 + num2
    sub = num1 - num2
    mul = num1 * num2
    div = num1 / num2
    exp = num1 ** num2
    exact_division = num1 // num2
    return (add, sub, mul, div, exp, exact_division)

print(func5(5, 2))

# 定义一个有默认参数的函数
def sayHello(name='Alex'):
    print('Hello,world! I am %s!' % name)

sayHello('Ala')
sayHello()

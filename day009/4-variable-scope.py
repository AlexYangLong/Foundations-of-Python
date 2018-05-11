'''
title: 变量作用域
time: 2018.04.08 17:13
author: 杨龙（Alex）
'''

'''
作用域:针对于变量  在函数中的使用情况
局部作用域:
函数作用域:(闭包以外的函数)
全局作用域:(定义到整个文档中)
内建作用域:
'''

# 下面的情况体现不出作用域
num1 = 10
if 1:
    tmp = 20
print(tmp)
print(num1)


# 总结1: 在函数内部定义的变量无法在函数外部使用
def func1():
    num2 = 10
    print(num2)
func1()
# print(num2)

# 总结2: 在函数外部定义的变量可以在函数内部使用
num3 = 30
def func2():
    print('函数内部打印：%d' % num3)
    print(id(num3))

func2()
print('函数外部打印：%d' % num3)
print(id(num3))

# 总结3: 这里并没有体现作用域,只是分别在函数外部和函数内容定义了相同名字的变量名而已
num4 = 50
def func3():
    num4 = 666
    print('函数内部打印：%d' % num4)
    print(id(num4))

func3()
print('函数外部打印：%d' % num4)
print(id(num4))

# 总结4: 一旦在函数内部设置为global,则该变量全局有效
num5 = 100
def func4():
    global num5
    num5 = 666
    print('函数内部打印：%d' % num5)
    print(id(num5))

func4()
print('函数外部打印：%d' % num5)
print(id(num5))

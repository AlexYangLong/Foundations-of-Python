'''
title: 装饰器
time: 2018.04.08 17:13
author: 杨龙（Alex）
'''

'''
装饰器:
1.在定义函数时,将函数名作为参数来传递
2.自定义一个装饰器,(即自定义一个函数),在函数内部去调用真正的函数
3.return 装饰器的自调
'''

# def func1():
#     print('这是一个函数')
#
# def func2(func):
#     def __decorator():
#         print('装饰器....')
#         func()
#         print('啦啦啦....')
#     return __decorator
#
# fun = func2(func1)
# fun()


# def outer(func):
#     def inner():
#         print('这是第一行')
#         return func()
#         print('这是第二行')
#     return inner()
#
# def mul():
#     return '这是乘法'
#
# print(outer(mul))


def outer(func):
    def inner():
        print('装饰器....')
        func()
        print('啦啦啦....')
    return inner

@outer
def func3():
    print('1234567')

func3()
'''
title: 运算符重载
time: 2018.04.12 16:47
author: 杨龙（Aelx）
'''

'''
运算符的重载:
1.基本上所有的重载方法前后都要加上双下划线
2.运算符的重载方法都是可选的,如果没有编写或者在类里边没有定义.那么就不支持重载
运算符重载即就是在执行某种特定的操作,并且在类中定义了该方法,则这些方法会被自动调用
'''

class Number(object):
    def __init__(self, value):
        if not isinstance(value, int):
            self.num = 0
        else:
            self.num = value


    def __sub__(self, other):
        return self.num - other

    def __add__(self, other):
        return self.num + other

    def __mul__(self, other):
        return self.num * other

num = Number(13)

y = num - 5
y = num + 5
y = num * 5
print(y)


class Class(list):
    def __sub__(self, b):
        a = self[:]
        b = b[:]
        while len(b) > 0:
            val_b = b.pop()
            if val_b in a:
                a.remove(val_b)
        return a


    def __add__(self, other):
        a = self[:]
        b = other[:]
        while len(b) > 0:
            val_b = b.pop()
            if val_b not in a:
                a.append(val_b)
        return a

list1 = [1, 2, 3, 4, 5, 6]
list2 = [2, 4, 6, 8, 9]
print(Class(list1) - Class(list2))
print(Class(list1) + Class(list2))


class Goods(object):
    def __getitem__(self, item):
        # print(self)
        return item ** 3

x = Goods()
print(x[2])
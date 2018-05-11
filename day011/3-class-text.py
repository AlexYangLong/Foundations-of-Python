'''
title: 面向对象 练习
time: 2018.04.10 17:42
author: 杨龙（Alex）
'''
class Rat(object):
    def __init__(self, name, age, color):
        self.__name = name
        self.__age = age
        self.__color = color
        print('构造函数执行')

    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age
    def set_age(self, age):
        self.__age = age

    def get_color(self):
        return self.__color
    def set_color(self, color):
        self.__color = color

    def eat(self, food):
        return '%s偷吃%s' % (self.__name, food)

    def eatWith(self, ratList):
        if len(ratList):
            str1 = '%s ' % self.__name
            for rat in ratList:
                str1 += '%s ' % rat.get_name()
            str1 += '一起去偷东西吃'
            return str1
        else:
            return '%s去偷东西吃' % (self.__name)

    def __del__(self):
        print('析构函数执行')


rat1 = Rat('rat1', 2, 'white')
print(rat1.get_name(), rat1.get_age(), rat1.get_color())

rat2 = Rat('rat2', 3, 'yellow')
print(rat2.eat('rice'))

ratList = []
ratList.append(rat1)
ratList.append(rat2)
rat3 = Rat('cat3', 4, 'gray')
print(rat3.eatWith(ratList))

ratList.append(rat3)
rat4 = Rat('cat4', 5, 'black')
print(rat4.get_name(), rat4.get_age(), rat4.get_color())

ratList.append(rat4)
rat5 = Rat('cat5', 6, 'white-black')
print(rat5.get_name(), rat5.get_age(), rat5.get_color())
print(rat5.eat('pork'))
print(rat5.eatWith(ratList))
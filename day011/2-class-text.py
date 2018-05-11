'''
title: 面向对象 练习
time: 2018.04.10 17:33
author: 杨龙（Alex）
'''

class Cat(object):
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
        return '%s吃%s' % (self.__name, food)

    def playWith(self, otherCat):
        return '%s和%s一起玩' % (self.__name, otherCat.get_name())

    def __del__(self):
        print('析构函数执行')

cat1 = Cat('cat1', 2, 'white')
print(cat1.get_name(), cat1.get_age(), cat1.get_color())

cat2 = Cat('cat2', 3, 'yellow')
print(cat2.eat('fish'))

cat3 = Cat('cat3', 4, 'gray')
print(cat3.playWith(cat2))

cat4 = Cat('cat4', 5, 'black')
print(cat4.get_name(), cat4.get_age(), cat4.get_color())
print(cat4.eat('fishes'))

cat5 = Cat('cat5', 6, 'white-black')
print(cat5.get_name(), cat5.get_age(), cat5.get_color())
print(cat5.eat('fishes'))
print(cat5.playWith(cat4))

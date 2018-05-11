'''
title: 面向对象 练习
time: 2018.04.10 17:22
author: 杨龙（Alex）
'''
class Dog(object):

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

    def run(self):
        return '%s会跑' % (self.__name)

    def __del__(self):
        print('析构函数执行')


dog1 = Dog('dog1', 3, 'red')
print(dog1.get_name(), dog1.get_age(), dog1.get_color())

dog2 = Dog('dog2', 2, 'yellow')
print(dog2.get_name(), dog2.get_age(), dog2.get_color())
print(dog2.eat('骨头'))
print(dog2.run())

dog3 = Dog('dog3', 1, 'white')
dog3.set_color('black')
print(dog3.get_name(), dog3.get_color())

dog4 = Dog('dog4', 4, 'white')
dog4.set_age(6)
print(dog4.get_name(), dog4.get_age(), dog4.get_color())

dog5 = Dog('dog5', 5, 'white')
dog5.set_name('dog55')
print(dog5.get_name(), dog5.get_age(), dog5.get_color())

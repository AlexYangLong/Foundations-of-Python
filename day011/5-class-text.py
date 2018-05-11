'''
title: 面向对象 练习
time: 2018.04.10 18:35
author: 杨龙（Alex）
'''
class Fish(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        print('构造函数执行')

    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age
    def set_age(self, age):
        if age <= 0:
            self.__age = 1
        else:
            self.__age = age

    def swim(self):
        print('My name is %s, I can swim!' % self.__name)

    def TPP(self):
        print('I am %d, I am learning TPP!' % self.__age)

    def __del__(self):
        print('析构函数执行')

f1 = Fish('f1', 1)
print(f1.get_name(), f1.get_age())

f2 = Fish('f2', 2)
print(f2.get_name(), f2.get_age())
f2.set_age(0)
print(f2.get_name(), f2.get_age())

f3 = Fish('f3', 3)
f3.swim()

f4 = Fish('f4', 4)
f4.TPP()

f5 = Fish('f5', 5)
print(f5.get_name(), f5.get_age())
f5.swim()
f5.TPP()


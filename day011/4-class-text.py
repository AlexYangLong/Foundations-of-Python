'''
title: 面向对象 练习
time: 2018.04.10 18:24
author: 杨龙（Alex）
'''
class Duck(object):
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

    def swim(self, duckList):
        if len(duckList):
            str1 = '%s ' % self.__name
            for duck in duckList:
                str1 += '%s ' % duck.get_name()
            str1 += '一起去浮水'
            return str1
        else:
            return '%s去浮水' % (self.__name)

    def __del__(self):
        print('析构函数执行')

duck1 = Duck('duck1', 1, 'white')
print(duck1.get_name(), duck1.get_age(), duck1.get_color())

duck2 = Duck('duck2', 2, 'yellow')
print(duck2.eat('xxx'))

duck3 = Duck('duck3', 3, 'gray')
print(duck3.get_name(), duck3.get_age(), duck3.get_color())
print(duck3.eat('xxxx'))

duck4 = Duck('duck4', 4, 'black')
print(duck4.get_name(), duck4.get_age(), duck4.get_color())
print(duck4.eat('xxxxxxx'))

duckList = []
duckList.append(duck1)
duckList.append(duck2)
duckList.append(duck3)
duckList.append(duck4)
duck5 = Duck('duck5', 5, 'orange')
print(duck5.get_name(), duck5.get_age(), duck5.get_color())
print(duck5.eat('pork'))
print(duck5.swim(duckList))
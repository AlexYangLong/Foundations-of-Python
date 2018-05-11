'''
title: 面向对象 练习
time: 2018.04.10 18:44
author: 杨龙（Alex）
'''
class Snack(object):
    def __init__(self, name, age, length):
        self.__name = name
        self.__age = age
        self.length = length
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

    def run(self):
        print('My name is %s, I can run!' % self.__name)

    def BS(self):
        if self.__age < 3:
            print('I am %d, I am not learning BS!' % self.__age)
        else:
            print('I am %d, I am learning BS!' % self.__age)

    def __del__(self):
        print('析构函数执行')

s1 = Snack('s1', 1, 50)
print(s1.get_name(), s1.get_age(),s1.length)

s2 = Snack('s2', 2, 70)
print(s2.get_name(), s2.get_age())
s2.set_age(0)
print(s2.get_name(), s2.get_age())

s3 = Snack('s3', 3, 110)
s3.run()

s4 = Snack('s4', 4, 120)
s4.BS()

s5 = Snack('s5', 2, 65)
print(s5.get_name(), s5.get_age())
s5.run()
s5.BS()










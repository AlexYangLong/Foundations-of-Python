'''
title: 面向对象 练习
time: 2018.04.10 18:52
author: 杨龙（Alex）
'''
class Spider(object):
    def __init__(self, name, age, isPoison):
        self.__name = name
        self.__age = age
        self.isPoison = isPoison
        print('构造函数执行')

    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age
    def set_age(self, age):
        self.__age = age

    def eat(self, food):
        return '%s吃%s' % (self.__name, food)

    def __str__(self):
        if self.isPoison:
            return 'My name is %s, %d years old, %s' % (self.__name,self.__age, '有毒')
        else:
            return 'My name is %s, %d years old, %s' % (self.__name, self.__age, '无毒')

    def __del__(self):
        print('析构函数执行')

s1 = Spider('s1', 1, True)
print(s1.get_name(), s1.get_age(),s1.isPoison)

s2 = Spider('s2', 2, True)
print(s2.get_name(), s2.get_age())
s2.set_age(0)
print(s2.get_name(), s2.get_age())

s3 = Spider('s3', 3, False)
s3.eat('ssss')

s4 = Spider('s4', 4, True)
print(s4)

s5 = Spider('s5', 2, False)
print(s5.get_name(), s5.get_age())
s5.eat('aaaa')
print(s5)






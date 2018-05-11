'''
title: 面向对象 练习
time: 2018.04.10 19:33
author: 杨龙（Alex）
'''
class Teacher(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def teach(self, course):
        print('hello, I am %s, I am teaching %s' % (self.name, course))

    def __del__(self):
        print('析构函数')

t1 = Teacher('t1', 25)
print(t1.name, t1.age)

t2 = Teacher('t2', 27)
t2.teach('English')

t3 = Teacher('t3', 30)
print(t3.name, t3.age)
t3.teach('Chinese')

t4 = Teacher('t4', 32)
print(t4.name, t4.age)
t4.teach('math')

t5 = Teacher('t5', 35)
print(t5.name, t5.age)
t3.teach('Chinese')





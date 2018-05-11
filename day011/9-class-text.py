'''
title: 面向对象 练习
time: 2018.04.10 19:07
author: 杨龙（Alex）
'''
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sayHello(self):
        print('hello, I am %s' % self.name)

    def __del__(self):
        print('析构函数')

p1 = Person('p1', 13)
print(p1.name, p1.age)

p2 = Person('p2', 15)
p2.sayHello()

p3 = Person('p3', 18)
p3.girlfriend = 'Ala'
print(p3.girlfriend)

p4 = Person('p4', 20)
p4.girlfriend = 'Eril'
print(p4.girlfriend)

p5 = Person('p5', 22)
p5.wife = 'Adli'
print(p5.wife)









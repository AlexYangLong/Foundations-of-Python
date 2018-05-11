'''
title: 面向对象 练习
time: 2018.04.10 19:00
author: 杨龙（Alex）
'''
class Plane(object):
    def __init__(self, name):
        self.name = name

    def fly(self):
        print('fly........')

    def __del__(self):
        print('析构函数')


p1 = Plane('p1')
print(p1.name)

p2 = Plane('p1')
p2.fly()

p3 = Plane('p1')
p3.color = 'gold'
print(p3.color)

p4 = Plane('p1')
print(p4.name)

p5 = Plane('p1')
print(p4.name)
p5.fly()













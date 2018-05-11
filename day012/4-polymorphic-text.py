'''
title: 多态
time: 2018.04.11 18:25
author: 杨龙（Alex）
'''

# 多态: 同一种行为具有不同的表现形式

class Animal(object):
    def eat(self):
        print('动物都会吃东西......')

class Tiger(Animal):
    def eat(self):
        print('老虎喜欢吃生肉......')

class Lion(Animal):
    def eat(self):
        print('狮子喜欢吃羚羊......')

def eatSomething(type):
    type.eat()

t1 = Tiger()
l1 = Lion()

eatSomething(t1)
eatSomething(l1)


'''
title: 单继承
time: 2018.04.11 17:13
author: 杨龙（Alex）
'''

'''
object: 是所有类的基类
1.在类名后边的括号里一般写的是基类的类名
2.子类中继承自父类(基类),则父类的成员属性和成员方法都可以被子类所继承
3.父类中私有的成员属性不能继承给子类的
'''

class Animal(object):
    def sleep(self):
        print('动物一般都是躺着睡的')

class Person(Animal):
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def eat(self):
        print('我喜欢吃肉')

    def run(self):
        print('我可以跑........')

class Girl(Person):
    pass

Ala = Girl('艾拉', 22, 168)
print(Ala.name, Ala.age, Ala.height)
Ala.eat()
Ala.run()
Ala.sleep()





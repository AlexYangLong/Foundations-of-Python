'''
title: 重写
time: 2018.04.11 18:15
author: 杨龙（Alex）
'''

# 在继承时,父类和子类具有相同的成员,在调用时,输出的是子类的内容,这就是子类重写了父类的成员

class Animal(object):
    tag = '动物'
    def __init__(self, color, age):
        self.color = color
        self.age = age

    def run(self):
        print('动物都会跑.....')

    def eat(self):
        print('动物都会吃....')

class Dog(Animal):
    tag = '狗'
    def __init__(self, name, age, color):
        super().__init__(color, age)
        self.name = name

    def run(self):
        print('狗都会跑.....')

    def eat(self):
        print('小狗狗吃骨头....')

dog = Dog('xiaogou', 3, 'yellow')
print(dog.tag)
dog.run()
dog.eat()

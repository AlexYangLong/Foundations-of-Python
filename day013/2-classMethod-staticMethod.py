'''
title: 类方法 、静态方法
time: 2018.04.12 16:19
author: 杨龙（Aelx）
'''
class Dog(object):
    user = '泰迪'
    age = 2

    def __init__(self, name, color, sex):
        self.name = name
        self.color = color
        self.sex = sex

    '''
        1.在类方法中:可以调直接类属性
        2.在调对象成员时需要将对象传递过来,才能使用对象的成员
    '''
    @classmethod
    def func(cls, self):
        print(Dog.user, Dog.age)
        self.run()

    def run(self):
        print('%s跑' % self.name)

    @staticmethod
    def sleep(dog):
        print(dog.name, dog.color, dog.sex)
        dog.run()


jinmao = Dog('金毛', 'gold', '公')
jinmao.func(jinmao)

jinmao.sleep(jinmao)




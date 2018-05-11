'''
title: 多继承
time: 2018.04.11 17:35
author: 杨龙（Alex）
'''
class Animal(object):
    def eat(self):
        return '动物一般喜欢吃肉...'

# 驴
class Donkey(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def tuimo(self):
        return '驴推磨......'

    def eat(self):
        return '驴喜欢吃干草...'

# 马
class Horse(Animal):
    def __init__(self, weight):
        self.weight = weight

    def run(self):
        return '汗血宝马可以日行千里，夜行八百'

    def eat(self):
        return '马喜欢吃青草'

# 骡子继承驴和马    多继承: 在类名后边的括号里可以写多个类名,中间使用 , 隔开
class Mule(Donkey, Horse):
    def eat(self):
        return '骡子喜欢吃干青草'

# 在子类中没有自定义 __init__ 时，多继承时,在实例化对象时,参数是以在最前边的父类为准
xiaoluo = Mule('xiaoluo', 2)
print(xiaoluo.name)
print(xiaoluo.eat())  # 重写






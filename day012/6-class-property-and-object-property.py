'''
title: 类属性和对象属性
time: 2018.04.11 18:25
author: 杨龙（Alex）
'''

# 对象.属性名 如果有构造方法,则获取的是对象的属性, 如果没有构造方法,则获取的是默认的类的属性
# 类名.属性名 永远调用的是类的属性

class Animal(object):
    name = 'Animal'

    def __init__(self, name):
        self.name = name

    def dy(self):
        print(Animal.name)
        print(self.name)

taidi = Animal('泰迪')
print(taidi.name)
print(Animal.name)
taidi.dy()

del taidi.name
# del taidi.name
print(taidi.name)

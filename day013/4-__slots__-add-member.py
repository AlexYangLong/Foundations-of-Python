'''
title: 动态添加属性、方法  __slots__
time: 2018.04.12 16:31
author: 杨龙（Aelx）
'''

from types import MethodType

class Person(object):
    # 当类中需要创建大量的指定的属性时,使用 __slots__ 来创建指定的属性
    __slots__ = ('name', 'age', 'run')


p1 = Person()
# 动态的添加属性
p1.name = 'Alex'
print(p1.name)
# 该属性没有添加成功,因为在类内没有指定
# p1.weight = 180
# print(p1.weight)

def paobu(object):
    print('%s can run' % object.name)

# 方式一： 没有将方法实际添加到对象中
# p1.run = paobu
# p1.run(p1)

# 方式二：
p1.run = MethodType(paobu, p1)
p1.run()










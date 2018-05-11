'''
title: 动态添加属性、方法
time: 2018.04.12 16:27
author: 杨龙（Aelx）
'''

from types import MethodType

class Person(object):
    pass

p1 = Person()
# 动态添加成员属性
p1.name = 'Alex'

print(p1.name)

def run(object):
    print('%s can run' % object.name)

# 动态添加成员方法
p1.run = MethodType(run, p1)
p1.run()









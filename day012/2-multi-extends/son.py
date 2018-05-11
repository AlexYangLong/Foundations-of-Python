'''
title: 多继承
time: 2018.04.11 17:42
author: 杨龙（Alex）
'''

from father import Father
from mother import Mother

class Son(Father, Mother):
    def __init__(self, money, facevalue):
        Father.__init__(self, money)
        Mother.__init__(self, facevalue)

        print(Father.eat(self))
        print(Mother.eat(self))

    def earn(self):
        # 方式一
        return Father.earn(self)
        # 方式二  不常使用
        # return super().earn()

xiaoming = Son(100000, 9)
print(xiaoming.money)
print(xiaoming.facevalue)

print(xiaoming.earn())
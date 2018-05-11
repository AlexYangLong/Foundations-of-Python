'''
title: 面向对象 练习
time: 2018.04.10 19:57
author: 杨龙（Alex）
'''
class Car(object):
    def __init__(self, tag, color, price):
        self.tag = tag
        self.color = color
        self.price = price

    def speed(self, speeding):
        print('%s , %d m/s' % (self.tag, speeding))

    def __str__(self):
        return  '%s , %s , %d' % (self.tag, self.color, self.price)

    def __del__(self):
        print('析构函数')

c1 = Car('Benz', 'white', 300000)
print(c1)
c1.speed(35)

c2 = Car('Audi', 'white', 350000)
print(c2)
c2.speed(33)

c3 = Car('BMW', 'white', 320000)
print(c3)
c3.speed(30)

c4 = Car('Hongqi', 'white', 340000)
print(c4)
c4.speed(20)

c5 = Car('Falarri', 'white', 1000000)
print(c5)
c5.speed(50)





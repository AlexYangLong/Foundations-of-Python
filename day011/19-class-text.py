'''
title: 面向对象 练习
time: 2018.04.10 20:20
author: 杨龙（Alex）
'''
class Computer(object):
    def __init__(self, tag, color, price):
        self.tag = tag
        self.color = color
        self.price = price

    def __str__(self):
        return '%s, %s, %d' % (self.tag, self.color, self.price)

    def __del__(self):
        print('析构函数')

thinkpad = Computer('ThinkPad', 'black', 5500)
print(thinkpad)

asus = Computer('ASUS', 'sliver', 6500)
print(asus)

dell = Computer('Dell', 'blue', 6000)
print(dell)

apple = Computer('Apple', 'white', 9000)
print(apple)

shenzhou = Computer('ShenZhou', 'black', 5000)
print(shenzhou)






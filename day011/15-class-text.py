'''
title: 面向对象 练习
time: 2018.04.10 19:50
author: 杨龙（Alex）
'''
class Calculate(object):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        print('%d + %d = %d' % (self.num1, self.num2, self.num1 + self.num2))

    def sub(self):
        print('%d - %d = %d' % (self.num1, self.num2, self.num1 - self.num2))

    def mul(self):
        print('%d * %d = %d' % (self.num1, self.num2, self.num1 * self.num2))

    def div(self):
        print('%d / %d = %d' % (self.num1, self.num2, self.num1 / self.num2))

    def mod(self):
        print('%d mod %d = %d' % (self.num1, self.num2, self.num1 % self.num2))

    def qm(self):
        print('%d ** %d = %d' % (self.num1, self.num2, self.num1 ** self.num2))

    def __del__(self):
        print('析构函数')

c1 = Calculate(10, 3)
c1.add()

c2 = Calculate(10, 3)
c2.sub()

c3 = Calculate(10, 3)
c3.mul()

c4 = Calculate(10, 3)
c4.div()

c5 = Calculate(10, 3)
c5.mod()
c5.qm()





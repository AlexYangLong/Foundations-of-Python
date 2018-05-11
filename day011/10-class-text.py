'''
title: 面向对象 练习
time: 2018.04.10 19:15
author: 杨龙（Alex）
'''
class Men(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def earn(self, money):
        print('I am earned %d this month!' % money)

    def __del__(self):
        print('析构函数')

m1 = Men('m1', 13)
print(m1.name, m1.age)

m2 = Men('m2', 15)
m2.earn(0)

m3 = Men('m3', 18)
m3.girlfriend = 'AAA'
print(m3.girlfriend)

m4 = Men('m4', 20)
m4.girlfriend = 'BBB'
print(m4.girlfriend)
m4.earn(2000)

m5 = Men('m5', 22)
m5.wife = 'CCC'
print(m5.wife)
m5.earn(7000)





'''
title: 面向对象 练习
time: 2018.04.10 19:45
author: 杨龙（Alex）
'''
class Employee(object):
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def dowork(self):
        print('hello, I am %s, I am doing work!' % self.name)

    def __del__(self):
        print('析构函数')

ee1 = Employee('ee1', 25, 3000)
print(ee1.name, ee1.age, ee1.salary)
ee1.dowork()

ee2 = Employee('ee2', 28, 5000)
print(ee2.name, ee2.age, ee2.salary)
ee2.dowork()

ee3 = Employee('ee3', 26, 4700)
print(ee3.name, ee3.age, ee3.salary)
ee3.dowork()

ee4 = Employee('ee4', 24, 2800)
print(ee4.name, ee4.age, ee4.salary)
ee1.dowork()

ee5 = Employee('ee5', 30, 8000)
print(ee5.name, ee5.age, ee5.salary)
ee5.dowork()





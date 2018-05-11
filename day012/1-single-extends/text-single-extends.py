'''
title: 单继承
time: 2018.04.11 17:30
author: 杨龙（Alex）
'''

from person import Person
from student import Student
from teacher import Teacher

Black = Student('Black', 17, 169, 1000,  123456)
print(Black.name)
# 在子类中不能继承父类的私有属性
# print(Black.__money)
print(Black.stuId)

print(Black.get_money())
print(Black._age)


haiyan = Teacher('haiyan', 18, 166, 10000, 'Python')
haiyan.teach()

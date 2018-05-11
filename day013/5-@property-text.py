'''
title: @property
time: 2018.04.12 16:39
author: 杨龙（Aelx）
'''

class Student(object):
    def __init__(self, score):
        self.__score = score

    def get_score(self):
        return self.__score

    def set_score(self, value):
        if not isinstance(value, int):  # 判断是否是 int 类型
            print('当前您输入的分数不是数字')
        elif value < 0 or value > 150:
            print('当前您输入的分数不在 [0,150] 范围内')
        else:
            self.__score = value

xx = Student(88)
print(xx.get_score())
xx.set_score(111)
print(xx.get_score())


class Teacher(object):
    def __init__(self, salary):
        self.__salary = salary

    # @property表示只读 将salary方法当做一个'属性'来访问, 访问的属性名就是该方法名  对象名.属性
    @property
    def salary(self):
        return self.__salary

    # salary.setter 表示既可以读也可以写  赋值： 对象名.属性 = 新值
    @salary.setter
    def salary(self, value):
        if not isinstance(value, int):
            print('当前您输入的薪水不是数字')
        elif value < 0:
            print('输入的薪水不能小于0')
        else:
            self.__salary = value

dd = Teacher(1000)

print(dd.salary)
dd.salary = 3000
print(dd.salary)
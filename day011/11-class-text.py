'''
title: 面向对象 练习
time: 2018.04.10 19:25
author: 杨龙（Alex）
'''
class Student(object):
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def study(self, course):
        print('hello, I am %s, I am learning %s' % (self.name, course))

    def __del__(self):
        print('析构函数')

s1 = Student('s1', 13, 7)
print(s1.name, s1.age, s1.grade)

s2 = Student('s2', 14, 8)
s2.study('English')

s3 = Student('s3', 15, 9)
s3.girlfriend = 'AAAA'
print(s3.girlfriend)
s3.study('English')

s4 = Student('s4', 16, 10)
s4.girlfriend = 'BBBB'
print(s4.girlfriend)
s4.study('math')

s5 = Student('s5', 17, 11)
s5.girlfriend = 'CCCC'
print(s5.girlfriend)
s5.study('Chinese')





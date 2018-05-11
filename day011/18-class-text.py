'''
title: 面向对象 练习
time: 2018.04.10 20:13
author: 杨龙（Alex）
'''
class Beauty(object):
    def __init__(self, name, age, dynasty):
        self.name = name
        self.age = age
        self.dynasty = dynasty

    def sayHello(self):
        print('hello, I am %s, I am %d years old, I am living %s.' % (self.name, self.age, self.dynasty))

    def __del__(self):
        print('析构函数')

zhaofeiyan = Beauty('ZhaoFeiYan', 24, 'Han')
zhaofeiyan.sayHello()

diaochan = Beauty('DiaoChan', 25, 'SanGuo')
diaochan.sayHello()

yangyuhuan = Beauty('YangYuHuang', 24, 'Tang')
yangyuhuan.sayHello()

baoni = Beauty('BaoNi', 24, 'Xia')
baoni.sayHello()

daji = Beauty('DaJi', 26, 'Shan')
daji.sayHello()





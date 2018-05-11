'''
title: 面向对象 练习
time: 2018.04.10 20:05
author: 杨龙（Alex）
'''
class HistoricalFigure(object):
    def __init__(self, name, identity, dynasty):
        self.name = name
        self.identity = identity
        self.dynasty = dynasty

    def sayHello(self):
        print('hello, I am %s, I am living %s, I am a %s.' % (self.name, self.dynasty, self.identity))

    def __del__(self):
        print('析构函数')

qinshihuang = HistoricalFigure('QinShiHuang', 'emperor','Qin')
qinshihuang.sayHello()

huoqubing = HistoricalFigure('HuoQuBing', 'general','Han')
huoqubing.sayHello()

libai = HistoricalFigure('LiBai', 'poet','Tang')
libai.sayHello()

gaochanggong = HistoricalFigure('GaoChangGong', 'general','BeiQi')
gaochanggong.sayHello()

weiqin = HistoricalFigure('WeiQin', 'general','Han')
weiqin.sayHello()




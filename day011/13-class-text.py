'''
title: 面向对象 练习
time: 2018.04.10 19:40
author: 杨龙（Alex）
'''
class Player(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def play(self, game):
        print('hello, I am %s, I am going to play %s' % (self.name, game))

    def __del__(self):
        print('析构函数')

p1 = Player('p1', 13)
print(p1.name, p1.age)

p2 = Player('p2', 15)
p2.play('cards')

p3 = Player('p3', 18)
p3.girlfriend = 'Ala'
print(p3.girlfriend)

p4 = Player('p4', 20)
p4.girlfriend = 'Eril'
print(p4.girlfriend)

p5 = Player('p5', 22)
print(p5.name, p5.age)
p5.play('chess')







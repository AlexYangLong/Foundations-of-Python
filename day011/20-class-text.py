'''
title: 面向对象 练习
time: 2018.04.10 20:33
author: 杨龙（Alex）
'''
class Boy(object):
    def __init__(self, name, age, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby

    def showhobby(self):
        print('I am %s' % self.name ,end=',')
        if len(self.hobby):
            print('I like', end=' ')
            for h in self.hobby:
                print(h,end=',')
            print()
        else:
            print('暂无爱好')

    def __del__(self):
        print('析构函数')

b1 = Boy('Alex', 22, ['reading','fishing','dongman'])
b1.showhobby()

b2 = Boy('Adam', 23, [])
b2.showhobby()

b3 = Boy('Black', 24, ['reading','sport'])
b3.showhobby()

b4 = Boy('Clark', 25, ['reading','thinking'])
b4.showhobby()

b5 = Boy('David', 27, ['reading','fishing'])
b5.showhobby()




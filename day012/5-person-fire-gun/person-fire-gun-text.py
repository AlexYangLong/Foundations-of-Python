'''
title: 类属性和对象属性
time: 2018.04.11 18:38
author: 杨龙（Alex）
'''

from bulletBox import BulletBox
from gun import Gun
from person import Person

bulletbox = BulletBox(5)

gun1 = Gun(bulletbox)

person1 = Person(gun1)

person1.fire()
person1.fire()
person1.fire()
person1.fire()
person1.fire()
person1.fire()

person1.reload(0)

person1.reload(10)
person1.fire()






'''
title: datetime模块 练习
time: 2018.04.09 19:25
author: 杨龙（Alex）
'''
import datetime

d1 = datetime.datetime.now()
print(d1)
print(type(d1))

d2 = datetime.datetime(2020, 10, 1, 10, 10, 10, 1234)
print(d2)
print(type(d2))

d3 = d1.strftime('%Y-%m-%d %X')
print(d3)
print(type(d3))

d4 = datetime.datetime.strptime(d3, '%Y-%m-%d %X')
print(d4)

d5 = datetime.datetime(2020, 10, 1, 0, 0, 0, 123456)
d6 = datetime.datetime.now()
d7 = d5 - d6
print(d7)
print(type(d7))
print(d7.days)
print(d7.seconds)

# 作业:
# 1.计算距离2018-5-1 00:00:00,放假时间,还有多少天,多少小时,多少秒
d8 = datetime.datetime(2018, 5, 1, 0, 0, 0)
d9 = datetime.datetime.now()
d10 = d8 - d9
print(d10.days)
print(d10.seconds)
print('%d天 %d小时 %d秒' % (d10.days, d10.seconds // 3600, d10.seconds % 3600))

# 2.计算我们放假离校时间,2018-4-30 17:45:00的时间
d11 = datetime.datetime(2018, 4, 30, 17, 45, 0)
d12 = datetime.datetime.now()
d13 = d11 - d12
print(d13.days)
print(d13.seconds)
print('%d天 %d小时 %d秒' % (d13.days, d13.seconds // 3600, d13.seconds % 3600))


'''
title: time模块 练习
time: 2018.04.09 19:25
author: 杨龙（Alex）
'''
import time

# 当前时间的时间戳
t1 = time.time()
print(t1)

# 将时间戳转换成UTC时间
t2 = time.gmtime(t1)
print(t2)

# 将时间戳转换成本地时间
t3 = time.localtime(t1)
print(t3)

#将时间格式转换成时间戳，单位是 s, 返回一个浮点数
t4 = time.mktime(t3)
print(t4)

# 将本地时间转换为用户可读的字符串格式时间
t5 = time.asctime(t3)
print(t5)
print(type(t5))

# 将当前时间的时间戳转换为用户可读的字符串格式时间
t6 = time.ctime(t1)
print(t6)
print(type(t6))

# 时间字符串的格式化输出
t7 = time.strftime('%Y-%m-%d %X', t2)
print(t7)
t8 = time.strftime('%Y-%m-%d %X', t3)
print(t8)

# 将字符串的时间格式转换成元祖类型的时间格式
t9 = time.strptime(t7,'%Y-%m-%d %X')
print(t9)





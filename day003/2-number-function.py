'''
title:数学函数练习
time：2018.03.29 16:45
author:杨龙（Alex）
'''

# abs() 函数  返回数字的绝对值
print(abs(123))
print(abs(-123))
print(abs(123.45))
print(abs(-123.78))

# max() 函数  返回给定参数中的最大值
num1 = 234
num2 = 45
num3 = 789
print(max(num1, num2, num3))

# min() 函数  返回给定参数中最小的值
print(min(num1, num2, num3))

# pow() 函数  求幂(求次方)
print(pow(5, 3))  # ===> 5**3

# round() 函数  四舍五入,如果只有一个参数,默认不保留小数点.  第二个参数: 表示精度，小数点后保留的位数
print(round(3.1415926))
print(round(3.1415926, 1))
print(round(4.678, 2))

# import 用来导入模块的,可以在文件的任何地方写  写法: import moudle
import math

# math.ceil()  向上取整
print(math.ceil(19.67))
print(math.ceil(15.134))

# math.floor()  向下取整
print(math.floor(15.134))
print(math.floor(15.999))

# math.sqrt()  求开方
print(math.sqrt(25))
print(math.sqrt(18))

# math.modf()  返回参数的整数部分和小数部分
print(math.modf(13.3546))

# 随机数模块
import random

# random.choice()  返回列表,元组中的某一个值
print(random.choice([12, 32, 4, 6, 75]))

# random.random()  返回0-1之间的数,  [0, 1)
print(random.random())

# random.uniform()  返回指定的一个区间范围的随机数  [1, 10)
print(random.uniform(1, 10))

# random.shuffle()  将列表中的数据进行打乱排序
list1 = [12, 32, 4, 6, 75]
random.shuffle(list1)
print(list1)









'''
title:位运算符的练习
time：2018.03.28 17:00
author:杨龙（Alex）
'''

num1 = int(input("请输入第一个数字："))
num2 = int(input("请输入第二个数字："))

# 按位与
print(num1 & num2)

# 按位或
print(num1 | num2)

#按位异或
print(num1 ^ num2)

#按位取反
print(~num1)
print(~num2)

#按位左移
print(num1 << 2)
print(num2 << 2)

#按位右移
print(num1 >> 2)
print(num2 >> 2)

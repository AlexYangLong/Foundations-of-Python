'''
title:input()函数练习
time：2018.03.28 11:30
author:杨龙（Alex）
'''

#input()函数  输入  接受一个标准输入数据，返回值为 string 类型
name = input("请输入你的名字：")
print(name)

num1 = input("请输入第一个数字：")
num2 = input("请输入第二个数字：")
print("和为：", int(num1) + int(num2))
print("%s + %s = %d" % (num1, num2, int(num1) + int(num2)))
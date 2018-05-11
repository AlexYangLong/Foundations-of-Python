'''
title: 分支语句 if 、 if-else 、 if-elif-...-else 练习
time: 2018.03.30 17:00
author: 杨龙（Alex）
'''

'''
第一种: if
格式: if 表达式:
        语句块
执行流程:执行时,先判断表达式的值,如果为真,则执行语句块,否则结束if结构
'''
num = int(input("请输入一个数："))
if num > 10:
    print('YES')
'''
注意：表达式为假的情况: 0 '' None  False []  ()  {}
'''

print('****************')
# 使用第三个变量交换两个变量的值
num1 = 111
num2 = 345
tmp = 0
if num1 < num2:
    tmp = num1
    num1 = num2
    num2 = tmp
    print(num1, num2)

print('****************')
#不使用第三个变量交换两个变量的值
num1 = 111
num2 = 345
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
print(num1, num2)

print('*****************************')
'''
第二种: if-else
格式: if 表达式:
        语句块1
      else:
        语句块2
执行流程:执行时,先判断表达式的值,如果为真,则执行语句块1,如果为假,则执行else中的语句块的内容
'''
money = int(input('请输入你的薪资:'))
if money < 3500:
    print('不开心')
else:
    print('哈哈哈')
print('****************')
# 判断一个年份是否是闰年
year = int(input('请输入一个年份:'))
if ((year % 4 == 0) and (year % 100 != 0))  or (year % 400 == 0):
    print('是闰年')
else:
    print('不是闰年')


print('**************************************')
'''
第三种: if-elif-else
格式: if 表达式1:
        语句块1
      elif 表达式2:
        语句块2
      elif 表达式3:
        语句块3
      ...
      else:
        语句块n
执行流程:执行时,判断表达式1的值,如果为真,则执行语句1,否则判断表达式2的值,如果为真,则执行语句块2,以此类推,否则,就执行else里边的语句块n
'''
score = int(input('请输入一个分数：'))
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('E')

'''
第四种: 分支嵌套
格式：if  表达式1:
        if 表达式2:
            语句块1
        else:
            语句块2
      else:
      	语句块3
执行流程:执行时,判断表达式1的值,如果为真,则继续判断表达式2的值,如果为真,则执行语句块1,,否则执行语句块2,如果表达式1的值为假,就执行语句块3
'''
name = 'Alex'
password = '123'

user = input('请输入用户名：')
passwd = int(input('请输入密码：'))

if user == name:
    if passwd == password:
        print('恭喜你,登录成功')
    else:
        print('用户名或者密码错误2')
else:
    print('用户名或者密码错误1')
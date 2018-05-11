'''
title: 循环语句 while、for-in 及 break、continue 练习
time: 2018.03.30 17:30
author: 杨龙（Alex）
'''

'''
while：
格式：while 表达式：
        语句块
执行流程：当表达式为真时，执行语句块，否则不执行
'''
# 输出1-100的值，用 ， 分割
i = 0
while i < 100:
    i += 1
    print(i, end = ',')
print('\n')

# 死循环
# import time
# #while True
# while 1:
#     print('endless loop')
#     time.sleep(2)


#人在江湖飘
import random
import time
while 1:
    Alex = random.randint(1, 5)
    XiaoMing = random.randint(1, 5)
    # 求两个个出的数字差
    dVal = Alex - XiaoMing
    if (abs(dVal) == 1) or (abs(dVal) == 4):
        #输赢已产生
        if (dVal == 1) or (dVal == -4):
            print('Alex赢了，XiaoMing喝')
        else:
            print('XiaoMing赢了，Alex喝')
        break
    else:
        print('Alex和XiaoMing旗鼓相当,继续!')
        time.sleep(2)

print('**************************************************')
'''
for  in
'''
str1 = 'I\'s your lucky day!'
# 遍历字符串
for i in str1:
    print(i, end = ',')
print()

# 遍历列表
list1 = ['Alex', 'John', 'Ala', 'Lilei', 'Hanmeimei']
# 注意：else是for遍历完成之后才执行
for i in list1:
    print(i)
else:
    print('看你是否遍历结束')

# 遍历一堆数字
for i in range(10):
    print(i, end = ',')
print()

#遍历set集合 ， 是无序的
dict1 = {'Alex', 'John', 'Ala', 'Lilei', 'Hanmeimei'}
for i in dict1:
    print(i, end = ',')
print(dict1)

print('**************************************************')
'''
break: 中断,跳出循环
注意: 一般情况下用在 for  while  if  里边
表示跳出整个循环
'''
for i in range(10):
    print(i)
    if i == 4:
        break
print()

num = 1
while num < 10:
    print(num)
    if num == 5:
        break
    num += 1
else:
    print('已经结束了')
# 注意：程序遇到break,就会跳出整个结构,包括else后边的代码也不再执行


print('**************************************************')
'''
continue: 跳出本次循环,后边代码不再执行,进入下次循环
'''
for i in range(10):
    print(i)
    if i == 5:
        continue
    print('&&&')
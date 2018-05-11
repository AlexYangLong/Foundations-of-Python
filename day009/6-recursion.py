'''
title: 递归 练习
time: 2018.04.08 16:20
author: 杨龙（Alex）
'''

'''
递归调用:一.个函数,调用了自身即是递归
三要素:
1.写出临界条件
2.返回上一级和下一级之间的关系
3.根据上一次计算出的结果求出本次计算的结果
'''

# 使用递归求 1*2*3...*n
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

print('**************************************')

# 使用递归求 1 + 2 + ... + n
def resucsionAdd(n):
    if n == 1:
        return 1
    return n + resucsionAdd(n-1)

print(resucsionAdd(100))

# 使用循环求 1 + 2 + ... + n
def circleAddByFor(n):
    sum = 0
    for i in range(n):
        sum += (i + 1)
    return sum
print(circleAddByFor(100))
# 使用循环求 1 + 2 + ... + n
def circleAddByWhile(n):
    sum = 0
    i = 1
    while i <= n:
        sum += i
        i += 1
    return sum
print(circleAddByWhile(100))

print('**************************************')

import os

# 使用递归遍历目录下所有文件
def getAllFileAndDir(path, spaceStr=''):
    FilesList = os.listdir(path)

    spaceStr += '   '

    for filename in FilesList:
        filePath = os.path.join(path, filename)
        if os.path.isdir(filePath):
            print(spaceStr + '目录：' + filename)
            getAllFileAndDir(filePath, spaceStr)
        else:
            print(spaceStr + '文件：' + filename)

getAllFileAndDir('../0408')

'''
title: 生成器
time: 2018.04.13 19:20
author: 杨龙（Alex）
'''

'''
generator和函数的执行流程不一样。
函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
'''

def test_yield(n):
    for i in range(n):
        yield func(i)
        print('i =', i)
    print('lalalalla....')
    print('end')

def func(n):
    return n * 2

for i in test_yield(5):
    print(i, end=',')





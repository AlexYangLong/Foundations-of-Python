'''
title: 生成器
time: 2018.04.13 19:25
author: 杨龙（Alex）
'''

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a

def start():
    list1 = list(range(1, 11))
    print(list1)

    list2 = [x * x for x in range(1, 11)]
    print(list2)

    list3 = [m + n for m in 'ABCD' for n in '1234']
    print(list3)

    list4 = [(x, y) for x in range(10) if x%2==0 for y in range(10) if y%3==0]
    print(list4)

    # 生成器, 生成时间长度列表的时间,但是占用空间少
    g1 = (m + n for m in 'ABCD' for n in '1234')
    print(g1)
    for i in g1:
        print(i, end=',')

    print('*********************************************')

    res = fib(20)
    print(res)
    for i in res:
        print(i, end=',')


if __name__ == "__main__":
    start()




'''
title: 迭代器
time: 2018.04.13 19:12
author: 杨龙（Alex）
'''

'''
1.可以使用迭代器访问集合
2.迭代器可以记住遍历的位置
3.迭代器对象从集合的第一个元素开始访问,直到最后一个元素结束,并且迭代器只能前进不能后退
4.iter()   next()
5.通常情况下可以用字符串,列表或者元祖都可以创建迭代器
'''

list1 = [1, 2, 3, 4, 5, 6]
# 创建迭代器对象
it = iter(list1)
print(it)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# 使用循环遍历
for i in it:
    print(i)


import sys

list2 = [2, 3, 4, 5, 6, 7]
it = iter(list2)

while True:
    try:
        print(next(it))
    except StopIteration as e:
        sys.exit('退出')
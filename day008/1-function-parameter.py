'''
title: 函数的参数 ———— 默认参数、不定长参数、关键字参数
time: 2018.04.04 16:35
author: 杨龙（Alex）
'''

# 默认参数
def addList(list1 = []):
    list1.append('end')
    print(list1)
addList([1, 2, 3, 4])

#这样调用会有点问题
addList()
addList()

# 优化代码
# 当调用函数时,不传递任何参数时,需要将形式参数设置为None,解决上述问题
def addList(list1 = None):
    if list1 is None:
        list1 = []
    list1.append('end')
    print(list1)

addList()
addList()
addList([2, 4])


'''
不定长参数: 指的是参数的长度不固定的.
1.不定长参数的长度可以是>=0
2.默认参数合不定长参数都要放到形式参数的最后边
3.在一个文件中可以定义同名的函数
4.当没有实际参数参数时,则形式参数接受的是一个空的元祖
'''
# 求多个数的和
def Sum(*args):
    sum = 0
    for i in args:
        sum += i

    print(type(args))
    return sum

print(Sum(2, 4, 5, 7))


'''
关键字参数: 函数调用时不限制参数
1、**代表键值对的参数,他的用法跟*类似
2、关键字参数得到的结果是一个字典
'''

def showinfo(name, age, **kwargs):
    # print(name, age)
    print(name, age, kwargs)
    print(type(kwargs))

showinfo('Alex', 22, height = 168, hobby = ['a', 12, 'ss'])







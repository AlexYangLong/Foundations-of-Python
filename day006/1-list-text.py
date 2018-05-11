'''
title: list 的方法练习
time: 2018.04.02 18:30
author: 杨龙（Alex）
'''

# 列表的方法
# append(): 在列表的末尾添加一个元素
list1 = [1, 2, 3, 4, 5, 6]
list1.append(8)
print(list1)
list1.append([7, 9, 10])
print(list1)

# extend(): 在列表的末尾一次性追加另外一个列表中的多个值
list2 = [1, 2, 3, 4, 5, 6]
list2.extend([200, 300, 400])
print(list2)

#insert(index, val):在指定下标处添加一个元素,原来此处的元素往后移动  index：表示列表下标，val：表示下标对应的值
list3 = [1, 2, 3, 4]
list3.insert(1, 250)
print(list3)

# pop([index]):将列表中指定下标的元素删除, 如果不传递参数,则删除的是最后一个元素  index：表示列表下标，返回值：删除的该元素
list4 = [1, 2, 3, 4, 5, 6]
print(list4.pop())
list4.pop()
print(list4)
list4.pop(1)
print(list4)

# remove(val): 移除列表中指定的元素，从左开始，移除第一个  val：表示列表中的值
list5 = [3, 4, 5, 6, 3, 7]
list5.remove(3)
# list5.remove(3)
print(list5)

# clear(): 清除列表中所有的元素
list6 = [1, 2, 3, 4, 5, 6]
list6.clear()
print(list6)

# index(val): 获取列表中该元素所对应的下标  val：列表中的某一个元素  返回值：列表中元素所对应的下标
list7 = [1, 2, 3, 4, 5, 6]
index1 = list7.index(3)
print(index1)

# len(list): 获取列表的长度
print(len([1, 2, 3, 4, 5, 6]))

# max(list): 获取列表中的最大值
print(max([1, 2, 3, 4, 5, 6]))

# min(list): 获取列表中的最小值
print(min([1, 2, 3, 4, 5, 6]))

# count(val): 计算列表中元素出现的次数  val：列表中的某一个元素
list8 = [1, 3, 4, 3, 3, 3, 3, 6, 7]
print(list8.count(3))

# reverse(): 将列表进行倒序排列
list9 = [1, 2, 3, 4, 5, 10, 7, 8, 9]
list9.reverse()
print(list9)

# sort(): 将列表中的元素进行升序排列
list10 = [10, 90, 78, 23, 65, 43]
list10.sort()
print(list10)

# 引用传递: 在列表中,如果修改一个列表的元素,那么对应的另外一个列表的元素也改变
list11 = [1, 2, 3, 4]
list12 = list11
list12[1] = 10
print(list11)
print(list12)
# id(): 查看内存的地址
print(id(list11))
print(id(list12))

# 值传递：在列表中修改一个元素的值时,对应的另外一个列表中的值是不发生改变的
list13 = [1, 2, 3, 4]
list14 = list13.copy()
list14[1] = 20
print(list13)
print(list14)
print(id(list13))
print(id(list14))

list15 = ['Alex', 'XiaoMing', 'Ala', 'Jhon', 'Tom']
'''
enumerate(list[, start = 0]):将列表中元素和其对应的下标一一展示出来
list: 列表
start: [start = 下标值]
'''
list16 = list(enumerate(list15))
list17 = list(enumerate(list15, start = 1))
print(list16)
print(list17)

for i, v in list16:
    print(i, v)
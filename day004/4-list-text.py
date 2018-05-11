'''
title: list类型 练习
time: 2018.03.30 18:30
author: 杨龙（Alex）
'''

'''
列表list:
格式: 列表名 = [列表值1, 列表值2, 列表值3, ... , 列表值n]
列表是一个有序集合
'''

# 创建一个空列表
list1 = []
print(list1)
print(type(list1))

# 创建带有元素的列表
list2 = [1, 2, 3, 4, 5, 6, 7, 8]
print(list2)

# 列表元素的类型可以不同
list3 = [12, 'qwe', 0.87, False, None]
print(list3)

# 访问列表中的元素  格式: 列表名[元素的下标] 注意：下标不能超出列表的范围，最大为len(list)-1
list4 = [1, 2, 3, 4, 5, 6, 7, 8]
print(list4[5])

# 修改元素
list4[3] = 10
print(list4)

# 列表的操作
# 列表拼接
list5 = [1, 2, 3, 4]
list6 = [5, 6, 7]
list7 = list5 + list6
print(list7)

# 列表的重复
list8 = [4, 5, 6]
print(list8 * 3)

# 判断一个元素是否在列表中
list9 = [1, 2, 3, 4, 5, 6]
# 返回的结果是布尔值 存在为True  不存在为False
print(7 in list9)
print(4 in list9)

# 截取列表 list[start:end:step]
list10 = [1, 2, 3, 4, 5, 6, 7, 8]
print(list10[:6])  # 从左截取，从头开始，到下标为5的元素
print(list10[5:])  # 从左截取，从下标为5的元素，到末尾
print(list10[::-1])  # 将list倒序排列
print(list10[::-2])  # 从右截取，末尾开始，每隔一个元素截取一个


# 二维列表
list11 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 获取元素
print(list11[0][0])


# 列表的方法
# append(): 在列表的末尾添加一个元素
list12 = [1, 2, 3, 4, 5, 6]
list12.append(8)
print(list12)
list12.append([7, 9, 10])
print(list12)
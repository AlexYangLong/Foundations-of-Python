'''
title: list、tuple、dict、set 数据类型转换练习
time: 2018.04.02 19:40
author: 杨龙（Alex）
'''

#list-set
list1 = [1, 2, 3, 4, 4, 5, 5]
set1 = set(list1)
print(set1)
print(type(set1))

# set->list
set2 = {1, 2, 3, 4, 5, 6}
list2 = list(set2)
print(list2)
print(type(list2))

# tuple->set
tuple1 = (1, 2, 3, 4, 5, 6, 6, 6)
set3 = set(tuple1)
print(set3)
print(type(set3))

# set->tuple
set4 = {1, 2, 3, 4, 5, 6}
tuple2 = tuple(set4)
print(tuple2)
print(type(tuple2))

# dict->set
dict1 = {'Alex': 88, 'xiaoming' : 99, 'Ala': 96, 'Tom': 85, 'Jhon': 77}
set5 = set(dict1)
print(set5)
print(type(set5))

# set-dict  注意：set不能转换成dict，因为set只有key，而dict是key-value形式存储的
# set6 = {2, 3, 4, 5}
# dict2 = dict(set6)
# print(dict2)











'''
title: tuple 的方法练习
time: 2018.04.02 18:50
author: 杨龙（Alex）
'''

# 创建一个空元组
tuple1 = ()
print(tuple1)
print(type(tuple1))

# tuple和list一样也可以保存任意数据类型的数据
tuple2 = (231, 323.14, 'asddf', None, True)
print(tuple2)

# 注意：当创建的元组只有一个元素时，需要在元素后面加一个逗号
tuple3 = (34, )  # tuple3 = (34)  # ===> int类型
print(tuple3)

# 获取元组的元素和list一样，通过下标来获取
tuple4 = (1, 2, 3, 4, 5, 6)
print(tuple4[-1])

# 注意：元组定义好之后是不能修改的
tuple5 = (1, 2, 3, 4, [11, 22, 33])
# tuple5[0] = 150  # 报错
print(tuple5[-1][-2]) #  ==> print(tuple5[4][1])

# 删除元组的用法跟删除变量的用法一致
tuple6 = (1, 2, 3, 5, 6)
del tuple6
# print(tuple6)

# 元组进行操作
# 将两个元组合并成一个新的元组
tuple7 = (1, 2, 3)
tuple8 = (4, 5, 6)
tuple9 = tuple7 + tuple8
print(tuple9)
print(tuple7, tuple8)

# 将元组重复n次,最后返回一个新的元组
tuple10 = (1, 2, 3)
print(tuple10 * 3)

# in 判断一个元素是否在一个元组中,如果在返回True,否则返回False
tuple11 = (3, 5, 7)
print(3 in tuple11)
print(4 in tuple11)

# 元组的截取
# 格式: 元组名[start:end:step]
tuple12 = (1, 2, 3, 4, 5, 6, 7, 8, 9,10)
print(tuple12[2:5])
print(tuple12[3:])
print(tuple12[:3])
# 将元组进行逆序排列
print(tuple12[::-1])

# 二维元组
tuple13 = ((2, 3, 4), (5, 6, 7))
print(tuple13)
print(tuple13[1][1])

# 元组的方法
# len(): 求一个元组的长度
tuple14 = (1, 2, 3, 4, 5)
print(len(tuple14))
# max(): 求一个元组的元素的最大值
print(max(tuple14))
# min(): 求一个元组的元素的最小值
print(min(tuple14))

#遍历
for i in tuple14:
    print(i)


# 将列表转换成元组
tuple15 = tuple([1, 2, 3, 4])
print(tuple15)

# 将元组转换成列表
list16 = list((1, 2, 3, 4))
print(list16)






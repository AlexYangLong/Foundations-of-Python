'''
title: set 的方法练习
time: 2018.04.02 19:30
author: 杨龙（Alex）
'''

'''
set(集合):类似于dict, 也是无序的,以key的形式存在,没有value
作用: 是对list,tuple进行去重的, 求交集、并集
1.set是无序集合
2.set集合是不可改变的
'''

set1 = set([1, 2, 2, 3, 3, 3])
print(set1)
print(type(set1))
set2 = set((1, 2, 3, 1, 2, 3, 4, 5))
print(set2)
print(type(set2))
set3 = set({3, 4, 5, 5, 6, 3, 7})
print(set3)
print(type(set3))

# 添加
set4 = set([1, 2, 2, 3, 3, 3])
set4.add(55)  # add() #可以添加重复的值,但是没效果

# set4.add([10, 9]) #直接报错,不能添加list
set4.add((10, 9))
# set4.add({'a':1}) #直接报错,不能添加字典
# 总结:list和dict是可改变的, 而tuple是不可改变
print(set4)

# 修改
set5 = set([1, 2, 3, 4, 5])
# 将list dict tuple 等等整个插入进去
set5.update([6, 7, 8])
set5.update({9 : 'a', 10 : 'b'})  #注意：插入字典时，是将key插进去
set5.update((11, 56))
print(set5)

# 删除
set6= set([1, 2, 3, 4, 5])
set6.remove(4)
print(set6)

# 遍历
set7 = set((231, 323.14, 'asddf', None, True))
for i in set7:
    print(i)

# 交集  &  并集  |
set8 = set([1, 2, 3, 4])
set9 = set([3, 4, 5, 6])
set10 = set8 & set9
set11 = set8 | set9
print(set10)
print(type(set10))
print(set11)
print(type(set11))


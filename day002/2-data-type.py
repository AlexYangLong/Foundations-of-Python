'''
title:python的数据类型的练习
time：2018.03.28 11:35
author:杨龙（Alex）
'''

#type():   查看变量的数据类型

#数字型  在python语言中,整型和浮点型都属于数字型
print(type(111))
print(type(13.14))

#字符串型
print(type('查看变量的数据类型'))
print(type('Alex'))

# 布尔类型:  True   False
print(type(True))
print(type(False))

#空类型
print(None)
print(type(None))

#列表类型
print(type([]))

#元组类型
print(type(()))

#字典类型
print(type({}))

#set集合类型
list = [1,2,3,4]
print(type(set(list)))




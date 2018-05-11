'''
title: dict 的方法练习
time: 2018.04.02 19:15
author: 杨龙（Alex）
'''

'''
dict：在字典里边是以键值对的形式存放. key-value
注意事项:
1.在字典中键(key)的值必须是唯一
2.在字典中可以存放多个键值对
3.在字典中键(key)必须是不可变类型   字符串 、整数都可以作为键(key)
4.list和tuple都是有序集合, 而dict是无序集合
'''

# 定义字典
dict1 = {'Alex': 88, 'xiaoming' : 99, 'Ala': 96, 'Tom': 85, 'Jhon': 77}
print(dict1)

# 元素的访问
# 获取的方式: 字典名[key]
print(dict1['xiaoming'])
print(dict1.get('Alex'))

# 添加元素
dict1['HanMeimei'] = 89
print(dict1)

# 修改
dict1['HanMeimei'] = '90'
print(dict1)

# 删除
dict1.pop('HanMeimei')
print(dict1)

# 遍历
for k in dict1:
    print(k, dict1[k])

# 获取字典所有的value和key
print(dict1.values())
print(dict1.keys())

# 遍历value值
for v in dict1.values():
    print(v)

#遍历key值
for k in dict1.keys():
    print(k)

#遍历key-value值
for k,v in dict1.items():
    print(k, v)

for k,v in enumerate(dict1):
    print(k, v)



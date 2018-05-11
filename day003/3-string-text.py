'''
title:字符串练习
time：2018.03.29 17:00
author:杨龙（Alex）
'''

# 单行字符串
str1 = '获得，源于付出，实在改变。'
str2 = "幸福不是从天而降，需要用双手去创造。财富、事业、家庭、梦想，人生价值和社会价值在创造中收获统一。"

# 多行字符串
str3 = '''
床前明月光，
疑似地上霜。
举头望明月，
低头思故乡。
'''

str4 = """
风住尘香花已尽，日晚倦梳头。
物是人非事事休，欲语泪先流。
闻说双溪春尚好，也拟泛轻舟。
只恐双溪舴艋舟，载不动许多愁。
"""

print(str1)
print(str2)
print(str3)
print(str4)

# len() 函数  获取字符串的长度
print(len(str1))

'''
提取字符串中的某一个字符
方式:
从左往右开始, 下标从0开始提取
str[0]   str[1]   str[2] ..... str[n-1]
从优往左开始, 下标从-1开始
str[-1]  str[-2] .....  str[-n]
'''
print(str1[3])

# 注意 ： pytjon中的字符串一旦定义好之后,是不可以修改的
#str1[0] = '元'    #  报错
#print('str1 =', str1)

# * 将字符串拼接n次
str5 = 'Alex'
print(str5 * 3)

# + 表示字符串与字符串变量之间的拼接 ， 如果接字符串以外的其他数据类型会报错
str6 = 'xiaoming'
print(str5 + str6)
#print(str5 + 12345)  #  报错


'''
字符串截取:
str1[开始下标:结束下标]:  从开始下标截取,到结束下标=结尾,.包含开始下标,但不包含结束下标
str1[0:5] 提取是的结果你是zhous
str1[:3] 默认从下标0开始到结束的开区间
str1[3:] 从指定的下标开始到结尾
str1[-n:]: 从最后边提取n个
str1[:]:  提取全部字符
str1[::2]  根据下标每个n个提取一次
str1[::-1]  将字符逆序排列
'''
str1 = 'Alex and xiaoming'
str2 = str1[2:5]
str2 = str1[:4]
str2 = str1[5:]
str2 = str1[-2:]
str2 = str1[:]
str2 = str1[::3]
str2 = str1[::-1]
str2 = str1[::-3]

print(str2)

'''
字符串比较大小：
规则:从第一个字符开始比较,将字符转换成ascii值进行比较
如果小于则返回True,否则返回False
'''
print('a' > 'b')  # False
print('aaaaa' < 'bbbbb')#True
print('asdf' < 'asdfg')#True









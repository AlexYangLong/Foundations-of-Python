'''
title: 字符串函数整理
time：2018.04.03 18:55
author: 杨龙（Alex）
'''

# split(str=' '[,num])  对字符串进行切片，并返回一个列表，str 表示按此字符串进行分割，默认是空格，num 表示最多分割多少次
str1 = 'aaa sss ddd fff hhh'
print(str1.split(' ', 3))

# splitlines() 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符，默认是False
str2 = '''aaaaaaaaaa
ssssssssssssssssss
dddddddd
'''
print(str2.splitlines(keepends=True))
print(str2.splitlines(keepends=False))

# join(): 用于将序列中的元素以指定的字符连接生成一个新的字符串
str3 = 'asdfghj'
list = ['a','s','e']
print('-'.join(list))
print('-'.join(str3))

# max():返回给定参数的最大ASCII值的字符，参数可以为序列
print(max('asdfghj'))
# min():返回字符串中最小ASCII值的字符
print(min('asdfghj'))

# replace(old, new[, max]):把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次
print('asdfghjkasasas'.replace('a', '1', 2))

# maketrans():返回字符串转换后生成的新字符串
# translate(table):返回按照table中给出的映射来进行翻译后的字符串
trantab = str.maketrans('abcd', '1234')
print('asdfghjkasasas'.translate(trantab))
print('asdfghjkasasas'.translate(trantab))

# startswith(str, beg=0,end=len(string)):方法用于检查字符串是否是以指定子字符串开头，如果是则返回 True，否则返回 False。如果参数 beg 和 end 指定值，则在指定范围内检查
print('asdfghjkasasas'.startswith('asd', 2, 10))
# endswith(suffix[, start[, end]]):方法用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回True，否则返回False。可选参数"start"与"end"为检索字符串的开始与结束位置
print('asdfghjkasasas'.endswith('ghj', 0, 7))

# encode():指定的编码格式编码字符串
print('asdfg'.encode('utf-8'))
# decode():以指定的编码格式解码 bytes 对象。默认编码为 'utf-8'。
print(('asdfg'.encode('utf-8')).decode('utf-8'))

# isalpha():方法检测字符串是否只由字母组成
print('asdfg12'.isalpha())
# isalnum():检测字符串是否由字母和数字组成。
print('123456asd'.isalnum())
# isupper():检测字符串中所有的字母是否都为大写。
print('ASDFGd'.isupper())
# islower():检测字符串是否由小写字母组成。
print('Asdfghjkrt5'.islower())
# istitle():检测字符串中所有的单词拼写首字母是否为大写，且其他字母为小写。
print('My Name Is Alex'.istitle())
# isdigit():检测字符串是否只由数字组成
print('12345678'.isdigit())
# isnumeric():检测字符串是否只由数字组成。这种方法是只针对unicode对象
print('1234567'.isnumeric())
# isdecimal():检查字符串是否只包含十进制字符。这种方法只存在于unicode对象
print('12345'.isdecimal())
# isspace():检测字符串是否只由空白字符组成
print('            '.isspace())

# len():返回对象（字符、列表、元组等）长度或项目个数
print(len('asdfghj234567'))

# lower():转换字符串中所有大写字符为小写
print('ASDasdfgerty3456'.lower())
# upper():将字符串中的小写字母转为大写字母。
print('ASDasdfgerty3456'.upper())
# swapcase():用于对字符串的大小写字母进行转换。
print('ASDasdfgerty3456'.swapcase())
# capitalize():将字符串的第一个字母变成大写,其他字母变小写
print('asd WERtsd3456'.capitalize())
# title():返回"标题化"的字符串,就是说所有单词都是以大写开始
print('my name is Alex'.title())

# center(width[, fillchar]):返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格
print('asd1'.center(10,' '))

# ljust(width[, fillchar]):返回一个原字符串左对齐,并使用fillchar填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串
print('asd1'.ljust(10,' '))
# rjust(width[, fillchar]):回一个原字符串右对齐,并使用fillchar填充至长度 width 的新字符串。如果指定的长度小于字符串的长度则返回原字符串
print('asd1'.rjust(10,' '))
# zfill(width):返回指定长度的字符串，原字符串右对齐，前面填充0
print('asd1'.zfill(10))

# count():统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置
print('aaaaaaaqwertya'.count('a'))

# find():方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果指定范围内如果包含指定索引值，返回的是索引值在字符串中的起始位置。如果不包含索引值，返回-1
print('asdfghjkl'.find('fg1'))
# rfind():返回字符串最后一次出现的位置，如果没有匹配项则返回-1
print('asdfghjklfg'.rfind('fg'))

# index():方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，该方法与 python find()方法一样
print('asdfghjkl'.find('fg'))
print('asdfghjkl'.find('fg1'))

# rindex():返回子字符串 str 在字符串中最后出现的位置，如果没有匹配项则返回-1
print('asdfghjklfg'.rfind('fg'))
print('asdfghjkl'.rfind('fg1'))

# strip():用于移除字符串头尾指定的字符（默认为空格）
print('      asd   '.strip())
# lstrip():方法用于截掉字符串左边的空格或指定字符（默认为空格）
print('      asd   '.lstrip())
# rstrip():删除 string 字符串末尾的指定字符（默认为空格）
print('      asd   '.rstrip())
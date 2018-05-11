'''
title: os模块 练习
time: 2018.04.09 18:18
author: 杨龙（Alex）
'''

import os

# 获取当前操作系统 windows-nt  posix->linux,unix 或者mac os x
print(os.name)
# 查看当前操作系统的详细信息,但是不支持windows操作系统
# print(os.uname())
# 获取当前操作系统的环境变量,返回一个dict
print(os.environ)
print(os.environ.keys())
print(os.environ.values())
print(os.environ.get('APPDATA'))
# 获取当前目录
print(os.curdir)
# 获取当前的绝对路径
print(os.getcwd())
# 列出路径下所有的目录和文件，该路径不能是文件
print(os.listdir(r'D:\for python\0409'))
# 创建目录
# os.mkdir(r'D:\for python\0409\text')
# os.mkdir('./text2')

# 删除目录, 只能删除空目录
# os.rmdir(r'D:\for python\0409\text')
# os.rmdir(r'D:\for python\0409\test')
# os.rmdir('./text2')

# 对文件进行重命名
# os.rename('text2', 'test')
# 获取文件属性
print(os.stat('1-os-text.py'))
# 删除文件
# os.remove('./test/111.txt')

# 路径拼接
path1 = r'D:\for python\0409'
path2 = 'alex'
# 注意:在参数二处尽量不要写 /
print(os.path.join(path1, path2))

# 拆分路径
print(os.path.split(r'D:\for python\0409'))
print(os.path.split(r'D:\for python\0409\1-os-text.py'))

# 拆分文件的扩展名
path1 = 'D:/for python/0409/1-os-text.py'
print(os.path.splitext(path1))

# 判断是否是目录,是返回True  否返回False
print(os.path.isdir(path1))
# 判断目录或文件存不存在
print(os.path.exists(path1))
# 判断是否是文件
print(os.path.isfile(path1))

# 获取文件的大小
print(os.path.getsize(path1))

# 获取当前文件的目录
print(os.path.dirname(path1))

# 获取当前文件名
print(os.path.basename(path1))
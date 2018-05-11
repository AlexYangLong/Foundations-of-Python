'''
title: 正则简单操作
time: 2018.04.14 17:22
author: 杨龙（Alex）
'''

import re

def func():
    #创建表达式对象
    pattern = re.compile(r'(?<=\D)(13[0-9]{9}|14[57]\d{8}|15[0-35-9]\d{8}|17[678]\d{8}|18\d{9})(?=\D)')

    content = '我的手机号是18408260044,而他的手机号是18408250000,不是他而是她的手机号是1218408260001,然后问他要了他的qq号是:12345678900.......'

    list1 = re.findall(pattern, content)
    print(list1)

if __name__ == '__main__':
    func()
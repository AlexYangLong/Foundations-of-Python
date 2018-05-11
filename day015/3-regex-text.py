'''
title: 正则简单操作
time: 2018.04.14 17:10
author: 杨龙（Alex）
'''

import re

def validate():
    # 只能是数字,字母_组合,4-12位
    username = input('请输入用户名：')
    # 规则: 至少6位,数字字母.下滑
    password = input('请输入密码：')
    tel = input('请输入手机号：')

    reg1 = re.match(r'[0-9a-zA-Z_]{4,12}', username)
    reg2 = re.match(r'\w{6,}', password)
    reg3 = re.match(r'1[3456789]\d{9}', tel)

    if not reg1:
        print('用户名格式错误，4-20由数字,字母,下划线组成')
    elif not reg2:
        print('密码格式错误，至少6位,数字字母,下划线组成')
    elif not reg3:
        print('手机号格式不正确')
    elif reg1 and reg2 and reg3:
        print('提交信息成功！')

if __name__ == '__main__':
    validate()
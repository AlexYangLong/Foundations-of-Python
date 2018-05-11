'''
title: 发送邮件
time: 2018.04.12 17:05
author: 杨龙（Aelx）
'''
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# smtp邮件服务器地址
smtpServer = 'smtp.163.com'

# 发送人
sender = '18408260044@163.com'

# 授权密码
password = 'yl952001'

# 接受人列表
receiveList = ['18408260044@163.com', '18408257304@163.com']

# 邮件内容
content = '这是一封测试邮件'

# 将邮件内容转换成邮件格式
Message = MIMEText(content)

# 添加邮件主题、标题
Message['Subject'] = '一封来自未来的邮件'

# 添加邮件发送者
Message['From'] = sender

# 创建smtp邮件服务器
mailServer = smtplib.SMTP(smtpServer, 25)

# 授权登录
mailServer.login(sender, password)

# 发送邮件
mailServer.sendmail(sender, receiveList, Message.as_string())

# 退出邮箱
mailServer.quit()













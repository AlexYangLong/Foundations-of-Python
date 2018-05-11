'''
title: tkinter 简单操作
time: 2018.04.14 16:25
author: 杨龙（Alex）
'''

import tkinter
import tkinter.messagebox

# 创建主窗口
inter = tkinter.Tk()
# 设置窗口大小
inter.geometry('500x400')
# 设置窗口的标题
inter.title('用户界面')
# 创建label 并设置字体、大小、颜色
label = tkinter.Label(inter, text = 'username,password', font = 'Arial -32', fg = 'red')
label.pack()
# 创建按钮容器
panel = tkinter.Frame(inter)
panel.pack(side = 'bottom')

# 将按钮绑定到panel上
button1 = tkinter.Button(panel, text = '添加')
button1.pack(side = 'left')

button2 = tkinter.Button(panel, text = '退出')
button2.pack(side = 'right')

# 添加循环组件
tkinter.mainloop()
'''
title: turtle 简单使用
time: 2018.04.04 17:14
author: 杨龙（Alex）
'''
import turtle
#设置屏幕大小
turtle.screensize(600, 500)
# write()往turtle中写内容   normal(正常)  italic(斜体)
# turtle.write('Alex,Hello World!', font=('微软雅黑', 30, 'normal'))
# 隐藏画笔
turtle.hideturtle()
# 显示画笔
turtle.showturtle()

# 开始填充
turtle.begin_fill()
# 给画笔填充颜色
turtle.color('orange')
turtle.circle(100, steps = 10)
turtle.end_fill()

# 重置屏幕
turtle.reset()

# 画笔笔触的大小
turtle.pensize(5)
turtle.begin_fill()
turtle.color('red')
turtle.circle(50, steps = 6)
turtle.end_fill()

turtle.hideturtle()

turtle.done()














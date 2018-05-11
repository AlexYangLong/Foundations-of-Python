'''
title: turtle 简单使用
time: 2018.04.04 17:27
author: 杨龙（Alex）
'''
import turtle

turtle.pensize(10)

turtle.color('black')
turtle.circle(100)

# 笔触抬起
turtle.penup()
# 笔触点移动到另一个坐标点 x轴向左移是负的,向右移动是正的.y轴向上移动是正的,向下移动是负的
turtle.goto(-200, 0)
# 笔触放下
turtle.pendown()

turtle.color('blue')
turtle.circle(100)

turtle.penup()
turtle.goto(200, 0)
turtle.pendown()
turtle.color('red')
turtle.circle(100)

turtle.penup()
turtle.goto(100, -170)
turtle.pendown()
turtle.color('green')
turtle.circle(100)

turtle.penup()
turtle.goto(-100, -170)
turtle.pendown()
turtle.color('yellow')
turtle.circle(100)

turtle.hideturtle()

turtle.done()


























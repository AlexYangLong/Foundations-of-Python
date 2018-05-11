'''
title: 日历模块 练习
time: 2018.04.09 19:35
author: 杨龙（Alex）
'''

import calendar

# 获取指定的月份的日历
print(calendar.month(2018, 5))

# 获取指定年份全年日历
print(calendar.calendar(2018))

# 参数一返回上个月的最后一天对应的星期
# 参数二返回当月的天数
print(calendar.monthrange(2018, 5))

# 返回一个二级列表, 并且每个单独的二级列表是以周为单位
print(calendar.monthcalendar(2018, 4))



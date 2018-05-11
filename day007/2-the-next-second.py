'''
title: 计算下一秒 练习
time：2018.04.03 18:30
author: 杨龙（Alex）
'''

# 按照以前的方式
# while True:
#     timeStr = input('请输入一个时间：')
#     timeList = timeStr.split(':')
#     hour = int(timeList[0])
#     minute = int(timeList[1])
#     second = int(timeList[2])
#
#     second += 1
#     if second == 60:
#         second = 0
#         minute += 1
#         if minute == 60:
#             minute = 0
#             hour += 1
#             if hour == 24:
#                 hour = 0
#
#     print('%02d:%02d:%02d' % (hour, minute, second))

def theNextTime(timeStr):
    timeList = timeStr.split(':')
    hour = int(timeList[0])
    minute = int(timeList[1])
    second = int(timeList[2])

    second += 1
    if second == 60:
        second = 0
        minute += 1
        if minute == 60:
            minute = 0
            hour += 1
            if hour == 24:
                hour = 0

    return '%02d:%02d:%02d' % (hour, minute, second)

timeStr = input('请输入一个时间：')
print(theNextTime(timeStr))


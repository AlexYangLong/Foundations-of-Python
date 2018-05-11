'''
title: 异常处理
time: 2018.04.13 18:48
author: 杨龙（Alex）
'''

'''
1、try...except...
格式：
    try:
        可能会发生异常的代码块
    except 异常类 as e:
        异常处理块
    except ...
执行：进入try语句块，如果发生错误，依次匹配except中的异常类，匹配成功进入该异常处理块，匹配不成功会报原始错误...
'''
# try:
#     print(x)
# except NameError as e:
#     print(NameError)
#     print(e)
#     print(111)
# except ValueError as e:
#     print(e)
#     print(222)
# except (TypeError, RuntimeError, NameError) as e:
#     print(e)
#     print(333)


'''
2、try...except...[else...]
格式：
    try:
        可能会发生异常的代码块
    except 异常类 as e:
        异常处理块
    except ...
    
    [else:
        else语句块]
执行：进入try语句块，如果发生错误，依次匹配except中的异常类，匹配成功进入该异常处理块，如果不报错，会执行else中的语句...
'''
# try:
#     a = 123
# except TypeError as e:
#     print(e)
# else:
#     print('没有错误信息')


'''
3、try...except...[else...][finally...]
finally:
try字句不管有没有发生异常,finall字句必然执行
格式:
    try:
        代码块
    except 错误码 as e:
        错误信息
    ...
    else:
        没有错误信息
    finally:
        无论有没有错误信息,必然会走这里
执行：进入try语句块，如果发生错误，依次匹配except中的异常类，匹配成功进入该异常处理块，如果不报错，会执行else中的语句，而finally不管有没有报错都会执行...
'''
# def div(x , y):
#     try:
#         res = x / y
#     except ZeroDivisionError as e:
#         print('除数不能为0')
#     else:
#         print(res)
#     finally:
#         print('Anyway，I also run')
# div(10, 0)


# python中使用raise来抛出一个指定的异常
# raise NameError('不存在该变量')



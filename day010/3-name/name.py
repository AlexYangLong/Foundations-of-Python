'''
title: 引入自定义模块
time: 2018.04.09 18:54
author: 杨龙（Alex）
'''
'''
在python中,每一个脚本执行都会有一个__name__属性
1.如果当前脚本独立运行,则其name属性的值为__main__
2.如果当前脚本引入模块,则模块中的names属性值是当前模块名,而执行脚本的name属性值是__main__
'''

if __name__ == '__main__':
    print('当前脚本独立运行')

else:
    print('被当做模块引入其他文件')











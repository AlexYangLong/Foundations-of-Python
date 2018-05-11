'''
title: 包 练习
time: 2018.04.09 19:10
author: 杨龙（Alex）
'''

'''
1.包:在python中其实就是一个目录.
2.再引入的时候包.模块[.函数]
3.当引入的模块出现同名的时候,我们可以起一个别名来解决同名的问题
包的作用:一般在项目中会出现功能类似导致模块名相同时.并且在引用的过程中就会出现冲突的问题.这时我们可以很好通过包来解决这个问题
'''
# 方式一:  包名称.模块名
import admin.helper
import home.helper
print(admin.helper.edit())
print(home.helper.edit())

# 方式二: from 包名.模块名 import function as new_name
# 当引入模块下边的方法出现同名时,我们可以使用使用as关键字起一个别来来解决
from admin.helper import edit as a_edit
from home.helper import edit as h_edit
print(a_edit())
print(h_edit())

# 方式三: from 包名 import 模块名 as new_name
# 无论是模块还是方法,只要出现同名我们都可以起一个别名来解决冲突的问题
from admin import helper as a_helper
from home import helper as h_helper
print(a_helper.edit())
print(h_helper.edit())

'''
title: 读写文件练习2 -- 写文件
time: 2018.04.08 16:50
author: 杨龙（Alex）
'''

path = r'./io/text2.txt'

# 写文件
fw = open(path, 'w', encoding='utf-8')
fw.write('dadadadada\n')

# 追加内容
fa = open(path, 'a', encoding='utf-8')
fa.write('aaaaaaaa啊啊啊啊aaa')

fw.close()




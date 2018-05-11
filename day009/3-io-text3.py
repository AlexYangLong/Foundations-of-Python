'''
title: 读写文件练习3
time: 2018.04.08 16:50
author: 杨龙（Alex）
'''

path1 = r'./io/text.txt'
path2 = r'./io/text2.txt'

# 使用 try
# try:
#     fr = open(path1, 'r', encoding='utf-8')
#     print(fr.read())
# finally:
#     if fr:
#         fr.close()

# 使用 with
with open(path1, 'r', encoding='utf-8') as fr:
    print(fr.read())

with open(path2, 'a') as fa:
    fa.write('qwerty阿斯蒂芬')






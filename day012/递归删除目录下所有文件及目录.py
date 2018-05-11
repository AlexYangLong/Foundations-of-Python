'''
title: 使用递归来删除目录下所有文件
time: 2018.04.08 18:50
author: 杨龙（Alex）
'''
import os
def deleteAllFileAndDir(path):
    FilesList = os.listdir(path)

    for filename in FilesList:
        filePath = os.path.join(path, filename)
        if os.path.isdir(filePath):

            deleteAllFileAndDir(filePath)
            print('目录：' + filePath + '被删除')
            os.rmdir(filePath)
        else:
            print('文件：' + filePath + '被删除')
            os.remove(filePath)


deleteAllFileAndDir('./text')

# os.rmdir('./text/222')











'''
title: 使用列表模拟栈来遍历目录下所有文件
time: 2018.04.08 16:30
author: 杨龙（Alex）
'''
import os

def getAllFileAndDirByStack(path):
    list1 = []
    list1.append(path)

    while len(list1) != 0:
        dirPath = list1.pop()
        FilesList = os.listdir(dirPath)
        for filename in FilesList:
            filePath = os.path.join(dirPath, filename)
            if os.path.isdir(filePath):
                print('目录：' + filename)
                list1.append(filePath)
            else:
                print('文件：' + filename)

getAllFileAndDirByStack('../0408')

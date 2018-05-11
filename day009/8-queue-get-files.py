'''
title: 使用队列来遍历目录下所有文件
time: 2018.04.08 16:35
author: 杨龙（Alex）
'''
import os
import collections

def getAllFileAndDirByQueue(path):
    queue = collections.deque()
    queue.append(path)

    while len(queue) != 0:
        dirPath = queue.popleft()
        FilesList = os.listdir(dirPath)
        for filename in FilesList:
            filePath = os.path.join(dirPath, filename)
            if os.path.isdir(filePath):
                print('目录：' + filename)
                queue.append(filePath)
            else:
                print('文件：' + filename)

getAllFileAndDirByQueue('../0408')


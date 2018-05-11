'''
title: CSV文件操作
time: 2018.04.13 18:40
author: 杨龙（Alex）
'''

import csv
def readCSVFile(path):
    list1 = []
    with open(path, 'r', encoding='utf-8') as fr:
        res = csv.reader(fr)
        for rowData in res:
            list1.append(rowData)

    return list1

path = r'write.csv'
print(readCSVFile(path))


def writeCSVFile(path, dataList):
    with open(path, 'w', newline='') as fw:
        writer = csv.writer(fw)
        for rowData in dataList:
            writer.writerow(rowData)

datalist = [[1, 2, 4, 5], [3, 4, 5, 6], [6, 7, 8, 9], [10, 2, 3, 4]]

writeCSVFile(path, datalist)






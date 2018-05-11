import csv

class CSVTools(object):
    #读取csv文件的内容，并返回一个二维list
    def readCSVFile(self, path):
        dataList = []
        with open(path, "r") as fr:
            allInfo = csv.reader(fr)
            for rowData in allInfo:
                dataList.append(rowData)
        return dataList

    #将data数据写入path路径的文件中，注意：dataList是一个二维list
    def writeCSVFile(self, path, dataList):
        with open(path, "w", newline='') as fw:
            writer = csv.writer(fw)
            for rowData in dataList:
                writer.writerow(rowData)

csvtools = CSVTools()
list1 = [[1,2,3],[2,3,4],[3,4,5]]

path = r'write.csv'
csvtools.writeCSVFile(path, list1)
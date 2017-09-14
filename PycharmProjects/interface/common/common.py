#encoding:utf-8
import os
from xlrd import open_workbook
import readConfig
proDir =  '/Users/xiaoxiao/PycharmProjects/interface/'
#从excel中读取测试用例
def get_xls(sheet_name):
    #将除了case_name那行的每一行的数据存在一个数组中
    clo =[]
    xlsPath = os.path.join(proDir,'testFile','测试用例.xlsx')
    file = open_workbook(xlsPath)
    sheet = file.sheet_by_name(sheet_name)
    rows = sheet.nrows
    '''for i in range(1,rows):
        if sheet.row_values(i)[0] != u'case_name':
            clo.append(sheet.row_values(i))
            #.append()函数用于在列表末尾添加新的对象
    print clo
    print clo[0][3]'''
    for i in range(rows):
        row = sheet.row_values(i)
    case_name = row[0]
    method = row[1]
    url = row[2]
    data = row[3]
    return url,method,data
print get_xls('sheet1')
print type(get_xls('sheet1'))


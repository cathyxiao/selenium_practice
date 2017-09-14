#encoding:utf-8
import xlrd
import os,logging,requests
import json
Dir = os.path.realpath(__file__)
PATH = os.path.join(os.path.split(Dir)[0],'testFile','测试用例.xlsx')
logging.info("打开%s表成功"%PATH)
file = xlrd.open_workbook(PATH)
#sheet = file.sheet_by_name('sheet1')
sheet = file.sheets()[0]
nrows = sheet.nrows
#读取某行某列的数据
#print sheet.row_values(1)
#print sheet.col_values(1)
#循环
col = len(sheet.row_values(1))
for i in range(nrows):
    row = sheet.row_values(i)
case_name = row[0]
method = row[1]
url = row[2]
data = row[3]
def interfaceTest(url,method,data):
    if method == 'get':
        r = requests.get(url=url,data=dict(data))
    elif method =='post':
        r = requests.post(url=url,data=dict(data))
    print r.status_code
    print r.cookies
if __name__ == '__main__':
    interfaceTest(url,method,data)
#读取单元格
#print sheet.cell(1,0).value
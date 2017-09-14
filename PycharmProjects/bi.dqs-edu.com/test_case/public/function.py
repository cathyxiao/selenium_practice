#encoding:utf-8
import os,logging,time
import json
#定义截屏函数
def screen_shot(driver,file_name):
    file_path = '/Users/xiaoxiao/PycharmProjects/bi.dqs-edu.com/report/image/' + file_name
    driver.get_screenshot_as_file(file_path)
#
def getAllUrl(driver):
    link_list = driver.find_elements_by_tag_name('a')
    #link_list = driver.get_attribute('href')
    print len(link_list)
    return link_list
#
def assertTitle(driver,title):
    try:
        assert driver.title == title
        print title + u"链接正确"
    except:
        print title + '' + u"链接不对"
#
def assertTextPresent(driver,text,file_name):
    try:
        assert text in driver.page_source
    except:
        print '该页面没有加载出' + text
        screen_shot(driver, file_name)
#默认登录
def login(driver):
    driver.find_element_by_id('uname').clear()
    driver.find_element_by_id('uname').send_keys('amily')
    driver.find_element_by_id('upwd').clear()
    driver.find_element_by_id('upwd').send_keys('amily')
    driver.find_element_by_tag_name('button').click()
    driver.implicitly_wait(3)
    driver.maximize_window()
#定义打开excel的函数
def open_execl(PATH):
    try:
        file = xlrd.open_workbook(PATH)
        return file
    except:
        print "打开用例失败"
#参数:file：Excel文件路径 colnameindex：表头列名所在行 ，by_index：表的索引
def excel(file,colnameindex=0,by_index=0):
    file = open_execl(file)
    sheet = file.sheets[by_index]
    nrows = sheet.nrows #统计有多少行
    col = sheet.row_values(colnameindex) #获取表头的那一行数据
    list = []
    for rownum in range(1, nrows):
        row = sheet.row_values(rownum)  #每一行的数据
        if row:
            app = {}
            for i in range(len(col)):
                app[col[i]] = row[i]
                list.append(app)
    return list


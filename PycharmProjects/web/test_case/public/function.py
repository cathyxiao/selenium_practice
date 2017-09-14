#encoding:utf-8
from selenium import webdriver
import os
#定义截屏函数
def screen_shot(driver,file_name):
    file_path = '/Users/xiaoxiao/PycharmProjects/web/report/image/' + file_name
    driver.get_screenshot_as_file(file_path)
def getAllUrl(driver):
    link_list = driver.find_elements_by_tag_name('a')
    #link_list = driver.get_attribute('href')
    print len(link_list)
    return link_list
def assertTitle(driver,title):
    try:
        assert driver.title == title
        print title + u"链接正确"
    except:
        print title + '' + u"链接不对"
def assertTextPresent(driver,text,file_name):
    try:
        assert text in driver.page_source
    except:
        print '该页面没有加载出' + text
        screen_shot(driver, file_name)

#if __name__ == '__main__':

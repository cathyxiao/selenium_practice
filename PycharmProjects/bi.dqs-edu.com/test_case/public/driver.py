#encoding:utf-8
from selenium import webdriver
#定义浏览器驱动
def browser():
    driver = webdriver.Firefox()
    #driver = webdriver.Chrome()
    #driver.maximize_window()
    driver.get('http://bi.dqs-edu.com/')
    return driver
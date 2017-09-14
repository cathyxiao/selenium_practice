#encoding:utf-8
import selenium
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get('http://ms.dqs-edu.com/')
driver.find_element_by_id('uname').clear()
driver.find_element_by_id('uname').send_keys('admin')
driver.find_element_by_id('upwd').clear()
driver.find_element_by_id('upwd').send_keys('ossadmin')
driver.find_element_by_tag_name('button').click()
driver.implicitly_wait(3)
driver.maximize_window()
driver.find_element_by_id('shop-name').send_keys(u'测试')
driver.find_element_by_id('search-btn').click()
try:
    assert 'hahaahhaahhahh' in driver.page_source
except:
    print '没有搜索出结果'

#encoding:utf-8
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get('http://bi.dqs-edu.com/')
driver.find_element_by_id('uname').clear()
driver.find_element_by_id('uname').send_keys('amily')
driver.find_element_by_id('upwd').clear()
driver.find_element_by_id('upwd').send_keys('amily')
driver.find_element_by_tag_name('button').click()
driver.implicitly_wait(3)
driver.maximize_window()
driver.find_element_by_xpath("//thread[@id='bar_head']/tr/th")
'''driver.find_element_by_xpath("//a[@id='account-nav']/span").click()
driver.find_element_by_link_text(u"账号列表").click()
driver.find_element_by_link_text(u"添加预警邮箱").click()
driver.back()'''
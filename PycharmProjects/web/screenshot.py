#encoding:utf-8
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get('http://crm.amily.org')
driver.find_element_by_id('uname').clear()
driver.find_element_by_id('uname').send_keys('123')
time.sleep(3)
driver.get_screenshot_as_file('/Users/xiaoxiao/PycharmProjects/web/data/image.jpg')
driver.quit()
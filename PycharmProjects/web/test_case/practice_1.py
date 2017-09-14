#encoding:utf-8
import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Firefox()
driver.get('http://www.webdriver.org/nav1/')
driver.maximize_window()
a = driver.find_element_by_link_text(u'定位技术')
ActionChains(driver).move_to_element(a).perform()
js = 'document.querySelectorAll("hidefocus")'.style.hidefocus='false'
driver.find_element_by_link_text()
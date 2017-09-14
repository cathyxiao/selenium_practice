#encoding:utf-8
from selenium import webdriver
import time
'''from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys'''
driver = webdriver.Firefox()
driver.get('https://mail.qq.com/')
driver.implicitly_wait(3)
driver.maximize_window()
driver.switch_to.frame('login_frame')
driver.find_element_by_xpath("//span[@id='img_out_1182317567']").click()
driver.implicitly_wait(3)
driver.find_element_by_link_text(u'写信').click()
#element = driver.find_element_by_xpath("//input[@name='UploadFile']")
driver.switch_to.frame('mainFrame')
element = driver.find_element_by_xpath("//a[@class='editor_btn_text qmEditorPhoto ']/span[1]/input[1]")#空格的问题 定位的时候一些元素后面会含有空格
element.send_keys('/Users/xiaoxiao/Desktop/a/aa.jpg')
'''driver.switch_to.frame('x-URS-iframe')
driver.find_element_by_xpath("//input [@class='j-inputtext dlemail']").clear()
driver.find_element_by_xpath("//input [@class='j-inputtext dlemail']").send_keys('wangxiaoxiao2009')
driver.find_element_by_xpath("//input [@class='j-inputtext dlpwd']").send_keys('15153510854haha')
driver.find_element_by_link_text(u'登  录').click()
driver.implicitly_wait(3)
driver.find_element_by_xpath("//b[@class='nui-ico fn-bg ga0']").click()
element = driver.find_element_by_xpath("//input[@class='O0']")
element.send_keys('/Users/xiaoxiao/Desktop/036bc01faf4eaafab11bc5cbbd76a409.jpg')'''
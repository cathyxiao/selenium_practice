#encoding:utf-8
import time,sys
from selenium import webdriver
sys.path.append('./page_obj')
class Login():
    '''def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.driver.get('http://crm.amily.org')
        time.sleep(3)'''
    def user_login(self,driver,username,password):
        driver.find_element_by_id('uname').clear()
        driver.find_element_by_id('uname').send_keys(username)
        driver.find_element_by_id('upwd').clear()
        driver.find_element_by_id('upwd').send_keys(password)
        driver.find_element_by_class_name('btn-submit').click()
        time.sleep(3)
    def user_login_(self,driver):
        driver.find_element_by_id('uname').clear()
        driver.find_element_by_id('uname').send_keys('15910300621')
        driver.find_element_by_id('upwd').clear()
        driver.find_element_by_id('upwd').send_keys('password')
        driver.find_element_by_class_name('btn-submit').click()
        time.sleep(3)
    def user_logout(self,driver):
        driver.find_element_by_class_name('login-out').click()
#encoding:utf-8
from selenium import webdriver
import time
from public_login_crm import Login
class TestLogin():
    def __init__(self):
        self.driver = webdriver.Firefox()
        time.sleep(3)
        self.driver.maximize_window()
        self.driver.get('http://crm.amily.org')
        time.sleep(3)
    def test_user1_login(self):
        username = '15910300621'
        password = 'password'
        #调用Login类中的user_login（）函数实现登录
        Login().user_login(self.driver,username,password)
        Login().user_logout(self.driver)
        self.driver.get_screenshot_as_file('/Users/xiaoxiao/PycharmProjects/web/data')
        time.sleep(6)
    def test_user2_login(self):
        username = '1209262921@qq.com'
        password = 'password'
        Login().user_login(self.driver,username,password)
        Login().user_logout(self.driver)
TestLogin().test_user1_login()
TestLogin().test_user2_login()


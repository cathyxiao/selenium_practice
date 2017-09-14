#encoding:utf-8
from selenium import webdriver
import time
import unittest
from public_login_crm import Login
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
class MyTestLogin(unittest.TestCase):
    def setUp(self):
        print ('test start')
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.driver.get('http://crm.amily.org')
        time.sleep(3)
    def test_user_telephone_login(self):
            '''测试手机号登录是否成功'''
            username = '15910300621'
            password = 'password'
            # 调用Login类中的user_login（）函数实现登录
            Login().user_login(self.driver, username, password)
            title = self.driver.title
            self.assertEqual(title,u'Amily 商品管理页')
            self.driver.get_screenshot_as_file('/Users/xiaoxiao/PycharmProjects/web/report/product.jpg')
    def test_user_email_login(self):
            '''测试邮箱登录是否成功'''
            username = '1209262921@qq.com'
            password = 'password'
            # 调用Login类中的user_login（）函数实现登录
            Login().user_login(self.driver, username, password)
            title = self.driver.title
            self.assertEqual(title,u'Amily 商品管理页')
    def test_nousername_l_login(self):
            '''用户名为空'''
            username = ''
            password = 'password'
            # 调用Login类中的user_login（）函数实现登录
            Login().user_login(self.driver, username, password)
            title = self.driver.title
            self.assertEqual(title,u'Amily 商品管理页')
    def tearDown(self):
        print ('test end')
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()
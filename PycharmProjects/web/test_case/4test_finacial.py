#encoding:utf-8
from selenium import webdriver
import unittest,time
from public_login_crm import Login
import sys
sys.path.append('/Users/xiaoxiao/PycharmProjects/web/test_case/public')
import function
import myunit
from driver import browser
sys.path.append('/Users/xiaoxiao/PycharmProjects/web/test_case/page_obj')
from basePage import Page
from finacialPage import Finacial
class MyFinacial(myunit.MyTest):
    def test_finacial_page(self):
        try:
            Login().user_login_(self.driver)
        except:
            print 'Login failed'
        Finacial(self.driver).finacial_page()
        self.driver.implicitly_wait(3)
        function.screen_shot(self.driver,'finacial页面')
        self.assertEqual(self.driver.title,u'Amily 结算记录')
if __name__ == '__main__':
    unittest.main()






#encoding:utf-8
import unittest,time
from public_login_crm import Login
import sys
sys.path.append('/Users/xiaoxiao/PycharmProjects/web/test_case/public')
import function
import myunit
sys.path.append('/Users/xiaoxiao/PycharmProjects/web/test_case/page_obj')
from basePage import Page
from finacialPage import Finacial
from orderPage import Order
class MyLink(myunit.MyTest):
    def test_order_link(self):
        try:
            Login().user_login_(self.driver)
        except:
            print 'Login failed'
        Order(self.driver).order_page()
        self.driver.implicitly_wait(3)
        for i in function.getAllUrl(self.driver):
            print i
        '''function.assertTitle(self.driver,u'Amily-')
        function.assertTextPresent(self.driver,'aaaaaa','截图')
    def test_finacial_link(self):
        try:
            Login().user_login_(self.driver)
        except:
            print 'Login failed'
        Finacial(self.driver).finacial_page()
        self.driver.implicitly_wait(3)
        function.assertTitle(self.driver, u'Amily 结算记录')
        function.assertTextPresent(self.driver, 'aaaaaa', '截图')'''
if __name__ == '__main__':
    unittest.main()
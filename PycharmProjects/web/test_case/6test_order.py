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
from orderPage import Order
class MyOrder(myunit.MyTest):
    def test_add_order(self):
        #调用driver模块中的browser（）函数启动浏览器
        #driver = browser()
        #调用public_login_crm import中的Login()函数实现登录
        try:
            Login().user_login_(self.driver)
            #注意此时的self.driver  来自myunit.Test中   self的作用
            function.screen_shot(self.driver,'test')
        except:
            print 'login failed'
        time.sleep(3)
        Order(self.driver).order_page()
        '''self.driver.implicitly_wait(10)
        function.screen_shot(self.driver,'order_page')
        self.driver.find_element_by_id('addNewOrder').click()
        self.driver.find_element_by_class_name('order-btns-save').click()
        self.driver.maximize_window()'''
        Order(self.driver).order_add()
        Order(self.driver).order_locktime().click()
    '''def test_data_switch(self):
        try:
            Login().user_login_(self.driver)
            #注意此时的self.driver  来自myunit.Test中   self的作用
            function.screen_shot(self.driver,'test')
        except:
            print 'login failed'
        time.sleep(3)
        Order(self.driver).order_page()
        self.driver.find_element_by_class_name('date-prev ai-date-prev')
        self.driver.find_element_by_class_name('date-next ai-date-next')'''

if __name__ == '__main__':
    unittest.main()

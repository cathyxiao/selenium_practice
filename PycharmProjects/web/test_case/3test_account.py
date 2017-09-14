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
from accountPage import Account
class MyOrder(myunit.MyTest):
    '''def test_account_page(self):
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
        Account(self.driver).account_page()
        self.driver.implicitly_wait(10)
        #self.driver.find_element_by_id('html5_1bbb0i7erbb31ivvmtoc8rr7l3').send_keys('FC3DEADEB53410978FA799AAFCE3035F.jpg')
        #self.driver.find_element_by_xpath('//button').send_keys('FC3DEADEB53410978FA799AAFCE3035F.jpg')
        #/Users/xiaoxiao/Desktop/FC3DEADEB53410978FA799AAFCE3035F.jpg
    def test_pay_info(self):
        try:
            Login().user_login_(self.driver)
            #注意此时的self.driver  来自myunit.Test中   self的作用
            function.screen_shot(self.driver,'test')
        except:
            print 'login failed'
        time.sleep(3)
        Account(self.driver).account_page()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('//div[2]/div/ul/li[3]/a').click()
        self.driver.implicitly_wait(10)
        function.screen_shot(self.driver, 'pay_info')'''
    def test_scroll(self):
        try:
            Login().user_login_(self.driver)
            #注意此时的self.driver  来自myunit.Test中   self的作用
            function.screen_shot(self.driver,'test')
        except:
            print 'login failed'
        time.sleep(3)
        Account(self.driver).account_page()
        self.driver.implicitly_wait(10)
        #通过JavaScript设置浏览器窗口的滚动条位置
        #self.driver.set_window_size(600,600)
        js = 'window.scrollTo(800,1009);'
        self.driver.execute_script(js)
        time.sleep(3)
if __name__ == '__main__':
    unittest.main()
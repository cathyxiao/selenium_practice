#encoding:utf-8
import sys,time,unittest
sys.path.append('/Users/xiaoxiao/PycharmProjects/bi.dqs-edu.com/test_case/public')
import function
import myunit
sys.path.append('/Users/xiaoxiao/PycharmProjects/bi.dqs-edu.com/test_case/page_object')
from loginPage import Login
from shopPage import Shop
class MyTestShop(myunit.MyTest):
    def test_shop(self):
     try:
        Login().login_page()
        time.sleep(3)
        function.login(self.driver)
     except:
        function.screen_shot(self.driver, 'test')
        print 'login failed'
     time.sleep(3)
     Shop(self.driver).shop_page()
     select = self.driver.find_element_by_id('select')
     option_list = select.find_elements_by_tag_name('option')  # 注意这个地方是elements 否则会报错
     count = 0
     for i in option_list:
         count = count + 1
     print '商户列表品牌的个数是：', count
if __name__ == '__main__':
    unittest.main()
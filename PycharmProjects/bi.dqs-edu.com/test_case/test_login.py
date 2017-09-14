#encoding:utf-8
import sys,time,unittest
sys.path.append('/Users/xiaoxiao/PycharmProjects/bi.dqs-edu.com/test_case/public')
import function
import myunit
sys.path.append('/Users/xiaoxiao/PycharmProjects/bi.dqs-edu.com/test_case/page_obj')
from loginPage import Login
class MyTestLogin(myunit.MyTest):
    def test_login(self):
        Login().login_page(self.driver)
        function.login(self.driver)
        listdata = function.excel(file="",by_index=0)
        if (len(listdata) <= 0):
            assert 0, u"Excel数据异常"
        for i in range(0, len(listdata)):
            # 点击登录按钮
            self.driver.find_element_by_id('uname').clear()
            time.sleep(3)
            self.driver.find_element_by_id('uname').send_keys(listdata[i]['username'])
            time.sleep(3)
            self.driver.find_element_by_id('upwd').clear()
            time.sleep(3)
            self.driver.find_element_by_id('upwd').send_keys(listdata[i]['password'])
            time.sleep(3)
            self.driver.find_element_by_tag_name('button').click()
            time.sleep(3)
if __name__ == '__main__':
    unittest.main()
import sys,time,unittest
sys.path.append('./public')
from myunit import MyTest
sys.path.append('./page_obj')
from loginPage import Login
class LoginTest(MyTest):
    def test_login(self):
        Login(self.driver).login_page()
        Login(self.driver).login_username('15910300621')
        Login(self.driver).login_username('password')
        Login(self.driver).login_submit()
if __name__ == '__main__':
    unittest.main()

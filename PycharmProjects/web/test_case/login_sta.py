#encoding:utf-8
import unittest
import sys
sys.path.append('./page_obj')
sys.path.append('./public')
#对于模块和自己写的程序不在同一个目录下，可以把模块的路径通过sys.path.append(路径)添加到程序中。
#sys.path.append(’引用模块的地址')
from public import myunit
from page_obj.loginPage import Login
class MyTestLogin(myunit.MyTest):
    def test_user_telephone(self):
        username = '15910300621'
        password = 'password'
        Login(self.driver).login(self.driver,username,password)
if __name__ == '__main__':
    unittest.main()
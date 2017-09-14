import sys,time
sys.path.append('./public')
from function import login
from myunit import MyTest
class Login(MyTest):
    def test_login1(self,driver,username,password):
        '用户名正确，密码正确'
        try:
            login(self.driver,username='',password='')
        except:
            print 'longin failed'
    def test_login2(self,driver,username,password):
        '用户名正确，密码不正确'
        try:
            login(self.driver,username='',password='')
        except:
            print 'longin failed'
    def test_login3(self,driver,username,password):
        '用户名正确，密码为空'
        try:
            login(self.driver,username='',password='')
        except:
            print 'longin failed'
    def test_login4(self,driver,username,password):
        '用户名正确，密码为空格'
        try:
            login(self.driver,username='',password='')
        except:
            print 'longin failed'
    def test_login5(self,driver,username,password):
        '用户名不正确，密码正确  不正确包含不合法'
        try:
            login(self.driver,username='',password='')
        except:
            print 'longin failed'
    def test_login6(self,driver,username,password):
        '用户名不正确，密码不正确 不正确包含不合法'
        try:
            login(self.driver,username='',password='')
        except:
            print 'longin failed'
    def test_login7(self,driver,username,password):
        ''
        try:
            login(self.driver,username='',password='')
        except:
            print 'longin failed'
    def test_login8(self,driver,username,password):
        ''
        try:
            login(self.driver,username='',password='')
        except:
            print 'longin failed'
    def test_login9(self,driver,username,password):
        '用户名不正确，密码为空'
        try:
            login(self.driver,username='',password='')
        except:
            print 'longin failed'
    def test_login10(self,driver,username,password):
        '用户名不正确，密码为空格'
        try:
            login(self.driver,username='',password='')
        except:
            print 'longin failed'
    def test_login11(self,driver,username,password):
        '用户名正确，密码不正确'
        try:
            login(self.driver,username='',password='')
        except:
            print 'longin failed'
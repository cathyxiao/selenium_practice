import sys
sys.path.append('./public')
from function import login_defaut_administrator,login_defaut_ordinary
from myunit import MyTest
class Right(MyTest):
    def test_administrator(self):
        #管理员登录
        try:
            login_defaut_administrator(self.driver)
        except:
            print 'longin failed'
        #跳转到某个页面

        #验证是否存在某些权限  assertTextPresent 检查在当前给用户显示的页面上是否有出现指定的文本）
        self.assertTextPreset()

    def test_ordinary(self):
        #普通用户登录
        try:
            login_defaut_administrator(self.driver)
        except:
            print 'longin failed'
        #跳转到某个页面

        #验证某些权限


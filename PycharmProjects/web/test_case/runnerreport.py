#encoding:utf-8
import unittest
import time
from HTMLTestRunner import HTMLTestRunner
from test_login import MyTestLogin
import test_login
test_dir = './'#当前目录
#TestLoader类中提供了discover（）自动识别测试用例，可找到制定模块下的所有测试模块，只有匹配到文件名才能被加载,以test开头的
discover = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')
if __name__ == '__main__':
    #unittest.main()
    #定义测试报告的地址
    now = time.strftime("%Y_%_m%_d %H:%M:%S")#指定格式获取当前时间
    file = '/Users/xiaoxiao/PycharmProjects/web/report' + '/'+ now +'report.html'
    f = open(file,'wb')
    runnerreport = HTMLTestRunner(stream=f,title=u'登录测试报告',description=u'用例执行情况')
    runner = unittest.TextTestRunner()
    #在unittest中提供TextTestRunner类提供的runner（）方法执行
    #runner.run(discover)
    runnerreport.run(discover)
    #suite = unittest.TestSuite()
    #suite.addTest(MyTestLogin('test_user_telephone_login'))
    #suite.addTest(MyTestLogin('test_user_email_login'))
    #runner.run(suite)
    f.close()
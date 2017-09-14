#encoding:utf-8
import unittest
from HTMLTestRunner import HTMLTestRunner
test_dir = './'#当前目录
#TestLoader类中提供了discover（）自动识别测试用例，可找到制定模块下的所有测试模块，只有匹配到文件名才能被加载,以test开头的
discover = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py',top_level_dir=None)
f = open('./report.html','wb')
report = HTMLTestRunner(stream=f,title=u'登录测试报告',description=u'执行用例情况')
runner = unittest.TextTestRunner()
runner.run(discover)
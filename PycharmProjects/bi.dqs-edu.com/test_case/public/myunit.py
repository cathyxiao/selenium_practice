#encoding:utf-8
import unittest
from driver import browser
class MyTest(unittest.TestCase):
    def setUp(self):
        print 'test start'
        self.driver = browser()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
    '''def tearDown(self):
        self.driver.quit()
        print 'test end'''
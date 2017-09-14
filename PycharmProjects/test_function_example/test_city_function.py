#encoding:utf-8
'''该函数验证city_function中get_cities这个函数'''
import os
import unittest
from city_functions2 import get_cities
class cityTestcase(unittest.TestCase):
    def test_city_function(self):
        city = get_cities('weifang','china')
        #city为我的测试数据
        self.assertEqual(city,'Weifang,China-')
if __name__ == '__main__':
    unittest.main()
'''测试函数是否有可空的形参 要是该可空的参数前面还需要有符号连接的话 函数中还得加一个if连接的判断 如果不加的话 该字符为空时 该字符的前面
也会出现所设定的连接的符号eg：上面的population前面的-'''

'''开发经常容易犯的错误'''
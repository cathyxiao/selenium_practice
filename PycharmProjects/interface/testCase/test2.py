#encoding:utf8
import unittest
import md5
import json
import requests
from common import common
from readConfig import ReadConfig
class A(unittest.TestCase):
    def setUp(self):
        print 'test start'
    def tearDown(self):
        print 'test end'
    url = common.get_xls('sheet1')[0]
    method = common.get_xls('sheet1')[1]
    data = common.get_xls('sheet1')[2]
    def test_login(url,method,data):
        if method == 'get':
            r = requests.get(url=url, data=dict(data))
        elif method == 'post':
            r = requests.post(url=url, data=dict(data))
        print r.status_code
if __name__ == '__main__':
    unittest.main()
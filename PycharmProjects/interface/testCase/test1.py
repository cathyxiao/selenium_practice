#coding: UTF-8
import requests
import json
import unittest
class Interface(unittest.TestCase):
    def setUp(self):
        self.url_base = 'http://101.200.173.33:8123'
    def tearDown(self):
        print 'test end'
    def test_searchBussiniess_code(self):
        url = '/crud/list/brand.htm'
        url = self.url_base + url
        print url
        a = '%a%'
        paramer = {'name':a}
        r = requests.get(url=url,params=paramer)
        assert r.status_code == 200
    def test_shopReport(self):
        url = '/shop/shopReport.htm'
        url = self.url_base + url
        print url
        #paramer = {'shopId': ,}

    def test_shopRadio(self):
        url = '/shop/shopRatio.htm'
        url = self.url_base + url


if __name__ == '__main__':
    print 'start'
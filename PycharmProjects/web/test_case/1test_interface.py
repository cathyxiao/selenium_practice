#encoding:utf-8
import unittest
import requests
import json,os,csv
class InterfaceTest(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://bi.dqs-edu.com/'
    def tearDown(self):
        print 'test end'
    def test_null(self):
        url = '/shop/groupbuyingReport.htm'
        url = self.base_url + url
        print url
        #lines = csv.reader('/Users/xiaoxiao/PycharmProjects/web/data/data.csv')
        #for line in lines:
        data ={'uin':'','cityId':'1','type':'5','version':'2920','tv':'30','indexno':'0'}
        print type(data)
        data_json = json.dumps(data)
        #Encode过程，是把python对象转换成json对象的一个过程，
        # 常用的两个函数是dumps和dump函数。两个函数的唯一区别就是dump把python对象转换成json对象生成一个fp的文件流，
        # 而dumps则是生成了一个字符串
        #将数据转换为json格式
        #json.loads()将json格式转化为python格式
        #print type(data_json)
        r = requests.post(url,data=data_json).content
        print type(r)
        result = json.loads(r)
        print type(result)
        #获取字典里的值的用法：value = dictname[key]
        if (result['ret'] == 0):
            print '成功返回数据'
        else:
            print '返回数据失败'
if __name__ == '__main__':
    unittest.main()
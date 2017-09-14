#encoding:utf-8
import requests
import readConfig
local_readConfig = readConfig.ReadConfig
class ConfigHttp:
    def __init__(self):
        global host
        host = local_readConfig.get_http('baseurl')
        #port = local_readConfig.get_http('port')

    def set_url(self,url):
        self.url = host + url

    def set_header(self,header):
        self.header = self.header

    def set_paramer(self,paramer):
        self.paramer = paramer

    def set_data(self,data):
        self.data = data

    def get(self):
        try:
            result = requests.get(url=self.url,params=self.paramer)
        except:
            print 'time out'

    def post(self):
        try:
            result = requests.post(url=self.url,data=self.data)
        except:
            print 'time out'
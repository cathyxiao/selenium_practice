#encoding:utf-8
import os
import configparser  #是用来读取配置文件的包
import codecs
proDir = os.path.split(os.path.realpath(__file__))[0]#__file__  当前执行脚本的路径 os.path.realpath(__file__)绝对路径
#os.path.split(path)  #把路径分割成dirname和basename，返回一个元组，元组特点是值不可变
configPath = os.path.join(proDir,'config.ini')
class ReadConfig:
    def __init__(self):
        #file = open(configPath)
        #data = file.read()
        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)
    def get_email(self,name):
        value = self.cf.get('EMAIL',name)
        print value
        #return value
    def get_url(self,name):
        value = self.cf.get('HOST',name)
        return value
    def get_http(self,name):
        value = self.cf.get('HTTP',name)
        return

'''if __name__ == '__main__':
    ReadConfig().get_http('baseurl')'''
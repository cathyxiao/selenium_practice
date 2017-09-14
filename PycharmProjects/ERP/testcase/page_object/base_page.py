#encoding:utf-8
#实例化时完成浏览器中打开url操作
import time
from test_case.public.driver import browser
from selenium.webdriver.common.action_chains import ActionChains
class Page(object):
    #页面的基础类，用于所有的页面,初始化Page时先执行init方法
    login_url = 'http://bi.dqs-edu.com/'
    #在初始化方法中驱动driver 基本的url 和 超时时间
    def __init__(self,driver,base_url=login_url):
        self.driver = driver
        self.url = base_url
        self.timeout = 20
        #self.parent = parent
    #self只有在类的方法中才会有，独立的函数或方法是不必带有self的,self指的是类实例对象本身(注意：不是类本身)
    def open(self,url):
        url = self.url + url
        #地址 + 后缀的url
        self.driver.get(url)
    def find_elementq(self,loc):
        return self.driver.find_element(loc)
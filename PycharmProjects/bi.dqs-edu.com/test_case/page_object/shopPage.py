#encoding:utf-8
import time
from selenium.webdriver.common.by import By
from basePage import Page
#创建登录对象 每个元素都拆分开
class Shop(Page):
    a_url = 'm/shop/shop_report'
    #定义页面元素
    #定义方法
    def shop_page(self):
         Page(self.driver).open(self.a_url)
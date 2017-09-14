#encoding:utf-8
import time
from selenium.webdriver.common.by import By
from basePage import Page
#创建登录对象 每个元素都拆分开
class Login(Page):
    a_url = '/'
    #定义页面元素
    #定义方法
    def login_page(self):
         Page(self.driver).open(self.a_url)
    def login_username(self,username):
        Page(self.driver).find_element(self.login_username_loc).clear
        Page(self.driver).find_element(self.login_username_loc).send_keys(username)

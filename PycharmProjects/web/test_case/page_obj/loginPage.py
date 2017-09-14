#encoding:utf-8
import time
from selenium.webdriver.common.by import By
from basePage import Page
#创建登录对象 每个元素都拆分开
class Login(Page):
    a_url = '/'
    #定义页面元素
    login_username_loc = (By.ID,"uname")
    login_password_loc = (By.ID,"upwd")
    login_botton_loc = (By.ID,"btn-submit")
    forget_pwd_loc = (By.ID,"forget-pwd")
    #定义方法
    def login_page(self):
         Page(self.driver).open(self.a_url)
    def login_username(self,username):
        Page(self.driver).find_element(self.login_username_loc).clear
        Page(self.driver).find_element(self.login_username_loc).send_keys(username)
    #
    def login_password(self,password):
        self.find_element(self.login_password_loc).clear
        self.find_element(self.login_password_loc).send_keys(password)
    #
    def login_submit(self):
        self.find_element(self.login_botton_loc).click
    def forget_pwd(self):
        self.find_element(self.forget_pwd_loc).click
    #定义统一登录入口
    def login1(self,username,password):
        self.open()
        self.login_username(username)
        self.login_password(password)
        self.login_submit()
        time.sleep(3)
    def login(self,username,password):
        self.open()
        self.login_username(username)
        self.login_password(password)
        self.login_submit()
        time.sleep(3)
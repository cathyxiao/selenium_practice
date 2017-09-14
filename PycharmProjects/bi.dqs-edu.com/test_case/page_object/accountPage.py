#encoding:utf-8
from selenium.webdriver.common.by import By
from basePage import Page
class Account(Page):
    account_url = 'm/account/account_list'
    def account_page(self):
        Page(self.driver).open(self.account_url)
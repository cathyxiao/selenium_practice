#encoding:utf-8
from selenium.webdriver.common.by import By
from basePage import Page
class Groupbuying(Page):
    groupbuying_url = 'm/groupbuying/groupbuying_report'
    def groupbuying_page(self):
        Page(self.driver).open(self.groupbuying_url)
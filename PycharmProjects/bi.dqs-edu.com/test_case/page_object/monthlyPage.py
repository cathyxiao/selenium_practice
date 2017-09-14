#encoding:utf-8
from selenium.webdriver.common.by import By
from basePage import Page
class Monthly(Page):
    monthly_url = 'm/monthly/monthly_report'
    def monthly_page(self):
        Page(self.driver).open(self.monthly_url)
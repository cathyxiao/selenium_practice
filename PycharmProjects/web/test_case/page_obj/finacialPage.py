#encoding:utf-8
from selenium.webdriver.common.by import By
from basePage import Page
class Finacial(Page):
    finacial_url = '/m/finance'
    def finacial_page(self):
        Page(self.driver).open(self.finacial_url)
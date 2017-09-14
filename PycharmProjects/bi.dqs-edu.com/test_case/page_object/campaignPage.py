#encoding:utf-8
from selenium.webdriver.common.by import By
from basePage import Page
class Campaign(Page):
    campaign_url = 'campaign/campaign_report'
    def campaign_page(self):
        Page(self.driver).open(self.campaign_url)
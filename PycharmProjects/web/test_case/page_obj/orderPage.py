#encoding:utf-8
from selenium.webdriver.common.by import By
from basePage import Page
class Order(Page):
    order_url = '/m/person_day'
    order_add_col = (By.CSS_SELECTOR,'add-new-order')
    #//li[2]/a
    order_locktime_col = (By.ID,'setHoliday')
    order_page_col = (By.CLASS_NAME,'g-nav-inner')
    def order_page(self):
        Page(self.driver).open(self.order_url)
        #self.find_element(self.order_page_col).click
        #ActionChains().click(*self.order_page_col)
    def order_add(self):
        self.find_elementq(self.order_add_col).click()
    def order_locktime(self):
        self.find_elementq(self.order_page_col).click()
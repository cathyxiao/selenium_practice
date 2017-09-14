#encoding:utf-8
from selenium import webdriver
def browser():
    driver = webdriver.Firefox()
    driver.get("http://bi.dqs-edu.com/")
    return driver

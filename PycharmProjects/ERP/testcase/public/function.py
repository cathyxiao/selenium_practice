# encoding:utf-8
from selenium import webdriver
from driver import browser
import os
# 定义截屏函数
def screen_shot(driver,file_name):
    file_path = '/Users/xiaoxiao/PycharmProjects/ERP/report/image/' + file_name
    driver.get_screenshot_as_file(file_path)
def login_defaut_administrator(driver,username='',password=''):
    driver.find_element_by_id('uname').clear()
    driver.find_element_by_id('uname').send_keys(username)
    driver.find_element_by_id('upwd').clear()
    driver.find_element_by_id('upwd').send_keys(password)
    driver.find_element_by_class_name('btn-submit').click()
def login_defaut_ordinary(driver,username='',password=''):
    driver.find_element_by_id('uname').clear()
    driver.find_element_by_id('uname').send_keys(username)
    driver.find_element_by_id('upwd').clear()
    driver.find_element_by_id('upwd').send_keys(password)
    driver.find_element_by_class_name('btn-submit').click()
def login(driver,username,password):
    driver.find_element_by_id('uname').clear()
    driver.find_element_by_id('uname').send_keys(username)
    driver.find_element_by_id('upwd').clear()
    driver.find_element_by_id('upwd').send_keys(password)
    driver.find_element_by_class_name('btn-submit').click()
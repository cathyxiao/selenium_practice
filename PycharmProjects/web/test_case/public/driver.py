#encoding:utf-8
from selenium import webdriver
#from selenium.webdriver import Remote
#定义浏览器驱动
def browser():
    driver = webdriver.Firefox()
    #driver = webdriver.Chrome()
    #driver.maximize_window()
    driver.get('http://crm.amily.org/')
    '''host = '127.0.0.1:4444'#webdriver 默认selenium server 地址
    dc = {'browserName' : 'firefox'}
    #对浏览器配置 浏览器的配置由desired_capabilities决定
    #调用remote的方法配置
    driver = Remote(command_executor='http://' + host + '/wd/hub',desired_capabilities=dc)'''
    return driver
if __name__ == '__main__':
    dr = browser()
    dr.get('http://www.baidu.com')
    dr.quit()
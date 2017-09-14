#encoding:utf-8
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get('http://bi.dqs-edu.com/')
driver.find_element_by_id('uname').clear()
driver.find_element_by_id('uname').send_keys('amily')
driver.find_element_by_id('upwd').clear()
driver.find_element_by_id('upwd').send_keys('amily')
driver.find_element_by_tag_name('button').click()
driver.implicitly_wait(3)
driver.maximize_window()
#获取商户通的品牌
select = driver.find_element_by_id('select')
option_list = select.find_elements_by_tag_name('option')#注意这个地方是elements 否则会报错
count = 0
for i in option_list:
    count=count+1
print '商户列表品牌的个数是：',count
a = Select(driver.find_element_by_id('select'))
a.select_by_index('3')
if driver.find_element_by_xpath("//input[@value='month']").is_selected():
    print 'seleted'
    #注意xpath的定位写法外面双引号 里面单引号
else:
    driver.find_element_by_xpath("//input[@value='month']").send_keys(Keys.SPACE)
#进入团购页面
driver.find_element_by_id('groupbuying-nav').click()
driver.implicitly_wait(3)
#进入团购报表页
driver.find_element_by_link_text('团购报表').click()
driver.implicitly_wait(3)
#点击查询按钮 联系弹出框
#driver.find_element_by_xpath("//button[@class='js-search']").click()
driver.implicitly_wait(3)
#点击获取弹窗的链接
driver.find_element_by_xpath("//span[@class='click']").click()
#定位checkbox
driver.find_element_by_xpath("//input[@value='22331166']").send_keys(Keys.SPACE)
driver.find_element_by_xpath("//span[@class='pull-right']/a").click()
#driver.find_element_by_xpath("//div[@class='form-group']/button").click()
#driver.refresh()
#driver.back()
#driver.back()
#driver.quit()
#进入到代运营账号页
#driver.find_element_by_xpath("//a[@id='account-nav']/i/span").click()
#encoding:utf-8
import time,re,MySQLdb,sys
from selenium import webdriver
reload(sys)
sys.setdefaultencoding('utf-8')
driver = webdriver.Firefox()
driver.set_page_load_timeout(30)
driver.get('http://blog.csdn.net/Eastmount')
driver.implicitly_wait(3)
driver.maximize_window()
def getPage():
    #找到页面的那一行
    texts = driver.find_element_by_id('papelist').text
    #正则表达式寻找数字
    m = re.findall(r'\w*[0-9]+',texts)
    #print u'页数：' + str(m[1])
    return int(m[1])
url ='http://blog.csdn.net/Eastmount'
allpage = getPage()
#创建读入的文件
f = file('data1.txt','w+')
#获取每页的url
i=2
while i <= allpage:
    ur = url + '/article/list/' + str(i)
    #print ur
    try:
        driver.get(ur)
    except:
        print 'time out'
        driver.execute_script('window.stop()')
    article_title = driver.find_elements_by_class_name('article_title')
    #print article_title
    #article_title = driver.find_elements_by_xpath("//a[@class='link_title']/a")
    article_title = driver.find_elements_by_xpath("//div[@class='article_title']")
    list=[]
    for title in article_title:
        a = title.text
        #print type(a)
        f.writelines(a+'\n')
        list.append(a)
    #print list[0]
    i = i + 1
connect = MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456',port=3306,db='test')
cur = connect.cursor()
j = 1
while j<= len(list):
    website = list[j-1]
    #sql = "insert into web values(%s,'2','3','4')"
    #website = list[j-1]
    #website = list[j]
    cur.execute("insert into get_data values(%s)",(list[j-1]))
    connect.commit()
    connect.close()
    j = j + 1

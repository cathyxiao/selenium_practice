#encoding:utf-8
import time,re,MySQLdb
'''from selenium import webdriver
driver = webdriver.Firefox()
driver.get('http://blog.csdn.net/Eastmount')
driver.implicitly_wait(3)
driver.maximize_window()
texts = driver.find_element_by_id('papelist').text
print texts
m = re.findall(r'\w*[0-9]+',texts) #正则表达式寻找数字
print '页数：' + str(m[1])
print m '''
connect = MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456',port=3306,db='test')
cur = connect.cursor()
list = ['1','2','3','4']
sql = "insert into web values('list[0]')"
cur.execute(sql)
connect.close
connect.commit()
sql_select = 'select * from web'
cur.execute(sql_select)
#读取方法一
rs = cur.fetchall()
for i in rs:
    print i
print cur.fetchone()''
'''#读取方法二：
cur = connect.cursor(cursorclass=MySQLdb.cursors.DictCursor)
cur.execute("select * from web")#每一行用键值对表示出来
for line in cur.fetchall():
    print line['website']#字典的取值方式dic['key']'''

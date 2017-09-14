#encoding: UTF-8
import requests
import json
from login_bi import MyLogin
#get
r = 'http://bi.dqs-edu.com/shop/shopReport.htm'
'''param = {'pn':1,'ps':15}
cookies = {'cookies':'JSESSIONID=1x3avrbhwsw5bwm4b3m82sc3m'}
result = requests.get(r,params=param,cookies=cookies)
#print result.text
print result.headers
print result.cookies
print result.status_code'''
'''
requests 会自动帮我们拼接请求地址
post
res = requests.post("http://httpbin.org/post",data={"key":"value", ...})
发送delete请求
res = requests.delete("http://httpbin.org/delete")
res = requests.head("http://httpbin.org/get")
res = requests.options("http://httpbin.org/
'''
"""
haha
"""
data = {'pn':'1','ps':'30','beginDay':'20170208','endDay':'20170208','brandId':'1'}
cookies =MyLogin()
result = requests.post(r,data=data,cookies=cookies)
r = result.status_code
print r

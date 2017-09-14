#encoding:utf-8
import requests
import json
def MyLogin():
    url = 'http://bi.dqs-edu.com/'
    params_login = {'user':'amily','password':'amily'}
    print type(params_login)
    r = requests.get(url = url,data=params_login)
    #return r.headers
    #return r.cookies
    print r.status_code
    #print requests.utils.dict_from_cookiejar(r.cookies)
MyLogin()
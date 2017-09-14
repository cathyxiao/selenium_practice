#encoding:utf-8
import urllib.request
import configparser #configparser

#配置
class ConfigHttp:
    #配置测试接口服务器的ip 端口 域名 请求方式
    def __int__(self,ini_file):
        config = configparser.ConfigParser()
        #从配置文件中获取数据
        config.read(ini_file)
    #封装http get请求方法
    def get_func:
        url = ''
        param = {}
        res = result.get(url,params=param)


    #封装http post请求方法(使用post方式时，数据放在data或者body中，不能放在url中，放在url中将被忽略)
        def post_func:
            url = ''
            data = {}
            res = result.post(url, data=data)



    #封装head请求方法

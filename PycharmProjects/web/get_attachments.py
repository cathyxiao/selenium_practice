#encoding:utf-8
import os
import time
report_dir = '/Users/xiaoxiao/PycharmProjects/web/report'
lists = os.listdir(report_dir)#获取目录的内容 listdir
print lists
new_time = os.path.getmtime(report_dir)
timeArray = time.localtime(new_time)
print time.strftime("%Y_%_m%_d %H:%M:%S",timeArray)
#time.local()转换秒数为本地时间
new_list = lists.sort(key=lambda fn: os.path.getmtime(report_dir+'/'+fn))
#key=lambda fn:key是带一个参数的函数，用来为每个元素提取比较值.默认为None, 即直接比较每个元素lambda提供了一个运行时动态创建函数的方法。
# 我这里创建了fn 函数。
#getmtime()获取文件最后修改的时间
print new_list
print (('最新文件排序为'+ lists[-1]))
file = os.path.join(report_dir,lists[-1])
#list[-1]代表最后一个元素new_report_dir = os.path.dirname(file)
new_report_dir = os.path.basename(file)
print new_report_dir

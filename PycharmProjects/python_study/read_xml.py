#encoding:utf-8
from xml.dom import minidom
file = minidom.parse('wenjianming')#parse()用于打开一个xml文件
root = file.documentElement
#documentElement用来得到xml文件的唯一根元素
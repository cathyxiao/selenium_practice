#encoding:utf-8
file_object = open('file')
lines = file_object.readlines()#以数组的形式存储
for line in lines:
    a = line.split(',')[0]#分割出来的以数组的形式存储
    #split()通过指定分隔符对字符串进行切片,str.split(str="", num=string.count(str)).str -- 分隔符，默认为空格。分割次数
    b = line.split(',')[1]
    print a
    print b
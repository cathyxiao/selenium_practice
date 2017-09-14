#encoding:utf-8
#python在该路径下查找制定文件 关键字with指的是在不需要访问文件后将其关闭，相当于close 但是避免了close没执行时导致文件未关闭的问题,但是页存在问题，立马关闭
'''with open('report.py') as file_object:
    #contents = file_object.read()
    #print contents.rstrip()
    #read（）到达文件末尾时会返回一个空字符串，显示出来就是空行，删除空行，使用rstrip（）
    for line in file_object:
        print(line)
    #逐行读'''
'''with open('report.py') as file_object:
    contents = file_object.readlines()#将每一行存储在contents列表里，注意readline与readlines的区别
    print contents
ps = ''
for line in contents:
    ps += line.rstrip()
print ps '''
with open('report.py') as file_object:
    contents = file_object.read()
a = input('请输入内容')
#用户输入的时候必须要加上引号（单引号双引号都可以）
if a in contents:
    print ('have')
else:
    print ('not')
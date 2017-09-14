#encoding:utf-8
import unittest
import time
from test_login import MyTestLogin
import test_login
from HTMLTestRunner import HTMLTestRunner
import smtplib,os
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#配置邮箱 用户 密码
def send_mail(newreport):
    smtpserver = 'smtp.exmail.qq.com'
    usr ='wangxiaoxiao@hiamily.com'
    password = 'Wxx123'
    sender = 'wangxiaoxiao@hiamily.com'
    receiver = '1182317567@qq.com'
    #创建一个multipart()实例  带附件 # 构造MIMEMultipart对象做为根容器
    msg = MIMEMultipart()
    # 构造MIMEText对象做为邮件显示内容并附加到根容器
    #body = MIMEText('<html><h1>测试报告</h1></html>','html','utf-8')
    #att1_dir = os.path.dirname(file)
    f = open(newreport,'rb')
    att1 = MIMEText(f.read(), 'base64', 'utf-8')
    f.close()
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename=''daily report'' '
    msg.attach(att1)
    #设置一下发送邮件的标题 发送者等信息
    subject = '测试报告'
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    #发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver,25)
    smtp.login(usr,password)
    smtp.sendmail(sender,receiver,msg.as_string())#要注意msg的格式。这个格式就是smtp协议中定义的格式
    print('邮件发送成功')
    smtp.quit()
# 查找最新生成的测试报告
def search_file(report_dir):
    lists = os.listdir(report_dir)
    new_lists = lists.sort(key=lambda fn: os.path.getmtime(report_dir + '/' + fn))
    file_new = os.path.join(report_dir, lists[-1])
    file_name = ' 最新测试报告'
    # os.path.dirname()获取路径名   os.path.basename()获取文件名
    #new_report_dir = os.path.basename(file)
    print file_new
    return file_new
if __name__ == '__main__':
    test_dir = './'  # 当前目录
    report_dir = '/Users/xiaoxiao/PycharmProjects/web/report'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
    now = time.strftime("%Y_%_m%_d %H:%M:%S")  # 指定格式获取当前时间
    filename = '/Users/xiaoxiao/PycharmProjects/web/report' + '/' + now + 'report.html'
    fp = open(filename, 'wb')
    runnerreport = HTMLTestRunner(stream=fp, title=u'登录测试报告', description=u'用例执行情况')
    runnerreport.run(discover)
    fp.close()
    newreport = search_file(report_dir)
    send_mail(newreport)

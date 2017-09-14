#encoding:utf-8
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#发送邮箱服务器
smtpserver = 'smtp.exmail.qq.com'
#发送邮箱用户名/密码
user = 'wangxiaoxiao@hiamily.com'
password = 'Wxx123'
#发送邮箱
sender = 'wangxiaoxiao@hiamily.com'
receiver = '1182317567@qq.com'
#发送邮件主题
subject = '邮件的标题'
#三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
msg = MIMEText('<html><h1>测试报告</h1></html>','html','utf-8')
msg['Subject'] = Header(subject,'utf-8')
#创建一个multipart()实例  带附件 # 构造MIMEMultipart对象做为根容器
'''msg = MIMEMultipart()
# 构造MIMEText对象做为邮件显示内容并附加到根容器
body = MIMEText('<html><h1>测试报告</h1></html>','html','utf-8')
#att1 = MIMEText(open('/Users/xiaoxiao/Desktop/crm数据统计 接口.pages').read(), 'base64', 'utf-8')
att1 = MIMEText(open('/Users/xiaoxiao/Desktop/erp登录/report/html/TestReport201704230234.html').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename=''name'' '
msg.attach(att1)
subject = '测试报告'
msg['Subject'] = Header(subject,'utf-8')'''
msg['From'] = sender
try:
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver,25)
    smtp.login(user,password)
    #需要先登录否则发送不成功
    smtp.sendmail(sender,receiver,msg.as_string())
    smtp.quit()
except smtplib.SMTPException:
    print 'failed'
#发送带附件的邮件，首先要创建MIMEMultipart()实例，然后构造附件，如果有多个附件，可依次构造，最后利用smtplib.smtp发送


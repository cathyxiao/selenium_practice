#encoding:utf-8
import smtplib
from email.header import Header
from email.mime.text import MIMEText
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
msg = MIMEText('<html><h1>测试报告</h1></html>','html','utf-8')
#发送邮件主题
subject = '测试报告'
#三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
msg = MIMEText('<html><h1>测试报告</h1></html>','html','utf-8')
msg['Subject'] = Header(subject,'utf-8')
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
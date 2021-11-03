#coding=utf-8
'''
time:2020/8/21 17:10
'''
import smtplib
from email.mime.text import MIMEText  # MIMEText()定义邮件正文
from email.header import Header  # Header()定义邮件标题

# 发送邮箱服务器
smtpserver = 'smtp.163.com'

# 发送邮箱用户/密码(登录邮箱操作)
user = "zyxzhongzhi@163.com"
psw="LJRHHONJDQZHSRMS"

# 发送邮箱
sender = "zyxzhongzhi@163.com"

# 接收邮箱
# receiver = ['zyxzhongzhi@163.com','kaiho_wang@163.com']
# receiver = ['kaiho_test@163.com','zyxzhongzhi@163.com']
# receiver = 'kaiho_test@163.com'
receiver = '1319421581@qq.com'
# 发送主题

try:
# 编写HTML类型的邮件正文（把HTML代码写进入）
    msg = MIMEText('小王', 'html', 'utf-8')
    msg['Subject'] = Header('xiao', 'utf-8')
    # 连接发送邮件（smtplib模块基本使用格式）
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(user, psw)
    smtp.sendmail(sender, receiver, msg.as_string())
    print "邮件发送成功"
except smtplib.SMTPException:
    print "Error: 无法发送邮件"
smtp.quit()
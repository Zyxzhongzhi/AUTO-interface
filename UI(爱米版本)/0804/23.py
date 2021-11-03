#coding=utf-8
'''
time:2020/9/23 15:11
'''

# 正确发送邮件（一个收件人）

import smtplib
from email.mime.text import MIMEText
# 引入smtplib和MIMEText
from time import sleep
from email.header import Header

def sentemail():
    host = 'smtp.163.com'
    # 设置发件服务器地址
    port = 465
    # 设置发件服务器端口号。注意，这里有SSL和非SSL两种形式，现在一般是SSL方式
    sender = 'zyxzhongzhi@163.com'
    # 设置发件邮箱，一定要自己注册的邮箱
    pwd = 'LJRHHONJDQZHSRMS'
    # 设置发件邮箱的授权码密码，根据163邮箱提示，登录第三方邮件客户端需要授权码
    receiver = '1319421581@qq.com'
    # receiver = 'zyxzhongzhi@163.com'
    # receiver = 'kaiho_wang@163.com'
    # receiver = '1721471797@qq.com'
    # 设置邮件接收人，可以是QQ邮箱
    # body = '<h1>国庆正常上班</h1><p>zhongfs</p>'
    # 设置邮件正文，这里是支持HTML的
    # msg = MIMEText(body, 'html')
    msg = MIMEText('国庆正常上班,不乱码了', 'plain','utf-8')   #加了plain，表示text
    # 设置正文为符合邮件格式的HTML内容
    msg['subject'] = Header('放假通知','utf-8')
    # 设置邮件标题
    msg['from'] = sender
    # 设置发送人
    msg['to'] = receiver
    # 设置接收人
    try:
        s = smtplib.SMTP_SSL(host, port)
        # 注意！如果是使用SSL端口，这里就要改为SMTP_SSL
        s.login(sender, pwd)
        # 登陆邮箱
        s.sendmail(sender, receiver, msg.as_string())
        # 发送邮件！
        print ('Done.sent email success')
    except smtplib.SMTPException:
        print ('Error.sent email fail')


if __name__ == '__main__':
    sentemail()
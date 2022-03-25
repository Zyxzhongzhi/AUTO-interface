#coding=utf-8

from config import path
from public.utils import HTMLTestRunner3
from public.utils.mail import SendMail
# from HTMLTestRunnerCN import HTMLTestRunner
import time
import unittest

now = time.strftime('%Y-%m-%d-%H-%M-%S')
filename =path.report+'\\'+str(now)+'_ui.html'
def auto_all():

    start_dir = r'E:\桌面\PyCharm\0804\testcase'
    discover = unittest.defaultTestLoader.discover(start_dir=start_dir,pattern='te*.py')

    # now = time.strftime('%Y-%m-%d-%H-%M-%S')
    # print now

    # filename =path.report+'\\'+str(now)+'_ui.html'
    # print filename

    f = open(filename,'wb')
    runner = HTMLTestRunner3.HTMLTestRunner(
        stream=f,
        title=u'自动化测试报告',
        description=u'详细测试用例结果')

    runner.run(discover)
    f.close()

def send_mail():
    sm = SendMail(send_msg=filename, attachment=filename)
    sm.send_mail()


if __name__ == '__main__':
    auto_all()
    # send_mail()
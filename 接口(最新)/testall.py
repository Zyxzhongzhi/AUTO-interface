# coding = utf-8
'''
time:2021/5/11 13:34
'''


import HTMLTestRunner3
import time
import unittest

def auto_all():

    start_dir = r'E:\PycharmProjects\0511'
    discover = unittest.defaultTestLoader.discover(start_dir=start_dir,pattern='te*.py')

    now = time.strftime('%Y-%m-%d-%H-%M-%S')
    # print now

    filename =r'E:\PycharmProjects\0511\report'+'\\'+str(now)+'api_report.html'
    # print filename

    f = open(filename,'wb')
    runner = HTMLTestRunner3.HTMLTestRunner(
        stream=f,
        title=u'自动化测试报告',
        description=u'详细测试用例结果'
            )

    runner.run(discover)
    f.close()

if __name__ == '__main__':
    auto_all()

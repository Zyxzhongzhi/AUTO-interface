# coding = utf-8
'''
time:2021/5/11 13:33
'''
import unittest
import requests
import time

import HTMLTestRunner3
# from HTMLTestRunner3 import HTMLTestRunner
from base.test_data import testData as t
from base.demo import RequestHandler

class Test_Yuemi(unittest.TestCase):

    def setUp(self):
        self.run = RequestHandler()

    # @classmethod
    # def setUpClass(cls):
    #     cls.session = requests.Session()   #创建一个session对象

    def test001_studentList(self):
        res1 = self.run.visit("get", t.stuentList_url, t.stuentList_data).json()

        if res1['msg'] == u'获取成功':
            print("测试通过")
        else:
            print("测试失败")
        print(res1)



# coding = utf-8
'''
time:2021/5/24 11:02
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

    # media_type:1     课件资源
    def test001_resource_media_type1(self):
        res2 = self.run.visit("get", t.url, t.resource_media_type1).json()
        if res2['msg'] == u'获取课堂资源信息成功':
            print("测试通过")
        else:
            print("测试失败")
        print(res2)

    # media_type:2     图片资源
    def test002_resource_media_type2(self):
        res2 = self.run.visit("get", t.url, t.resource_media_type2).json()
        if res2['msg'] == u'获取课堂资源信息成功':
            print("测试通过")
        else:
            print("测试失败")
        print(res2)

    # media_type:3     视频资源
    def test003_resource_media_type3(self):
        res2 = self.run.visit("get", t.url, t.resource_media_type3).json()
        if res2['msg'] == u'获取课堂资源信息成功':
            print("测试通过")
        else:
            print("测试失败")
        print(res2)
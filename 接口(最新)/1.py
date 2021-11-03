# coding = utf-8
'''
time:2021/5/11 10:48
'''
import unittest
import requests
import time

import HTMLTestRunner3
from HTMLTestRunner3 import HTMLTestRunner

class Test_Yuemi(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.session = requests.Session()   #创建一个session对象
        # pass

    def test001_studentList(self):
        url = 'http://172.168.70.195:9901/api/z-paper-pen/get-paper-pen-basic-info'
        data = {
            't_mac': '58 - 41 - 20 - 29 - 9D - F4'
        }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.get(url, data)
        response = self.session.get(url, data)
        # print(response.text)
        # print(response.url)
        result = response.json()
        assert result['msg'] == u'获取成功'

    #
    # def test002_resource(self):
    #     url = 'http://172.168.70.195:9901/api/class/get-pp-class-resource'
    #     data = {
    #         'class_id': '1',
    #         'package_id': '2566',
    #         'source_type': '1',
    #         'media_type': '1'
    #     }
    #     headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    #     response = self.session.get(url, data)
    #     # print(response.text)
    #     # print(response.url)
    #     result = response.json()
    #     assert result['msg'] == u'获取课堂资源信息成功'
    #     # self.assertEqual(result['msg'],u'获取课堂资源信息成功')

# def all_case():
#     suite = unittest.TestSuite()
#     suite.addTest(Test_Yuemi("test001_studentList"))
#     suite.addTest(Test_Yuemi("test002_resource"))
#     return suite


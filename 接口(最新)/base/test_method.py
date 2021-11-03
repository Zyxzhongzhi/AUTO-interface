# coding = utf-8
'''
time:2021/5/11 13:54
'''
# import unittest
# import json
# import HTMLTestRunner3
# from .demo import RequestHandler
# from .test_data import testData as t
#
# class TestMethod(unittest.TestCase):
#     def setUp(self):
#         self.run = RequestHandler()
#     def test_01(self):
#         # url = 'http://172.168.70.195:9901/api/z-paper-pen/get-paper-pen-basic-info'
#         # data = {
#         #     'class': '1'
#         # }
#         res1 = self.run.visit("get", t.stuentList_url, t.stuentList_data).json()
#
#         if res1['msg'] == u'获取成功':
#             print("测试通过")
#         else:
#             print("测试失败")
#         print(res1)
#
#     def test_02(self):
#         # url = 'http://172.168.70.195:9901/api/class/get-pp-class-resource'
#         # data = {
#         #     'class_id': '1',
#         #     'package_id': '2566',
#         #     'source_type': '1',
#         #     'media_type': '1'
#         # }
#         res2 = self.run.visit('get', t.url, t.data).json()
#
#         if res2['msg'] == u'获取课堂资源信息成功':
#             print("测试通过")
#         else:
#             print("测试失败")
#         print(res2)
#
#
# if __name__ == '__main__':
#     unittest.main()
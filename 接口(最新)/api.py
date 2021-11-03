# coding = utf-8
'''
time:2021/5/11 10:07
'''

import requests

# url = 'http://172.168.70.195:9901/api/z-paper-pen/get-paper-pen-basic-info?class_id=1'
# data = {
#     'class':'1'
# }
# headers = {'Content-Type': 'application/x-www-form-urlencoded'}
# response = requests.request(method='post',url=url,data=data,headers=headers)
# print(response.text)
# print(response.json())
#
# result = response.json()
# if result['msg'] == u'获取成功':
#     print('成功')
#     assert True
# else:
#     print('失败')
#     assert False
#
# assert result['msg'] == u'成功！'

#
# url = 'http://172.168.70.195:9901/api/z-paper-pen/get-paper-pen-basic-info?class_id=1'
# params = {
#     'class':'1'
# }
# headers = {'Content-Type': 'application/x-www-form-urlencoded'}
# response = requests.get(url=url,params=params,headers=headers)
# print(response.text)
# print(response.json())
#
# result = response.json()
# # if result['msg'] == u'获取成功':
# #     print('成功')
# #     assert True
# # else:
# #     print('失败')
# #     assert False
#
# assert result['msg'] == u'获取成功'

#
# class Yuemi(object):
#
#     def __init__(self):
#         self.session = requests.Session()  #创建一个session对象、让登录接口和登录后的接口保持在同一个会话当中
#
#     def studentList(self):
#         url = 'http://172.168.70.195:9901/api/z-paper-pen/get-paper-pen-basic-info?class_id=1'
#         data = {
#             'class': '1'
#         }
#         headers = {'Content-Type': 'application/x-www-form-urlencoded'}
#         response = self.session.post(url=url,data=data,headers=headers)
#         print(response.text)
#
#     def resource(self):
#         url = 'http://172.168.70.195:9901/api/class/get-pp-class-resource?class_id=1&package_id=2566&source_type=1&media_type=1'
#         data = {
#             'class_id': '1',
#             'package_id': '2566',
#             'source_type': '1',
#             'media_type': '1'
#         }
#         headers = {'Content-Type': 'application/x-www-form-urlencoded'}
#         response = self.session.post(url=url,data=data,headers=headers)
#         print(response.text)
#
# if __name__ == '__main__':
#     c = Yuemi()   #创建对象
#     c.studentList()
#     c.resource()

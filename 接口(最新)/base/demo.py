# coding = utf-8
'''
time:2021/5/11 13:49
'''

import requests

class RequestHandler:
    def __init__(self):
        self.session = requests.session()

    def visit(self, method, url, params=None, data=None, json=None, headers=None):
        return self.session.request(method, url, params=params, data=data, json=json, headers=headers)

    def close_session(self):
        self.session.close()


# if __name__ == '__main__':
#     url = 'http://172.168.70.195:9901/api/class/get-pp-class-resource'
#     data = {
#         'class_id': '1',
#         'package_id': '2566',
#         'source_type': '1',
#         'media_type': '1'
#     }
#     req = RequestHandler()
#     resource = req.visit("get",url,data)
#     print(resource.json())
#     print(resource.url)
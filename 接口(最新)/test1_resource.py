# coding = utf-8
'''
time:2021/5/14 16:37
'''

import requests
from base.test_data import testData as t

url = 'http://172.168.70.195:9789/api/class/get-pp-class-resource'
data = {
        'class_id': '1',
        'package_id': '2566',
        'source_type': '2',
        'media_type': '1'
}
#
reponse = requests.get(url, data)
result = reponse.json()
# print(reponse.url)
print(reponse.json())
# assert result['msg'] == u'获取成功'

if result['msg'] == u'获取课堂资源信息成功':
    print('测试通过')
else:
    print('失败')

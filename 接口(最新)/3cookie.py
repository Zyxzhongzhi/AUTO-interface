# coding = utf-8
'''
time:2021/5/19 13:52
'''

import requests


#登录接口
# url = 'http://172.168.70.195/api/user/login'
# data = {
#     'usename': 'zhengyuxia',
#     'password': 'js123456'
# }
# login_res = requests.post(url, json=data)
# print(login_res.text)
#
# print(login_res.json())
# cookies = login_res.cookies
# print(cookies)

url = 'http://web.ktwelve.com.cn/'
data = {
    'usename': 'zhengyuxia',
    'password': 'js123456'
}
login_res = requests.post(url, json=data)
print(login_res.text)

print(login_res.json())
cookies = login_res.cookies
print(cookies)





# url = 'http://172.168.70.195/api/z-common/get-teacher-material-list'
# data = {
#     'period_id': '2',
#     'subject_id': '1',
#     'need_material': '1'
# }
#
# get_material = requests.post(url, data)
# print(get_material.json())

# import pypinyin
#
#
# stu_list = [{"name": "李四", "gender": 1}, {"name": "张三", "gender": 1},
#             {"name": "王五", "gender": 1}, {"name": "翟小", "gender": 1},
#             {"name": "啊本", "gender": 0}]
#
#
# def hanzi_to_pinyin(last_name):
#     """
#     功能说明：将姓名转换为拼音首字母缩写
#     参数：hanzi_to_pinyin(u'李白')
#     返回值：lb
#     """
#     rows = pypinyin.pinyin(last_name, style=pypinyin.NORMAL)  # 获取姓氏首字母
#     return ''.join(row[0][0] for row in rows if len(row) > 0)   # 拼接姓名首字母字符串
#
# # 按姓名首字母排序（不改变原列表方法）
# stu_list = sorted(stu_list, key=lambda x: hanzi_to_pinyin(x["name"][0]))
#
# # 按姓名首字母排序（改变原列表方法）
# # stu_list.sort(key=lambda x: hanzi_to_pinyin(x["name"][0]))
#
# print(stu_list)
#

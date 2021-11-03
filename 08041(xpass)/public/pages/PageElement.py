#coding=utf-8
'''
time:2020/9/10 13:12
'''

class PageElement:

    #登录元素定位
    teacher = ('class','student')
    userName = ('xpath','//*[@id="login-item"]/div[2]/div[1]/input')
    passWord = ('xpath','//*[@id="login-item"]/div[2]/div[2]/input')
    loginBtn = ('xpath','//*[@id="login-item"]/div[2]/div[4]/span')
    loginOut = ('xpath','//*[@id="um"]/p[1]/a[7]')

    #回到首页
    index = ('xpath','//*[@id="mn_forum"]/a')


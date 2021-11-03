#coding=utf-8
'''
time:2020/9/10 13:12
'''

class PageElement:

    #登录元素定位
    teacher = ('class','teacher')
    student = ('class', 'student')
    userName = ('xpath','//*[@id="login-item"]/div[2]/div[1]/input')
    passWord = ('xpath','//*[@id="login-item"]/div[2]/div[2]/input')
    loginBtn = ('xpath','//*[@id="login-item"]/div[2]/div[4]/span')
    loginOut = ('xpath','//*[@id="index"]/div[1]/div[2]/div[2]/span[3]/span')

    #课堂互动
    #点名
    ketanghudong = ('class','interaction-name')
    dianming = ('class','call-index')
    kaishiqiangda = ('class','interact-answer-btn')
    suijidianming = ('class','random-smoke')
    shiyongqiangda = ('class','next-interact')
    jiesuqiangda = ('class','interact-answer-btn')
    close = ('class','interact-close')
    #锁屏
    suopingkai = ('class','lock-screen-index')
    suopingguan = ('class','lock-screen-index lock-screen-active')

    baiban = ('class','handwrite-index')
    beijingse = ('class','select-background-color')
    zise = ('xpath','//*[@id="handWrite"]/div[2]/div/p[6]/span[1]')
    xiankuan = ('xpath','//*[@id="handWrite"]/div[2]/div/p[7]/span[1]')
    chexiao = ('class','recall')
    huifu = ('class','refresh')
    qingping = ('class','clear')


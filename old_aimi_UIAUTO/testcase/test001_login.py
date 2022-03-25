#coding=utf-8
from selenium import webdriver
from public.pages.BasePage import BasePage
from public.pages.PageElement import PageElement as p
from public.utils.ReadConfigIni import ReadConfigIni
from config.path import *
from time import sleep
import unittest
import time
import os

read= ReadConfigIni(os.path.join(config,'config.ini'))
url = read.get_ini_data('env1','url')
username = read.get_ini_data('env1','username')
password = read.get_ini_data('env1','password')
# print url

# @unittest.skip
class Yuemi(BasePage):

    @classmethod
    def setUpClass(cls):
        driver = webdriver.Chrome()
        BasePage.set_driver(driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        # BasePage.go_home(p.index)

    def test001_login(self):
        driver = BasePage.get_driver()
        driver.get(url)
        driver.maximize_window()
        sleep(2)
        #点击教师端
        elem = BasePage.find_element(p.teacher)
        # #点击学生端
        # elem = BasePage.find_element(p.student)
        BasePage.click()
        sleep(1)
        #1.输入账号
        elem = BasePage.find_element(p.userName)
        BasePage.send_keys(username)
        sleep(1)
        #2.输入密码
        elem = BasePage.find_element(p.passWord)
        BasePage.send_keys(password)
        sleep(1)
        #3.点击登录
        elem = BasePage.find_element(p.loginBtn)
        BasePage.click()
        sleep(2)
        #4.进行断言
        value = BasePage.get_text(p.loginOut)
        # print value
        assert value == u'退出'
        sleep(2)

if __name__ == '__main__':
    unittest.main()
#     testunit = unittest.TestSuite()#初始化测试用例集合对象，构建测试套件
#     testunit.addTest(Baidu("test_baidu_search"))#把测试用例加入到测试用力集合中去，将用例加入到检测套件中
#     fp = open('./result.html','wb')#定义测试报告存放路径
#     runner = HTMLTestRunner(stream=fp,title='百度搜索测试报告',description='用例执行情况')#定义测试报告
#     runner.run(testunit)#执行测试用例
#     fp.close()


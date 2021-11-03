#coding=utf-8
'''
time:2020/8/13 11:14
'''
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
url = read.get_ini_data('env','url')
username = read.get_ini_data('env','username')
password = read.get_ini_data('env','password')
# print url

@unittest.skip
class Yuemi(BasePage):

    @classmethod
    def setUpClass(cls):
        driver = webdriver.Chrome()
        BasePage.set_driver(driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test002_dianming(self):
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
        #4.点击课堂互动
        elem = BasePage.find_element(p.ketanghudong)
        BasePage.click()
        #5.点击点名
        elem = BasePage.find_element(p.dianming)
        BasePage.click()
        #6.






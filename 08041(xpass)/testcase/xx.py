#coding=utf-8
'''
time:2020/8/21 17:10
'''
import selenium.webdriver

driver = selenium.webdriver.Chrome()
driver.get('http://testyuemi.ziyuenet.com.cn:8282')
driver.find_element_by_class_name('teacher').click()
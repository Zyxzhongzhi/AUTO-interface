# coding = utf-8
'''
time:2021/5/26 16:25
'''

from selenium import webdriver
from public.utils.ReadConfigIni import ReadConfigIni
from config.path import *
import os
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

read = ReadConfigIni(os.path.join(config, 'config.ini'))
url = read.get_ini_data('env', 'url')
# print(url)
driver = webdriver.Chrome()
driver.get("http://172.168.70.195")
sleep(2)
driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[1]/div[2]/div[1]/input').send_keys('zhengyuxia')

driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[1]/div[2]/div[2]/input').send_keys('js123456')

sleep(5)  #等待时间输入验证码
driver.find_element_by_class_name('login').click()
driver.maximize_window()
sleep(2)
#作业
# driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[3]/div/div[2]/div/div[4]').click()
driver.find_element_by_xpath('//div[text()="作业"]').click()
sleep(2)
#布置课外作业
# driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/div[2]/div[2]/div/div[1]/span[2]/span/a').click()
# driver.find_element_by_xpath('//a[text()="课外作业"]').click()
driver.find_element_by_link_text('作业')
sleep(2)
#选题添题组卷
# driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/form/div[2]/div/div/ul[1]/li[1]/p').click()
driver.find_element_by_xpath('//p[text()="选题添题组卷"]').click()
sleep(4)
#添加题目
# driver.find_element_by_xpath('//*[@class="resource_main"]/li[1]/span[contains(text(),"添加")]/../text()]').click()

# MoveElement = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[2]/ul/li[1]/div/div[6]/div[2]/span[3]')
# sleep(2)
# Action = ActionChains(driver)
#单选题
driver.find_element_by_xpath('//*[@class="title"]/p/span[text()="单选题"]').click()
driver.find_element_by_link_text('')
sleep(1)
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[2]/ul/li[1]/div/div[6]/div[2]/span[3]').click()
#多选题
# driver.find_element_by_xpath('//span[text()="多选题"]').click()
# sleep(1)
# driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[2]/ul/li[1]/div/div[6]/div[2]/span[3]').click()
#
# #简答题
# driver.find_element_by_xpath('//span[text()="简答题"]').click()
# sleep(1)
# driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[2]/ul/li[1]/div/div[6]/div[2]/span[3]').click()


# driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[2]/ul/li[1]/div/div[6]/div[2]/span[3]').click()
# target = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[2]/ul/li[2]/div/div[6]/div[2]/span[3]')
# driver.execute_script('arguments[0].scrollIntoView();', target)
# driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[2]/ul/li[1]/div/div[6]/div[2]/span[4]').click()
# sleep(2)
# #点击试题篮
# driver.find_element_by_xpath('//span[text()="试题篮"]').click()
# sleep(2)
# #点击去组卷（可录入）
# driver.find_element_by_xpath('//span[text()="去组卷（可录入）"]').click()
# sleep(2)
#
# driver.find_element_by_xpath('//span[text()="确定"]').click()
# sleep(2)
#
# driver.quit()

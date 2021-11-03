#coding=utf-8
'''
time:2020/8/13 11:28
'''
from selenium import webdriver
import unittest

class BasePage(unittest.TestCase):

    @classmethod
    def set_driver(cls,driver):
        cls.driver = driver

    @classmethod
    def get_driver(cls):
        return cls.driver


    @classmethod
    def find_element(cls,element):
        type = element[0]
        value = element[1]
        if type == 'id':
            cls.elem = cls.driver.find_element_by_id(value)
        elif type == 'class':
            cls.elem = cls.driver.find_element_by_class_name(value)
        elif type == 'xpath':
            cls.elem = cls.driver.find_element_by_xpath(value)
        else:
            raise NameError('please input correct params')
        return cls.elem

    @classmethod
    def send_keys(cls,text):
        return cls.elem.send_keys(text)

    @classmethod
    def click(cls):
        cls.elem.click()

    @classmethod
    def get_text(cls,elem):
        return BasePage.find_element(elem).text

#
# if __name__ == '__main__':
#     b = BasePage()
#     baidu_input = ('id', 'kw')
#     b.find_element(baidu_input)




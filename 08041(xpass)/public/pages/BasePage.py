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
            elem = cls.driver.find_element_by_id(value)
        elif type == 'class':
            elem = cls.driver.find_element_by_class_name(value)
        elif type == 'xpass':
            elem = cls.driver.find_element_by_xpass(value)
        else:
            raise NameError('please input correct params')
        return elem

    @classmethod
    def send_keys(cls,elem,text):
        return elem.send_keys(text)

    @classmethod
    def click(cls,elem):
        elem.click




#
# if __name__ == '__main__':
#     b = BasePage()
#     baidu_input = ('id', 'kw')
#     b.find_element(baidu_input)




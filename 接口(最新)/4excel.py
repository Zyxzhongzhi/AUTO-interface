# coding = utf-8
'''
time:2021/5/24 13:38
'''

import os
import xlrd
import json


# class ExcelUtil():
#    def __init__(self,excelPath,sheetName):
#       self.data = xlrd.open_workbook(excelPath)
#       self.table = self.data.sheet_by_name(sheetName)
#       print(self.table)
#       self.keys = self.table.row_values(0)
#       self.rowNum = self.table.nrows
#       print(self.rowNum)
#       self.colNum = self.table.ncols
#       print(self.colNum)
#       self.rowValue = self.table.row_values(1)
#       print(self.rowValue)
#       self.wsheet = self.data.sheet_by_index(0)
#       print(self.wsheet)
#    def dict_data(self):
#       lst = []
#       # if self.rowNum >= 1:
#       dic = dict.fromkeys(self.wsheet.row_values(0))
#       print('dic'%(dic))
#       for i in range(self.rowNum):
#          for j in range(self.wsheet.row_len(i)):
#             dic[self.wsheet.cell_value(0, j)] = self.wsheet.cell_value(i, j)
#          yield dict
#       print(lst)
#       # for i in range(1, nor):
#       #    for j in range(nol):
#       #       title = table.cell_value(0, j)
#       #       value = table.cell_value(i, j)
#       #       # print value
#       #       dict[title] = value
#       #    yield dict
#
#
# if __name__ == '__main__':
#     e = ExcelUtil(r'E:\data.xls','纸笔课堂')
#     for i in dict_data():
#        print(i)
# # r'E:\data.xls''纸笔课堂'


import xlrd

def get_data(dir_case, sheetnum):

   data = xlrd.open_workbook(dir_case)
   table = data.sheets()[sheetnum]
   nor = table.nrows
   nol = table.ncols
   dict = {}
   for i in range(1, nor):
      for j in range(nol):
         title = table.cell_value(0, j)
         value = table.cell_value(i, j)
         # print value
         dict[title] = value
      yield dict

'''        
• yield 是一个类似 return 的关键字，只是这个函数返回的是个生成器
• 当你调用这个函数的时候，函数内部的代码并不立马执行 ，这个函数只是返回一个生成器对象
• 当你使用for进行迭代的时候，函数中的代码才会执行
'''
if __name__ == '__main__':
   for i in get_data(r'E:\data.xls', 0):
      print(i)
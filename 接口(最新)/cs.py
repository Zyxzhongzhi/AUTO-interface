# coding = utf-8
'''
time:2021/5/24 13:59
'''
import xlrd
from datetime import datetime, date

workbook = xlrd.open_workbook(r'E:\data.xls')
sheet1_object = workbook.sheet_by_name("纸笔课堂")
# sheets = workbook.sheet_names()
# sheet1 = workbook.sheet_by_index(0)
# sheet2 = workbook.sheet_by_name("Sheet2")
# if sheet1.cell_type(1, 3)  == 3:
# 	sheet1.cell_type(1, 3).tuple = xlrd.xldata_as_tuple(sheet1.cell_value(1, 3), datemode=0)
#
# date(*sheet1.cell_type(1, 3).tuple[:3]).strftime('%Y/%m/%d')
# print(sheet1.row(1))
# print(sheet1.row_values(0))
# print(sheet1.col(0))
# print(sheet1.cell_value(1, 3))
# print(sheet1.cell_type(1, 3))

# import datetime
# workbook = xlrd.open_workbook("测试.xlsx")
# sheet2_object = workbook.sheet_by_name("Sheet2")
# value_type = sheet1_object.cell(1, 3).ctype
# value_type = sheet1_object.cell_type(1, 3)
# print(value_type)  # 结果：3
# if value_type == 3:
#     print("单元格数据为日期")
#     cell_value = sheet1_object.cell_value(1, 3)
#     print(cell_value)  # 结果：44340.0
#     date_tuple = xlrd.xldate_as_tuple(cell_value, workbook.datemode)
#     print(date_tuple)  # 结果：(2021, 5, 24, 0, 0, 0)
# print(date(*date_tuple[:3]).strftime('%Y/%m/%d'))

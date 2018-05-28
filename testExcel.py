# coding=utf-8
'''
File: testExcel.py
Project: test
File Created: Monday, 28th May 2018 4:39:06 pm
Author: <<dpj>> (<<idle0423@126.com>>)
'''

# import xlrd
import xlwt

# book = xlrd.open_workbook("test.xls")
# print book.nsheets
# print book.sheets()
# print book.sheet_names()

# sheet = book.sheets()[0]
# print sheet
# sheet = book.sheet_by_index(0)
# print sheet
# sheet = book.sheet_by_name(u"Sheet1")
# print sheet
# print sheet.nrows
# print sheet.ncols
# print sheet.name

# print sheet.row(1)
# print sheet.row_values(1)

# print sheet.col(1)
# print sheet.col_values(1)

# cell = sheet.cell(1, 2)
# cell_value = sheet.cell_value(1, 2)
# print cell_value
# cell_value = sheet.cell(1, 2).value
# print cell_value

# print xlrd.xldate_as_tuple(sheet.cell(6, 3).value, 0)
# print xlrd.xldate_as_datetime(sheet.cell(6, 3).value, 0)

print ("_______________________")
book = xlwt.Workbook()
sheet = book.add_sheet("Sheet1")
book.save("myExcel.xls")

# 字体
font = xlwt.Font()
font.name = "Time New Roman"
font.bold = True
font.underline = True
font.italic = True
# 创建一个格式
sytle = xlwt.XFStyle()
# 设置格式字体
sytle.font = font
sheet.write(0, 0, "Formatted value", sytle)
book.save("myExcel.xls")

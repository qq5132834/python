#coding=utf-8
from xlutils.copy import copy
import xlrd
import xlwt

# 保存为97-2003的格式

if __name__ == "__main__":
    tem_excel = xlrd.open_workbook("D:/development/github/python3/demo1/日统计.xls", formatting_info=True)
    tem_sheet = tem_excel.sheet_by_index(0)
    new_excel = copy(tem_excel)
    new_sheet = new_excel.get_sheet(0)

    style = xlwt.XFStyle()

    # 字体
    font = xlwt.Font()
    font.name = '微软雅黑'
    font.bold = True
    font.height = 18 * 20  # 字体大小都必须乘以20
    style.font = font

    # 设置边框
    borders = xlwt.Borders()
    borders.top = xlwt.Borders.THIN
    borders.bottom = xlwt.Borders.THIN
    borders.left = xlwt.Borders.THIN
    borders.right = xlwt.Borders.THIN
    style.borders = borders

    # 对齐
    alignment = xlwt.Alignment()
    alignment.horz = xlwt.Alignment.HORZ_CENTER
    alignment.vert = xlwt.Alignment.VERT_CENTER
    style.alignment = alignment

    new_sheet.write(2, 1, 12, style)
    new_sheet.write(3, 1, 12, style)
    new_sheet.write(4, 1, 12, style)
    new_sheet.write(5, 1, 12, style)
    new_excel.save('D:/development/github/python3/demo1/日统计1.xls')

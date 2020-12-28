#coding=utf-8
import xlrd
#pip install xlrd==1.2.0
import xlwt
#pip install xlwt==1.2.0  对应的是xls后缀文件

##主要是excel的读写

def xlrdFunction():
    excelFile = '''D:/development/github/python3/demo1/hello.xlsx'''
    print(excelFile)
    xlsx = xlrd.open_workbook(excelFile)
    table = xlsx.sheet_by_index(0)
    table = xlsx.sheet_by_name("demo")
    print(table.cell_value(1, 1))
    print(table.cell(1, 1).value)
    print(table.row(1)[1].value)
    return


def xlwtFunction():
    excelFile = '''D:/development/github/python3/demo1/hello1.xls'''
    new_workbook = xlwt.Workbook()
    worksheet = new_workbook.add_sheet('demo_xlwt')
    worksheet.write(0, 0, 'test')
    new_workbook.save(excelFile)
    return


if __name__ == "__main__":
    print('helloworld.')
    xlrdFunction()
    xlwtFunction()

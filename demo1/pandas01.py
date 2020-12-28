import pandas as pd
import numpy as np
import random


def readXlsx():
    print('read')
    sheet = pd.read_excel('D:/development/github/python3/demo1/pandas/user.xlsx', 0)

    # sheet = pd.read_excel('D:/development/github/python3/demo1/pandas/user.xlsx', sheet_name='001')
    print('----------------------第一行---------------------')
    labels = list(sheet.columns.values)
    print(labels)
    print('----------------------')
    print(sheet.loc[0][0])
    print(sheet.loc[0][1])
    print(sheet.loc[0][2])
    print(sheet.loc[0][3])
    print('----------------------')

    data = np.array(sheet.loc[:, :])
    print(data)

    return


def writeXlsx():
    print('write')
    sheet = pd.read_excel('D:/development/github/python3/demo1/pandas/user.xlsx', 0)
    print("-------------------")
    print(sheet)
    print("-------------------")
    print(type(sheet))
    print("-------------------")
    sheet1 = sheet.copy()
    sheet1.loc[0, 'name'] = 'a'

    print(sheet1)
    df = pd.DataFrame(sheet1)

    df = df.style.set_properties(**{
        'background-color': 'grey',
        'font-size': '20pt',
    })

    df = sheet.style
    df.to_excel('D:/development/github/python3/demo1/pandas/222.xlsx', sheet_name='001', index=False, header=True)
    return


if __name__ == '__main__':
    # print('hello')
    # readXlsx()
    writeXlsx()

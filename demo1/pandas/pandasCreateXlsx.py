import pandas as pd

if __name__ == "__main__":
    print('hello world.')
    dict = {"id": [1, 2, 3], "name": ["lucy", "lilei", "liaohuang"]}
    df = pd.DataFrame(dict)
    print(df)
    df = df.set_index("id") #设置索引
    print("---------------------")
    print(df)
    df.to_excel("D:/pandasCreateXlsx.xlsx")

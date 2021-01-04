import pandas as pd

if __name__ == "__main__":
    print("hello world.")
    df = pd.read_excel("d:/hello.xlsx")
    print(df.shape)
    print(df.columns) #
    print(df.head())  # 默认5行
    print(df.head(3))  # 前3行
    print(df.tail(3))  # 后3行

    # 当出现head错误，就是excel文件第一行是乱数据的时候回，第二行才是head的时候
    df1 = pd.read_excel("d:/hello.xlsx", header=1)  # 默认header==0，现在设置header=1，从第1行开始
    df2 = pd.read_excel("d:/hello.xlsx", header=None)  # 当excel文件中没有头的时候
    df2.columns = ['id', 'name', 'age', 'iphone']
    df2.set_index("id", inplace=True)
    print(df2.columns)
    df2.to_excel("d:/hello1.xlsx")

    df3 = pd.read_excel("D:/hello.xlsx", index_col="id")  #指定header的index索引
    df4 = pd.read_excel("D:/hello.xlsx", skiprows=3, usecols="C:F")
    #有时候数据在excel中的中间，如果要读取中间的数据的话，跳过3行，使用CDEF4列的数据



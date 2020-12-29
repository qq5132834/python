import pandas as pd

# xlsx的行、列、单元格

if __name__ == "__main__":
    dict = {"x": 100, "y": 200, "z": 300}
    print(dict.keys())
    print(dict.values())
    print(dict["x"])

    # 字典转Series
    s1 = pd.Series(dict)
    print(s1)
    print(s1.index)
    print(s1.values)
    print(s1["x"])

    print("================================")

    L1 = [100, 200, 300]
    L2 = ["x", "y", "z"]
    s2 = pd.Series(L1, index=L2)
    print(s2)
    print(s2.index)
    print(s2.values)
    print(s2["x"])

    print("================================")

    s1 = pd.Series([1, 2, 3], index=[1, 2, 3], name='A')
    s2 = pd.Series([10, 20, 30], index=[1, 2, 3], name='B')
    s3 = pd.Series([100, 200, 300], index=[1, 2, 3], name='C')
    df = pd.DataFrame({s1.name: s1, s2.name: s2, s3.name: s3})
    print(df)
    df = pd.DataFrame({s1, s2, s3})
    print(df)

    print("================================")

    book = pd.read_excel("D:/hello.xlsx")
    print(type(book)) # 数据类型是Serial
    book["id"].at[0] = 100 #设置id列一个单元格的值

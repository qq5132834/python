import pymysql
# 新库 xlsxwriter as xw
# 新库 openpyxl

if __name__ == '__main__':
    print('pymysql')
    # url = 'jdbc:mysql://gz-cdb-9aun2cpz.sql.tencentcdb.com:62101/dev_public?useUnicode=true&characterEncoding=utf8&max_allowed_packet=16M&allowMultiQueries=true'
    username = 'sanydev'
    password = 'dev5tgb*UHB'
    database = pymysql.connect('gz-cdb-9aun2cpz.sql.tencentcdb.com',
                               username,
                               password,
                               'dev_public',
                               62101,
                               charset='utf8')
    cursor = database.cursor()
    cursor.execute("SELECT * from pub_channel_bill")
    # data = cursor.fetchone()
    data = cursor.fetchall()
    # print(data)
    for i in data:
        print(i)
    print('pymysql')
    # 关闭数据库连接
    database.close()
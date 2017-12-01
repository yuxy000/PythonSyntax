import pymysql

# open db
db = pymysql.connect("localhost", "root", "5720", "testdb")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 语句
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')

try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # 如果发生错误则回滚
    db.rollback()

# 关闭数据库连接
db.close()

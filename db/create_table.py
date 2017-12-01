import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "5720", "testdb")

# 使用cursor() 方法创建一个游标对象
cursor = db.cursor()

# 创建数据表
# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# 使用预处理语句创建表
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME CHAR(20) NOT NULL,
         LAST_NAME CHAR(20),
         AGE INT,
         SEX CHAR(1),
         INCOME FLOAT )"""

# 关闭数据库
db.close()

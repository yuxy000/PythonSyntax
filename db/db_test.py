"""
什么是 PyMySQL？
    PyMySQL 是在 Python3.x 版本中用于连接 MySQL 服务器的一个库，Python2中则使用mysqldb。
    PyMySQL 遵循 Python 数据库 API v2.0 规范，并包含了 pure-Python MySQL 客户端库。
PyMySQL 安装
在使用 PyMySQL 之前，我们需要确保 PyMySQL 已安装。
PyMySQL 下载地址：https://github.com/PyMySQL/PyMySQL。
如果还未安装，我们可以使用以下命令安装最新版的 PyMySQL：
    $ pip install PyMySQL
如果你的系统不支持 pip 命令，可以使用以下方式安装：
1、使用 git 命令下载安装包安装(你也可以手动下载)：
    $ git clone https://github.com/PyMySQL/PyMySQL
    $ cd PyMySQL/
    $ python3 setup.py install
2、如果需要制定版本号，可以使用 curl 命令来安装：
    $ # X.X 为 PyMySQL 的版本号
    $ curl -L https://github.com/PyMySQL/PyMySQL/tarball/pymysql-X.X | tar xz
    $ cd PyMySQL*
    $ python3 setup.py install
    $ # 现在你可以删除 PyMySQL* 目录
注意：请确保您有root权限来安装上述模块。
"""
import pymysql

# 数据库连接
"""
连接数据库前，请先确认以下事项：
    您已经创建了数据库 TESTDB.
    在TESTDB数据库中您已经创建了表 EMPLOYEE
    EMPLOYEE表字段为 FIRST_NAME, LAST_NAME, AGE, SEX 和 INCOME。
    连接数据库TESTDB使用的用户名为 "testuser" ，密码为 "test123",你可以可以自己设定或者直接使用root用户名及其密码，Mysql数据库用户授权请使用Grant命令。
    在你的机子上已经安装了 Python MySQLdb 模块。
"""

# 打开数据库连接
db = pymysql.connect("localhost", "root", "5720", "testdb")

# 使用cursor() 方法创建一个游标对象
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print("Database version: %s" % data)

# 关闭数据库
db.close()

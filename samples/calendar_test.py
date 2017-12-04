# _*_ coding: utf-8 _*_

"""
---------------------------------
@Time     : 2017/12/4 15:48
@Author   : yuxy
@File     : calendar_test.py
@Project  : PythonSyntax
----------------------------------
"""

import calendar

# 输入指定年月
yy = int(input("输入年份:"))
mm = int(input("输入月份:"))

# 显示日历
print(calendar.month(yy, mm))

# _*_ coding: utf-8 _*_

"""
---------------------------------
@Time     : 2017/12/5 18:03
@Author   : yuxy
@File     : leapyear_test.py
@Project  : PythonSyntax
----------------------------------
"""
year = int(input("请输入一个年份："))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("{0}是闰年".format(year))
else:
    print("{0}不是闰年".format(year))

# _*_ coding: utf-8 _*_

"""
---------------------------------
@Time     : 2017/12/5 13:51
@Author   : yuxy
@File     : asciitochar_test.py
@Project  : PythonSyntax
----------------------------------
"""
"""
ASCII码与字符相互转换
"""

# 用户输入字符
c = input("请输入一个字符: ")

# 用户输入ASCII码，并将输入的数字转为整型
a = int(input("请输入一个ASCII码: "))

print(c, "的ASCII码为", ord(c))    # ord()字符转ASCII码
print(a, "对应的字符为", chr(a))   # chr()ASCII码转字符



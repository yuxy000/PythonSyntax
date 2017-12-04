# _*_ utf-8 _*_

"""
---------------------------------
@Time     : 2017/12/4 15:21
@Author   : yuxy
@File     : str_judge_test.py
@Project : PythonSyntax
----------------------------------
"""

# 测试实例一
print("测试实例一")
str1 = "runoob.com"
print(str1.isalnum())   # 判断所有字符都是数字或者字母
print(str1.isalpha())   # 判断所有字符都是字母
print(str1.isdigit())   # 判断所有字符都是数字
print(str1.islower())   # 判断所有字符都是小写
print(str1.isupper())   # 判断所有字符都是大写
print(str1.istitle())   # 判断所有单词都是首字母大写，像标题
print(str1.isspace())   # 判断所有字符都是空白字符、\t、\n、\r

print("--------------------------------")

# 测试实例二
print("测试实例二")
str2 = "runoob"
print(str2.isalnum())
print(str2.isalpha())
print(str2.isdigit())
print(str2.islower())
print(str2.isupper())
print(str2.istitle())
print(str2.isspace())


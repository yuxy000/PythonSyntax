# _*_ utf-8 _*_

"""
---------------------------------
@Time     : 2017/12/4 15:30
@Author   : yuxy
@File     : file_io_test.py
@Project  : PythonSyntax
----------------------------------
"""

# 写文件 指定文件的编码格式
with open("../tmp/test.txt", "w+", encoding='utf8') as out_file:
    out_file.write("该文本会写入到文件中\n看到我了吧！")

# 读文件 #指定文件的编码格式
with open("../tmp/test.txt", "r+", encoding='utf8') as in_file:
    txt = in_file.read()

print(txt)

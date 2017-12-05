# _*_ coding: utf-8 _*_

"""
---------------------------------
@Time     : 2017/12/5 14:22
@Author   : yuxy
@File     : multitable_test.py
@Project  : PythonSyntax
----------------------------------
"""
# 九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print('{}*{}={}\t'.format(j, i, i*j), end='')
    print()


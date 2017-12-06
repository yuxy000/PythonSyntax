#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
---------------------------------
@Time     : 2017/12/6 14:16
@Author   : yuxy
@File     : quadratic_test.py
@Project  : PythonSyntax
----------------------------------
"""

import math


def quadratic(a, b, c):
    for i in (a, b, c):
        if not isinstance(i, (int, float)):
            raise TypeError('数据类型输入有误，请重新输入！')
    delta = b ** 2 - 4 * a * c
    n = -b / (2 * a)
    if a == 0:
        print('此方程不是一元二次方程！')
    elif delta == 0:
        print('该一元二次方程只有一个根：', n)
    elif delta < 0:
        print('该一元二次方程没有解!')
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return x1, x2


A = int(input('请输入数字a:'))
B = int(input('请输入数字b:'))
C = int(input('请输入数字c:'))
print('你要解答的一元二次方程是:', A, ' * XX+', B, '* X+', C, '= 0')
print('该方程的根为:', quadratic(A, B, C))

# _*_ coding: utf-8 _*_

"""
---------------------------------
@Time     : 2017/12/5 13:28
@Author   : yuxy
@File     : lcm_test.py
@Project  : PythonSyntax
----------------------------------
"""

"""
求最小公倍数
思路：
1.当最大值为最小公倍数时，返回最大值；
2.当最大值不为最小公倍数时，最小公倍数为最大值的倍数。
"""


def lcm(a, b):
    if b > a:
        a, b = b, a
    if a % b == 0:
        return a    # 判断a是否为最小公倍数
    mul = 2         # 最小公倍数为最大值的倍数
    while a * mul % b != 0:
        mul += 1
    return a * mul


while True:
    a = int(input("Input 'a':"))
    b = int(input("Input 'b':"))
    print(lcm(a, b))


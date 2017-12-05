# _*_ coding: utf-8 _*_

"""
---------------------------------
@Time     : 2017/12/5 14:27
@Author   : yuxy
@File     : primenum_test.py
@Project  : PythonSyntax
----------------------------------
"""
import math

"""
检测用户输入的数字是质数还是合数
原理是用了开根号法：
假如一个数N是合数,它有一个约数a,那么有a×b=N
则a、b两个数中必有一个大于或等于根号N,一个小于或等于根号N。
因此,只要小于或等于根号N的数（1除外）不能整除N,则N一定是素数。
"""

# 用户输入数字
num = int(input("请输入一个数字: "))

# 质数大于 1
if num > 1:
    # 找到其平方根（ √ ），减少算法时间
    sqrt_num = math.floor(num ** 0.5)
    # 查找其因子
    for i in range(2,sqrt_num + 1):
        if num % i == 0:
            print(num, "是合数")
            print(i, "乘于", num // i, "是", num)
            break
    else:
        print(num, "是质数")
# 如果输入的数字小于或等于 1，不是质数
else:
    print(num, "既不是质数，也不是合数")

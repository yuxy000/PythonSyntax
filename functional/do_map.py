#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
---------------------------------
@Time     : 2017/12/7 11:15
@Author   : yuxy
@File     : do_map.py
@Project  : PythonSyntax
----------------------------------
"""

from functools import reduce

# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回


def f(x):
    return x ** 2


r = map(f, [1, 2, 3, 4, 5, 6])
print(list(r))

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
# str转换为int的函数
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def fn(x, y):
    return x * 10 + y


def char2num(s):
    return DIGITS[s]


print(reduce(fn, map(char2num, '13789')))


# str2int 函数
def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s_char):
        return DIGITS[s_char]
    return reduce(fn, map(char2num, s))


# lambda函数 str2int
def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


# 练习
# 1. 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
def normalize(name):
    return name.title()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


# 编写一个prod()函数，可以接受一个list并利用reduce()求积
def prod(L):
    return reduce(leiji, L)


def leiji(x, y):
    return x * y


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


# 利用map和reduce编写一个str2float函数
def str2float(s):
    # n = s[::-1].find('.')
    n = s.rfind('.')
    left, right = s.split('.')
    integral = reduce(lambda x, y: x * 10 + y, map(lambda c: DIGITS[c], left))
    decimal = reduce(lambda x, y: x * 10 + y, map(lambda c: DIGITS[c], right))
    return integral + decimal / 10 ** n


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
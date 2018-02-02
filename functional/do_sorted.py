#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
---------------------------------
@Time     : 2017/12/7 15:07
@Author   : yuxy
@File     : do_sorted.py
@Project  : PythonSyntax
----------------------------------
"""
print(sorted([36, 5, -12, 9, -21]))
# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
print(sorted([36, 5, -12, 9, -21], key=abs))

# 字符串排序
# 默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
# 忽略大小写的排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
# 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True：
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(stu):
    return stu[0]


def by_score(stu):
    return stu[1]


L2 = sorted(L, key=by_name)
print(L2)

L3 = sorted(L, key=by_score, reverse=True)
print(L3)

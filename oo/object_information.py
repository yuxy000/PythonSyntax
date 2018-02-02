#!usr/bin/env python3
# _*_ coding:utf-8 _*_

"""
-------------------------------
@Author:    yuxy
@Time:      2018/2/2 15:45
@File:      object_information.py
@Project:   PythonSyntax
--------------------------------
"""
import types

# type() 获取对象类型
print(type(123))
print(type('str'))
print(type(None))
print(type(abs))
print(type(113) == type(456))
print(type(12) == int)
print(type('123') == str)
print(type(123) == type('223'))
print(isinstance(23, int))
"""
isinstance() 与 type() 区别：
    type() 不会认为子类是一种父类类型，不考虑继承关系。
    isinstance() 会认为子类是一种父类类型，考虑继承关系。
如果要判断两个类型是否相同推荐使用 isinstance()。
"""


def fn():
    pass


print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(isinstance(lambda x: x, types.LambdaType))


print(isinstance([1, 2, 3], (list, tuple)))


# 使用dir() 获得一个对象的所有属性和方法

#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
---------------------------------
@Time     : 2017/12/7 16:31
@Author   : yuxy
@File     : do_decorator.py
@Project  : PythonSyntax
----------------------------------
"""
import functools
import time


def now():
    print('2015-3-25')


print(now.__name__)
f = now
print(f.__name__)


# 在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s()' % func.__name__)
        return func(*args, **kw)
    return wrapper


# 借助Python的@语法，把decorator置于函数的定义处
@log
def print_time():
    print('2017-12-07')


print_time()


# 带有参数的装饰器
def log_prarm(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log_prarm('execute')
def print_now():
    print('2017-12-07')


print_now()
print(print_now.__name__)


def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        print('%s executed in %s ms' % (fn.__name__, 10.24))
        return fn(*args, **kw)
    return wrapper


@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


print(fast(11, 22), fast.__name__)


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')

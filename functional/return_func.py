#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
---------------------------------
@Time     : 2017/12/7 15:22
@Author   : yuxy
@File     : return_func.py
@Project  : PythonSyntax
----------------------------------
"""
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax
    return sum


f = lazy_sum(1, 3, 5, 7, 9)
print(f)
print(f())


# 利用闭包返回一个计数器函数，每次调用它返回递增整数：
def create_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count
    return counter


counterA = create_counter()
print(counterA(), counterA(), counterA(), counterA(), counterA())    # 1 2 3 4 5
counterB = create_counter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')


# 2
def createCounter():
    fs = [0]

    def counter():
        fs[0] = fs[0] + 1
        return fs[0]
    return counter


# 3
def createCounter():
    def counter():
        i = 1
        while True:
            yield i
            i += 1
    return counter().__next__

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')


L = list(filter(lambda n: n % 2 == 1, range(1, 20)))
print(L)

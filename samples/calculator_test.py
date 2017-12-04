# _*_ coding: utf-8 _*_

"""
---------------------------------
@Time     : 2017/12/4 15:52
@Author   : yuxy
@File     : calculator_test.py
@Project  : PythonSyntax
----------------------------------
"""


# 相加
def add(x, y):
    return x + y


# 相减
def substract(x, y):
    return x - y


# 相乘
def multiply(x, y):
    return x * y


# 相除
def divide(x, y):
    return x / y


# 用户输入
print("选择运算：")
print("1、相加")
print("2、相减")
print("3、相乘")
print("4、相除")

choice = input("输入你的选择(1/2/3/4):")

num1 = int(input("输入第一个数字: "))
num2 = int(input("输入第二个数字: "))

if choice == "1":
    print("{0} + {1} = {2}".format(num1, num2, add(num1, num2)))
elif choice == "2":
    print("{0} + {1} = {2}".format(num1, num2, substract(num1, num2)))
elif choice == "3":
    print("{0} + {1} = {2}".format(num1, num2, multiply(num1, num2)))
elif choice == "4":
    print("{0} + {1} = {2}".format(num1, num2, divide(num1, num2)))
else:
    print("非法输入")

"""
必需参数
    必需参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样
关键字参数
    关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。
    使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。
默认参数
    调用函数时，如果没有传递参数，则会使用默认参数。
    默认参数必须放在最后面
不定长参数
"""


# 必需参数
def print_me(str, age):
    print(str, age)
    return


# 调用print_me函数
name = "gm"
age = 20
print_me(age, name)
print("*******************")


# 关键字参数
def print_info(name, age):
    print("名字: ", name)
    print("年龄: ", age)
    return


# 调用print_info函数
print_info(age=50, name="runoob")
print("*******************")


# 默认参数
def print_info(name, age=35):
    print("名字: ", name)
    print("年龄: ", age)
    return


# 调用print_info函数
name = "baodu"
print_info(name, age=50)
print("------------------------")
print_info(name="runoob")
print("*******************")


# 不定长参数
"""
def functionname([formal_args,] *var_args_tuple ):
   "函数_文档字符串"
   function_suite
   return [expression]
加了星号（*）的变量名会存放所有未命名的变量参数。如果在函数调用时没有指定参数，它就是一个空元组。我们也可以不向函数传递未命名的变量。   
"""


def print_info(arg1, *vartuple):
    print("输出: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return


print_info(10)
print_info(70, 60, 50)

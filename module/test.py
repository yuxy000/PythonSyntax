from module import support
from module import fibo
import sys

support.print_func("Runoob")

fibo.fib(1000)

print(fibo.fib2(100))
print(fibo.__name__)

# 把模块中的一个函数赋给一个本地的名称
fib = fibo.fib
fib(10)

"""
from…import 语句
Python的from语句让你从模块中导入一个指定的部分到当前命名空间中，语法如下：
from modname import name1[, name2[, ... nameN]]
例如，要导入模块 fibo 的 fib 函数，使用如下语句：
>>> from fibo import fib, fib2
>>> fib(500)
1 1 2 3 5 8 13 21 34 55 89 144 233 377
这个声明不会把整个fibo模块导入到当前的命名空间中，它只会将fibo里的fib函数引入进来。

From…import* 语句
把一个模块的所有内容全都导入到当前的命名空间也是可行的，只需使用如下声明：
from modname import *
这提供了一个简单的方法来导入一个模块中的所有项目。然而这种声明不该被过多地使用。
"""


"""
__name__属性
一个模块被另一个程序第一次引入时，其主程序将运行。如果我们想在模块被引入时，模块中的某一程序块不执行，我们可以用__name__属性来使该程序块仅在该模块自身运行时执行。
    #!/usr/bin/python3
    # Filename: using_name.py
    
    if __name__ == '__main__':
       print('程序自身在运行')
    else:
       print('我来自另一模块')
运行输出如下：
    $ python using_name.py
    程序自身在运行
    $ python
    >>> import using_name
    我来自另一模块
    >>>
说明： 每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，否则是被引入。
"""

"""
内置的函数 dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回:
"""
print(dir(fibo))
print(dir(sys))
# 如果没有给定参数，那么 dir() 函数会罗列出当前定义的所有名称
print(dir())

#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
---------------------------------
@Time     : 2017/12/6 10:34
@Author   : yuxy
@File     : str_test.py
@Project  : PythonSyntax
----------------------------------
"""

"""
Python3 字符串
Python 访问字符串中的值
"""
var1 = "Hello world"
var2 = "Runoob"
print("var1[0]", var1[0])
print("var2[1:5]", var2[1:5])

"""
Python字符串更新
"""
print("已更新字符串 : ", var1[:6] + 'Runoob')

"""
Python字符串运算符    
"""
print("--------------Python字符串运算符---------------------- ")
a = "Hello"
b = "Python"
print("a + b 的结果：", a + b)
print("a * 2 的结果：", a * 2)
print("a[1] 的结果：", a[1])
print("a[1:4] 的结果：", a[1:4])

if("H" in a):
    print("H在变量a中")
else:
    print("H不在变量a中")
if("M" not in a):
    print("M不在变量a中")
else:
    print("H在变量a中")

print(r'\n')
print(R'\n')

print("--------------Python字符串运算符---------------------- ")

print("我叫%s,今年%d岁." % ('小名', 10))


print("--------------Python三引号---------------------- ")
para_str = """
这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print(para_str)


"""
Python capitalize()将字符串的第一个字母变成大写,其他字母变小写。
"""
str = "this is String example from runoob....wow!!!"
print("str.capitalize():" + str.capitalize())

"""
center() 方法返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。
center()方法语法：
str.center(width[, fillchar])
参数
    width -- 字符串的总宽度。
    fillchar -- 填充字符。
返回值
    返回一个指定的宽度 width 居中的字符串，如果 width 小于字符串宽度直接返回字符串，否则使用 fillchar 去填充。
"""
str1 = "[www.runoob.com]"
print("str.center(40, '*') : " + str1.center(40, "*"))
print("str.center(10, '*') : " + str1.center(10, "*"))

"""
描述
    count() 方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。
语法
count()方法语法：
    str.count(sub, start= 0,end=len(string))
参数
    sub -- 搜索的子字符串
    start -- 字符串开始搜索的位置。默认为第一个字符,第一个字符索引值为0。
    end -- 字符串中结束搜索的位置。字符中第一个字符的索引为 0。默认为字符串的最后一个位置。
返回值
    该方法返回子字符串在字符串中出现的次数。
"""
str = "www.runoob.com"
sub = 'o'
print("str.count('o') : ", str.count(sub))

sub = 'run'
print("str.count('run', 0, 10) : ", str.count(sub, 0, 10))

"""
描述
    decode() 方法以指定的编码格式解码 bytes 对象。默认编码为 'utf-8'。
语法
decode()方法语法：
    bytes.decode(encoding="utf-8", errors="strict")
参数
    encoding -- 要使用的编码，如"UTF-8"。
    errors -- 设置不同错误的处理方案。默认为 'strict',意为编码错误引起一个UnicodeError。 其他可能得值有 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' 以及通过 codecs.register_error() 注册的任何值。
返回值
    该方法返回解码后的字符串。
"""
"""
描述
    encode() 方法以指定的编码格式编码字符串。errors参数可以指定不同的错误处理方案。
语法
encode()方法语法：
    str.encode(encoding='UTF-8',errors='strict')
参数
    encoding -- 要使用的编码，如: UTF-8。
    errors -- 设置不同错误的处理方案。默认为 'strict',意为编码错误引起一个UnicodeError。 其他可能得值有 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' 以及通过 codecs.register_error() 注册的任何值。
返回值
    该方法返回编码后的字符串，它是一个 bytes 对象。
"""
str1 = "菜鸟教程"
str_utf8 = str1.encode("UTF-8")
str_gbk = str1.encode("GBK")

print(str1)

print("utf-8编码：", str_utf8)
print("GBK编码：", str_gbk)

print("utf-8解码：", str_utf8.decode("UTF-8", 'strict'))
print("GBK解码：", str_gbk.decode("GBK", 'strict'))


"""
描述
    endswith() 方法用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回True，否则返回False。可选参数"start"与"end"为检索字符串的开始与结束位置。
语法
endswith()方法语法：
    str.endswith(suffix[, start[, end]])
参数
    suffix -- 该参数可以是一个字符串或者是一个元素。
    start -- 字符串中的开始位置。
    end -- 字符中结束位置。
返回值
    如果字符串含有指定的后缀返回True，否则返回False。
"""

"""
描述
    startswith() 方法用于检查字符串是否是以指定子字符串开头，如果是则返回 True，否则返回 False。如果参数 beg 和 end 指定值，则在指定范围内检查。
语法
startswith()方法语法：
    str.startswith(str, beg=0,end=len(string));
参数
    str -- 检测的字符串。
    strbeg -- 可选参数用于设置字符串检测的起始位置。
    strend -- 可选参数用于设置字符串检测的结束位置。
返回值
    如果检测到字符串则返回True，否则返回False。
"""

# 编码
print('\u4e2d\u6587')

# 以Unicode表示的str通过encode()方法可以编码为指定的bytes
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
# 要把bytes变为str，就需要用decode()方法
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))


# 格式化
print('Hello, %s' % 'world')
print('Hi, %s, you have %s' % ('Tom', 10000))
"""
%运算符就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。
如果只有一个%?，括号可以省略。
常见的占位符有：

占位符	替换内容
%d	    整数
%f	    浮点数
%s	    字符串
%x	    十六进制整数
其中，格式化整数和浮点数还可以指定是否补0和整数与小数的位数：
"""
print('%03d-%03d' % (3000, 1))   # d前面的数字表示格式化后的长度 不够用0补
print('%.2f' % 3.1415926)

# 如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串
print('Age: %s. Gender: %s' % (25, True))

# 有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%
print('growth rate: %d%%' % 7)

print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))
s1 = 72
s2 = 85
r = (85 - 72) / 72
print('Hello, {0}, 成绩提升了{1:.1f}'.format('小名', r * 100))


def trim(s):
    if len(s) == 0:
        return s
    elif s[0] == " ":
        return trim(s[1:])
    elif s[len(s) - 1] == " ":
        return trim(s[:-1])
    else:
        return s


# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')

# 字符串从后往前遍历
st1 = "****H饿咯额   "
for b in st1[::-1]:
    print(b)


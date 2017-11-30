import math
import random

# 注释
'''
多行注释
多行注释
'''
"""
多号注释
多行注释
"""
print("Hello Python!")
print(5 + 6)
# 取整除
print(9//2)
# 幂
print(10**2)

print(1 > 10)

a = 10
b = 20
if not (a < b):
    print(b)

listArray = [1, 2, 3, 4, 5]
print(a in listArray)
print(a not in listArray)

print("is, is not")
print(a is b)
print(a is not b)
print(id(a) == id(b))

c = 123
d = 10
print(complex(c, d))

print(17 / 3)
print(17 // 3)

print(math.modf(12.3))

print("从 range(100) 返回一个随机数 : ", random.choice(range(100)))
print("从列表中 [1, 2, 3, 5, 9]) 返回一个随机元素 : ", random.choice([1, 2, 3, 5, 9]))
print("从字符串中 'Runoob' 返回一个随机字符 : ", random.choice('Runoob'))


"""
randrange() 方法返回指定递增基数集合中的一个随机数，基数缺省值为1。
random.randrange ([start,] stop [,step])
start -- 指定范围内的开始值，包含在范围内。
stop -- 指定范围内的结束值，不包含在范围内。
step -- 指定递增基数。
"""
# 从1-100中选择一个奇数
print("random.randrange(1, 100, 2):", random.randrange(1, 100, 2))
# 从 0-99 选取一个随机数
print("randrange(100) : ", random.randrange(100))

# random() 方法返回随机生成的一个实数，它在[0,1)范围内。
# 第一个随机数
print("random():", random.random())
# 第二个随机数
print("random():", random.random())

#shuffle() 方法将序列的所有元素随机排序。
listArray = [20, 16, 10, 5]
random.shuffle(listArray)
random.shuffle(listArray)
print("随机排序列表 : ", listArray)

random.shuffle(listArray)
print("随机排序列表 : ", listArray)

"""
uniform() 方法将随机生成下一个实数，它在[x,y]范围内。

"""
print("uniform(5, 10) 的随机浮点数 : ",  random.uniform(5, 10))
print("uniform(7, 14) 的随机浮点数 : ",  random.uniform(7, 14))

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

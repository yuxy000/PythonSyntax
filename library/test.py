# 操作系统接口
import os
import glob
import sys
from urllib.request import urlopen
import smtplib
import datetime
import time
from datetime import date
import zlib
from timeit import Timer
import doctest
import unittest


# 返回当前的工作目录
print(os.getcwd())

# 修改当前的工作目录
# os.chdir('../tmp')

# 执行系统命令 mkdir
# os.system('mkdir today')

# print(dir(os))
# print(help(os))


# 针对日常的文件和目录管理任务，:mod:shutil 模块提供了一个易于使用的高级接口:
"""
>>> import shutil
>>> shutil.copyfile('data.db', 'archive.db')
>>> shutil.move('/build/executables', 'installdir')
"""

# 文件通配符
# glob模块提供了一个函数用于从目录通配符搜索中生成文件列表:

print(glob.glob('*.py'))


"""
命令行参数
通用工具脚本经常调用命令行参数。这些命令行参数以链表形式存储于 sys 模块的 argv 变量。例如在命令行中执行 "python demo.py one two three" 后可以得到以下输出结果:
>>> import sys
>>> print(sys.argv)
['demo.py', 'one', 'two', 'three']
"""

# 错误输出重定向和程序终止
# sys.stderr.write('Warning, log file not found starting a new one\n')
# 大多脚本的定向终止都使用 "sys.exit()"。


# 字符串正则匹配
"""
re模块为高级字符串处理提供了正则表达式工具。对于复杂的匹配和处理，正则表达式提供了简洁、优化的解决方案:
>>> import re
>>> re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
['foot', 'fell', 'fastest']
>>> re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
'cat in the hat'
如果只需要简单的功能，应该首先考虑字符串方法，因为它们非常简单，易于阅读和调试:
>>> 'tea for too'.replace('too', 'two')
'tea for two'
"""

# 数学
"""
math模块为浮点运算提供了对底层C函数库的访问:
>>> import math
>>> math.cos(math.pi / 4)
0.70710678118654757
>>> math.log(1024, 2)
10.0
random提供了生成随机数的工具。
>>> import random
>>> random.choice(['apple', 'pear', 'banana'])
'apple'
>>> random.sample(range(100), 10)   # sampling without replacement
[30, 83, 16, 4, 8, 81, 41, 50, 18, 33]
>>> random.random()    # random float
0.17970987693706186
>>> random.randrange(6)    # random integer chosen from range(6)
4
"""

# 访问 互联网
"""
用于处理从 urls 接收的数据的 urllib.request
用于发送电子邮件的 smtplib
"""
# urllib.request
# for line in urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
#     line = line.decode('urf-8')     # Decoding the binary data to text.
#     if 'EST' in line or 'EDT' in line:
#         print(line)

# smtplib
# >>> import smtplib
# >>> server = smtplib.SMTP('localhost')
# >>> server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
# ... """To: jcaesar@example.org
# ... From: soothsayer@example.org
# ...
# ... Beware the Ides of March.
# ... """)
# >>> server.quit()

# 日期和时间
"""
datetime模块为日期和时间处理同时提供了简单和复杂的方法。
支持日期和时间算法的同时，实现的重点放在更有效的处理和格式化输出。
该模块还支持时区处理
python中时间日期格式化符号：
    %y 两位数的年份表示（00-99）
    %Y 四位数的年份表示（000-9999）
    %m 月份（01-12）
    %d 月内中的一天（0-31）
    %H 24小时制小时数（0-23）
    %I 12小时制小时数（01-12） 
    %M 分钟数（00=59）
    %S 秒（00-59）
    
    %a 本地简化星期名称
    %A 本地完整星期名称
    %b 本地简化的月份名称
    %B 本地完整的月份名称
    %c 本地相应的日期表示和时间表示
    %j 年内的一天（001-366）
    %p 本地A.M.或P.M.的等价符
    %U 一年中的星期数（00-53）星期天为星期的开始
    %w 星期（0-6），星期天为星期的开始
    %W 一年中的星期数（00-53）星期一为星期的开始
    %x 本地相应的日期表示
    %X 本地相应的时间表示
    %Z 当前时区的名称
    %% %号本身 
"""
# from datetime import date
now = date.today()
print(now)

datetime.date(2003, 12, 2)
print(now.strftime("%m-%d-%y. %d %b %Y is %A on the %d day of %B"))

# dates support calendar arithmetic
birthday = date(2016, 6, 16)
age = now - birthday
print(age.days)
# 打印当前时间
print(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))


# 数据压缩 直接支持通用的数据打包和压缩格式：zlib，gzip，bz2，zipfile，以及 tarfile。
s = b'witch which has which witches wrist watch'
print(len(s))
t = zlib.compress(s)     # 压缩
print(len(t))
print(zlib.decompress(t))    # 解压
print(zlib.crc32(s))     # 校验


# 性能度量 from timeit import Timer
print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
# ----0.04684487601221264
print(Timer('a,b = b,a', 'a=1; b=2').timeit())
# ----0.025131579479354862

# 测试模块
"""
开发高质量软件的方法之一是为每一个函数开发测试代码，并且在开发过程中经常进行测试
doctest模块提供了一个工具，扫描模块并根据程序中内嵌的文档字符串执行测试。
测试构造如同简单的将它的输出结果剪切并粘贴到文档字符串中。
通过用户提供的例子，它强化了文档，允许 doctest 模块确认代码的结果是否与文档一致
"""


def average(values):
    """Computes the arithmetic mean of a list of numbers.

    print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)


# doctest.testmod()

# unittest模块不像 doctest模块那么容易使用，不过它可以在一个独立的文件里提供一个更全面的测试集:


class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        self.assertRaises(ZeroDivisionError, average, [])
        self.assertRaises(TypeError, average, 20, 30, 70)


unittest.main()     # Calling from the command line invokes all tests

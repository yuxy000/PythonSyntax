#!usr/bin/python3

import time
import calendar

import os

ticks = time.time()
print("当前的时间戳：", ticks)

"""
序号	    字段	        值
0	        4位数年	        2008
1	        月	            1 到 12
2	        日	            1到31
3	        小时	        0到23
4	        分钟	        0到59
5	        秒	            0到61 (60或61 是闰秒)
6	        一周的第几日	0到6 (0是周一)
7	        一年的第几日	1到366 (儒略历)
8	        夏令时	        -1, 0, 1, -1是决定是否为夏令时的旗帜
上述也就是struct_time元组。这种结构具有如下属性：
序号	        属性	        值
0	            tm_year	        2008
1	            tm_mon	        1 到 12
2	            tm_mday	        1 到 31
3	            tm_hour	        0 到 23
4	            tm_min	        0 到 59
5	            tm_sec	        0 到 61 (60或61 是闰秒)
6	            tm_wday	        0到6 (0是周一)
7	            tm_yday	        一年中的第几天，1 到 366
8	            tm_isdst	    是否为夏令时，值有：1(夏令时)、0(不是夏令时)、-1(未知)，默认 -1
"""

# 获取当前时间
localtime = time.localtime(time.time())
print("本地时间为：", localtime)
print(str(localtime[0]) + "-" + str(localtime[1]) + "-" + str(localtime[2]) + " " + str(localtime[3]) + ":" + str(localtime[4]) + ":" + str(localtime[5]))


# 格式化日期

# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
a = "Mon Dec 04 10:09:40 2017"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))
b = "2017-12-04 10:09:40"
print(time.mktime(time.strptime(b, "%Y-%m-%d %H:%M:%S")))


"""
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

# 获取某月日历
cal = calendar.month(2017, 12)
print("以下输出2017年12月份的日历:")
print(cal)

# Time 模块
"""
time.altzone
返回格林威治西部的夏令时地区的偏移秒数。如果该地区在格林威治东部会返回负值（如西欧，包括英国）。对夏令时启用地区才能使用。
"""
print("time.altzone %d " % time.altzone)

"""
ime.asctime([tupletime])
接受时间元组并返回一个可读的形式为"Tue Dec 11 18:07:14 2008"（2008年12月11日 周二18时07分14秒）的24个字符的字符串。
"""
t = time.localtime()
print("time.asctime(t): %s " % time.asctime(t))

"""
time.clock()
用以浮点数计算的秒数返回当前的CPU时间。用来衡量不同程序的耗时，比time.time()更有用。
"""


# def procedure():
#     time.sleep(2.5)
#
#
# # time.clock
# t0 = time.clock()
# procedure()
# print(time.clock() - t0)
#
# # time.time
# t0 = time.time()
# procedure()
# print(time.time() - t0)

"""
time.ctime([secs])
作用相当于asctime(localtime(secs))，未给参数相当于asctime()
"""
print("time.ctime() : %s" % time.ctime())

"""
time.gmtime([secs])
接收时间辍（1970纪元后经过的浮点秒数）并返回格林威治天文时间下的时间元组t。注：t.tm_isdst始终为0
"""
print("time.gmtime:", time.gmtime(1455508609.34375))

"""
time.localtime([secs]
接收时间辍（1970纪元后经过的浮点秒数）并返回当地时间下的时间元组t（t.tm_isdst可取0或1，取决于当地当时是不是夏令时）。
"""
print("localtime(): ", time.localtime(1455508609.34375))

"""
time.mktime(tupletime)
接受时间元组并返回时间辍（1970纪元后经过的浮点秒数）。
"""
t = (2016, 2, 17, 17, 3, 38, 1, 48, 0)
secs = time.mktime(t)
print("time.mktime(t) : %f" % secs)
print("asctime(localtime(secs)): %s" % time.asctime(time.localtime(secs)))

"""
time.sleep(secs)
推迟调用线程的运行，secs指秒数。
"""
# print("Start : %s" % time.ctime())
# time.sleep(5)
# print("End : %s" % time.ctime())

"""
time.strftime(fmt[,tupletime])
接收以时间元组，并返回以可读字符串表示的当地时间，格式由fmt决定。
"""
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

"""
time.strptime(str,fmt='%a %b %d %H:%M:%S %Y')
根据fmt的格式把一个时间字符串解析为时间元组。
"""
struct_time = time.strptime("30 Nov 00", "%d %b %y")
print("返回元组: ", struct_time)

"""
time.time( )
返回当前时间的时间戳（1970纪元后经过的浮点秒数）。
"""
print(time.time())

"""
time.tzset()
根据环境变量TZ重新初始化时间相关设置。
AttributeError: module 'time' has no attribute 'tzset'
"""
# os.environ['TZ'] = 'EST+05EDT,M4.1.0,M10.5.0'
# time.tzset()
# print(time.strftime('%X %x %Z'))
#
# os.environ['TZ'] = 'AEST-10AEDT-11,M10.5.0,M3.5.0'
# time.tzset()
# print(time.strftime('%X %x %Z'))


# 日历（Calendar）模块

"""
此模块的函数都是日历相关的，例如打印某月的字符月历。
星期一是默认的每周第一天，星期天是默认的最后一天。更改设置需调用calendar.setfirstweekday()函数。模块包含了以下内置函数：
序号	函数及描述

1	calendar.calendar(year,w=2,l=1,c=6)
    返回一个多行字符串格式的year年年历，3个月一行，间隔距离为c。 每日宽度间隔为w字符。每行长度为21* W+18+2* C。l是每星期行数。
2	calendar.firstweekday( )
    返回当前每周起始日期的设置。默认情况下，首次载入caendar模块时返回0，即星期一。
3	calendar.isleap(year)
    是闰年返回True，否则为false。
4	calendar.leapdays(y1,y2)
    返回在Y1，Y2两年之间的闰年总数。
5	calendar.month(year,month,w=2,l=1)
    返回一个多行字符串格式的year年month月日历，两行标题，一周一行。每日宽度间隔为w字符。每行的长度为7* w+6。l是每星期的行数。
6	calendar.monthcalendar(year,month)
    返回一个整数的单层嵌套列表。每个子列表装载代表一个星期的整数。Year年month月外的日期都设为0;范围内的日子都由该月第几日表示，从1开始。
7	calendar.monthrange(year,month)
    返回两个整数。第一个是该月的星期几的日期码，第二个是该月的日期码。日从0（星期一）到6（星期日）;月从1到12。
8	calendar.prcal(year,w=2,l=1,c=6)
    相当于 print calendar.calendar(year,w,l,c).
9	calendar.prmonth(year,month,w=2,l=1)
    相当于 print calendar.calendar（year，w，l，c）。
10	calendar.setfirstweekday(weekday)
    设置每周的起始日期码。0（星期一）到6（星期日）。
11	calendar.timegm(tupletime)
    和time.gmtime相反：接受一个时间元组形式，返回该时刻的时间辍（1970纪元后经过的浮点秒数）。
12	calendar.weekday(year,month,day)
    返回给定日期的日期码。0（星期一）到6（星期日）。月份为 1（一月） 到 12（12月）。
"""
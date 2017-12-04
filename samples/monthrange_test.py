# _*_ coding:UTF-8 _*_

import calendar

monthRange = calendar.monthrange(2017, 2)
print(monthRange)
# (3, 30)
# 输出的是一个元组，第一个元素是所查月份的第一天对应的是星期几（0-6），第二个元素是这个月的天数。
# 以上实例输出的意思为 2017 年 1 月份的第一天是星期三，该月总共有 28 天。

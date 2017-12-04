# _*_ coding:UTF-8 _*_

# 引入 datetime 模块
import datetime


def get_yesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=2)  # 实现日期相加
    yesterday = today - oneday
    return yesterday


print(get_yesterday())

#!/usr/bin/python3
"""
json.dumps(): 对数据进行编码。把python对象转成json字符串
"""

import json

# Python 字典类型转换为 JSON 对象
data1 = {
    'no': 1,
    'name': 'Runoob',
    'url': 'http://www.runoob.com'
}

json_str = json.dumps(data1)
print("Python 原始数据：", repr(data1))
print("JSON 对象：", json_str)
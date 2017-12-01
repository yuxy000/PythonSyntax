"""
JSON (JavaScript Object Notation) 是一种轻量级的数据交换格式。它基于ECMAScript的一个子集。
Python3 中可以使用 json 模块来对 JSON 数据进行编解码，它包含了两个函数：
    json.dumps(): 对数据进行编码。
    json.loads(): 对数据进行解码。
在json的编解码过程中，python 的原始类型与json类型会相互转换，具体的转化对照如下：
Python 编码为 JSON 类型转换对应表：
Python	        JSON
dict	        object
list,           tuple	array
str	            string
int,            float, int- & float-derived Enums	number
True	        true
False	        false
None	        null
JSON 解码为 Python 类型转换对应表：
JSON	        Python
object	        dict
array	        list
string	        str
number (int)	int
number (real)	float
true	        True
false	        False
null	        None
"""
import json

data = {
    'no': 1,
    'name': 'Runoob',
    'url': 'http://www.runoob.com'
}
# 如果你要处理的是文件而不是字符串，你可以使用 json.dump() 和 json.load() 来编码和解码JSON数据。
# 写入 JSON 数据
with open("../tmp/data.json", 'w') as f:
    json.dump(data, f)

# 读取数据
with open('../tmp/data.json', 'r') as f:
    data1 = json.load(f)
    print(type(data1))


# _*_ coding: UTF-8 _*_

li = ["a", "b", "mpilgrim", "z", "example"]
print(li)

# list 负数索引
print("li[-1]:", li[-1])
print("li[-3]:", li[-3])
print("li[1:3]", li[1:3])
print("li[1, -1]:", li[1:-1])
print("li[0:3]", li[0:3])

# list 增加元素
li.append("new")    # 尾部增加
print(li)
li.insert(2, "new2")    # 指定位置添加
print(li)

li.extend(["two", "elements"])  # 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
print(li)

# list 搜索
print(li.index("example"))
print(li.index("new"))
# print(li.index("c"))    # 报异常 ValueError: 'c' is not in list

# list 删除元素
li = ['a', 'b', 'new', 'mpilgrim', 'z', 'example', 'new', 'two', 'elements']
li.remove("z")
print(li)
li.remove("new")    # 删除首次出现的一个值
print(li)   # 第二个 'new' 未删除
# li.remove("c")     # list 中没有找到值, Python 会引发一个异常

print(li.pop())     # pop 删除 list 的最后一个元素, 然后返回删除元素的值。
print(li)

# list 运算符
li = ['a', 'b', 'mpilgrim']
li = li + ['example', 'new']
print(li)
li += ["two"]
print(li)
li = [1, 2] * 3
print(li)

# 使用join链接list成为字符串
params = {"server": "mpilgrim", "database": "master", "uid": "sa", "pwd": "secret"}
print(["%s=%s" % (k, v) for k, v in params.items()])
print(";".join(["%s=%s" % (k, v) for k, v in params.items()]))
"""
oin 只能用于元素是字符串的 list; 它不进行任何的类型强制转换。连接一个存在一个或多个非字符串元素的 list 将引发一个异常。
"""

# list 分割字符串
li = ['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
s = ";".join(li)
print(s)
print(s.split(";"))
print(s.split(";", 1))
"""
split 与 join 正好相反, 它将一个字符串分割成多元素 list。
注意, 分隔符 (";") 被完全去掉了, 它没有在返回的 list 中的任意元素中出现。
split 接受一个可选的第二个参数, 它是要分割的次数。
"""

# list 的映射解析
li = [1, 9, 8, 4]
print([elem * 2 for elem in li])
li = [elem*2 for elem in li]
print(li)

# dictionary中的解析
params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
print(params.keys())
print(params.values())
print(params.items())
print([k for k, v in params.items()])
print([v for k, v in params.items()])
print(["%s=%s" % (k, v) for k, v in params.items()])

# list 过滤
li = ["a", "mpilgrim", "foo", "b", "c", "b", "d", "d"]
print([elem for elem in li if len(elem) > 1])
print([elem for elem in li if elem != "b"])
print([elem for elem in li if li.count(elem) == 1])     # count() 统计某个元素在列表中出现的次数


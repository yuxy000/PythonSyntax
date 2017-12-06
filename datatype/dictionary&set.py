"""
字典是另一种可变容器模型，且可存储任意类型对象。
字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中 ,格式如下所示：
d = {key1 : value1, key2 : value2 }
键必须是唯一的，但值则不必。
值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。
"""

# 访问字典里的值
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print("dict['Name']:", dict['Name'])
print("dict['Age']:", dict['Age'])
# dict.get(key, default) 如果key不存在，可以返回None，或者自己指定的value：
print("dict.get('Name1')", dict.get("Name1", "未知"))

# 修改字典
dict1 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
dict1['Age'] = 8   # 更新
dict1['School'] = "菜鸟教程"    # 添加
print("dict1['Age']: ", dict1['Age'])
print("dict1['School']: ", dict1['School'])

# 删除字典元素
dict2 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
del dict2['Name']   # 删除键 'Name'
# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除
print(dict2.pop("Age"))
print(dict2)
dict2.clear()   # 删除字典
del dict2   # 删除字典

"""
字典键的特性
字典值可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行。
两个重要的点需要记住：
    1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
    2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行
"""

# 字典内置函数:
dict3 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# 计算字典元素个数，即键的总数。
print("len(dict3):", len(dict3))
# 输出字典，以可打印的字符串表示。
print("str(dict3):", str(dict3))
# 返回输入的变量类型，如果变量是字典就返回字典类型。
print("type(dict3):", type(dict3))

# Python字典包含了以下内置方法：
"""
1	radiansdict.clear()
    删除字典内所有元素
2	radiansdict.copy()
    返回一个字典的浅复制
3	radiansdict.fromkeys()
    创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
4	radiansdict.get(key, default=None)
    返回指定键的值，如果值不在字典中返回default值
5	key in dict
    如果键在字典dict里返回true，否则返回false
6	radiansdict.items()
    以列表返回可遍历的(键, 值) 元组数组
7	radiansdict.keys()
    以列表返回一个字典所有的键
8	radiansdict.setdefault(key, default=None)
    和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
9	radiansdict.update(dict2)
    把字典dict2的键/值对更新到dict里
10	radiansdict.values()
    以列表返回字典中的所有值
11	pop(key[,default])
    删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
12	popitem()
    随机返回并删除字典中的一对键和值(一般删除末尾对)。
"""

# set
"""
set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
set 无序和无重复元素的集合
要创建一个set，需要提供一个list作为输入集合
"""
# 重复元素在set中自动被过滤
s = set([1, 2, 3, 1, 2, 3])
print(s)
# 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
s.add(4)
print(s)
# 通过remove(key)方法可以删除元素
s.remove(2)
print(s)

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
# 交集
print(s1 & s2)
# 并集
print(s1 | s2)

"""
set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，
所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。
"""

s3 = set([1, 2, [3, 4]])
print(s3)
list1 = ['Google', 'Runoob', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]
print("list1[0]:", list1[0])
print("list2[1:5]:", list2[1:5])
# 更新元素
print("第三个元素为 : ", list1[2])
list1[2] = 1998
print("更新后的第三个元素是：", list1[2])

# 删除元素
del list1[2]
print("删除第三个元素：", list1)

# list操作符
print("len([1, 2, 3]) = ", len([1, 2, 3]))
print("[1, 2, 4] + [5, 6] = ", [1, 2, 4] + [5, 6])
print("[\"Hi\"] * 4 = ", ["Hi"] * 4)
print("3 in [1, 2, 3] = ", 3 in [1, 2, 3])
for x in [1, 2, 3]:
    print("x = ", x)

# Python列表截取与拼接
L = ['Google', 'Runoob', 'Taobao']
print("L:", L)
print("L[2]:", L[2])
print("L[-2]:", L[-2])
print("L[1:]:", L[1:])

# 嵌套列表
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print("x = ", x)
print("x[0]:", x[0])
print("x[0][1]:", x[0][1])

# 将元组转换为列表
aTuple = (123, 'Google', 'Runoob', 'Taobao')
list_seq = list(aTuple)
print("list_seq:", list_seq)
str1 = "Hello World"
list_seq_2 = list(str1)
print("列表元素list_seq_2 : ", list_seq_2)
"""
list.append(obj)
    在列表末尾添加新的对象
2	list.count(obj)
    统计某个元素在列表中出现的次数
3	list.extend(seq)
    在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
4	list.index(obj)
    从列表中找出某个值第一个匹配项的索引位置
5	list.insert(index, obj)
    将对象插入列表
6	list.pop(obj=list[-1])
    移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
7	list.remove(obj)
    移除列表中某个值的第一个匹配项
8	list.reverse()
    反向列表中元素
9	list.sort([func])
    对原列表进行排序
10	list.clear()
    清空列表
11	list.copy()
    复制列表
"""


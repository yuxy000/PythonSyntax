tup1 = ()
# 元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用
tup1 = (50)
print(type(tup1))
tup1 = (50,)
print(type(tup1))

# 访问元组
tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7)
print("tup1[0]", tup1[0])
print("tup2[1:5]", tup2[1:5])
print("tup1[::2]", tup1[::2])

"""
修改元组
元组中的元素值是不允许修改的，但我们可以对元组进行连接组合
"""
tup1 = (12, 34.56);
tup2 = ('abc', 'xyz')

# 以下修改元组元素操作是非法的。
# tup1[0] = 100

tup3 = tup1 + tup2
print(tup3)

"""
删除元组
元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
"""
tup = ('Google', 'Runoob', 1997, 2000)

print(tup)
del tup
print("删除后的元组 tup: ")
# print(tup)

# 元组运算符
print("len((1, 2, 3)) = ", len((1, 2, 3)))
print("(1, 2, 4) + [5, 6) = ", (1, 2, 4) + (5, 6))
print("(\"Hi\",) * 4 = ", ("Hi",) * 4)
print("3 in (1, 2, 3) = ", 3 in (1, 2, 3))
for x in (1, 2, 3):
    print("x = ", x)

# 元组索引，截取
L = ('Google', 'Runoob', 'Taobao')
print("L:", L)
print("L[2]:", L[2])
print("L[-2]:", L[-2])
print("L[1:]:", L[1:])

"""
len(tuple)
    计算元组元素个数。
max(tuple)
    返回元组中元素最大值。
min(tuple)
    返回元组中元素最小值。
tuple(seq)
    将列表转换为元组。
"""
list1 = ['Google', 'Taobao', 'Runoob', 'Baidu']
tup1 = tuple(list1)
print(tup1)

import math
import random

# 注释
'''
多行注释
多行注释
'''
"""
多号注释
多行注释
"""
print("Hello Python!")
print(5 + 6)
# 取整除
print(9//2)
# 幂
print(10**2)

print(1 > 10)

a = 10
b = 20
if not (a < b):
    print(b)

listArray = [1, 2, 3, 4, 5]
print(a in listArray)
print(a not in listArray)

print("is, is not")
print(a is b)
print(a is not b)
print(id(a) == id(b))

c = 123
d = 10
print(complex(c, d))

print(17 / 3)
print(17 // 3)

print(math.modf(12.3))

print("从 range(100) 返回一个随机数 : ", random.choice(range(100)))
print("从列表中 [1, 2, 3, 5, 9]) 返回一个随机元素 : ", random.choice([1, 2, 3, 5, 9]))
print("从字符串中 'Runoob' 返回一个随机字符 : ", random.choice('Runoob'))


"""
randrange() 方法返回指定递增基数集合中的一个随机数，基数缺省值为1。
random.randrange ([start,] stop [,step])
start -- 指定范围内的开始值，包含在范围内。
stop -- 指定范围内的结束值，不包含在范围内。
step -- 指定递增基数。
"""
# 从1-100中选择一个奇数
print("random.randrange(1, 100, 2):", random.randrange(1, 100, 2))
# 从 0-99 选取一个随机数
print("randrange(100) : ", random.randrange(100))

# random() 方法返回随机生成的一个实数，它在[0,1)范围内。
# 第一个随机数
print("random():", random.random())
# 第二个随机数
print("random():", random.random())

#shuffle() 方法将序列的所有元素随机排序。
listArray = [20, 16, 10, 5]
random.shuffle(listArray)
random.shuffle(listArray)
print("随机排序列表 : ", listArray)

random.shuffle(listArray)
print("随机排序列表 : ", listArray)

"""
uniform() 方法将随机生成下一个实数，它在[x,y]范围内。

"""
print("uniform(5, 10) 的随机浮点数 : ",  random.uniform(5, 10))
print("uniform(7, 14) 的随机浮点数 : ",  random.uniform(7, 14))


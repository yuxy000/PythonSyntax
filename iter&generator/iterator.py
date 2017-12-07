import sys
from collections import Iterable
from collections import Iterator

"""
迭代是Python最强大的功能之一，是访问集合元素的一种方式。。
迭代器是一个可以记住遍历的位置的对象。
迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
迭代器有两个基本的方法：iter() 和 next()。
"""

# 判断一个对象是否可迭代对象
print("******************************")
print(isinstance('ABC', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))

# 判断一个对象是否是Iterator对象
print("判断一个对象是否是Iterator对象")
g = (x for x in range(10))
print(isinstance(g, Iterator))
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))
print("".center(30, "*"))

# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数：
print(isinstance(iter([]), Iterator))
print(isinstance(iter('abc'), Iterator))


list1 = [1, 2, 3, 4]
it = iter(list1)
print(next(it))     # 创建迭代器对象
print(next(it))     # 输出迭代器的下一个元素

for x in it:
    print(x, end=" ")
print("")

# while next()
list2 = [1, 2, 3, 4]
it2 = iter(list2)    # 创建迭代器对象
while True:
    try:
        print(next(it2))
    except StopIteration:
        sys.exit()


"""
凡是可作用于for循环的对象都是Iterable类型
凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
Python的for循环本质上就是通过不断调用next()函数实现的，例如：

for x in [1, 2, 3, 4, 5]:
    pass
实际上完全等价于：
# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
"""

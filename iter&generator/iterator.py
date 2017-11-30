import sys

"""
迭代是Python最强大的功能之一，是访问集合元素的一种方式。。
迭代器是一个可以记住遍历的位置的对象。
迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
迭代器有两个基本的方法：iter() 和 next()。
"""
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

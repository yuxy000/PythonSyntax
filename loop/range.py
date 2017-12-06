"""
如果你需要遍历数字序列，可以使用内置range()函数。它会生成数列
"""
for i in range(5):
    print(i)
print("********************")

# 使用range指定区间的值
for i in range(6, 9):
    print(i)
print("********************")

# 使range以指定数字开始并指定不同的增量
for i in range(0, 10, 3):
    print(i)
print("********************")

# 负数
for i in range(-10, -100, -30):
    print(i)
print("********************")

# 结合range()和len()函数以遍历一个序列的索引
a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i, a[i])
print("********************")

# 使用range()函数来创建一个列表
list1 = list(range(5))
print(list1)

# 循环语句可以有 else 子句，它在穷尽列表(以for循环)或条件变为 false (以while循环)导致循环终止时被执行,但循环被break终止时不执行。
# break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行。
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')

# 使用内置 enumerate 函数进行遍历
print("使用内置 enumerate 函数进行遍历:")
sequence = [12, 34, 34, 23, 45, 76, 89]
for i, j in enumerate(sequence):
    print(i, j)

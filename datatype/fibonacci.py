# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a + b

# 关键字end可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符
a, b = 0, 1
while b < 1000:
    print(b, end=" ")
    a, b = b, a + b

print()


# c使用递归方式求斐波纳契数列
def fab(n):
    if n < 1:
        print("输入结果有误！")
        return -1
    if n == 1 or n == 2:
        return 1
    else:
        return fab(n - 1) + fab(n - 2)


print(fab(5))

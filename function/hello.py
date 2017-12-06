"""
定义一个函数的规则：
    函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
    任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
    函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
    函数内容以冒号起始，并且缩进。
    return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。
"""


def hello():
    print("Hello World")


# 调用函数
hello()


# 计算面积
def area(width, height):
    return width * height


def print_welcome(name):
    print("Welcome", name)


print_welcome("Runoob")
w = 5
h = 4
print("width =", w, " height =", h, " area =", area(w, h))


# 传不可变对象实例
def change_int(a):
    a = 10
    print("a = ", a)


b = 2
change_int(b)
print("b = ", b)
"""
实例中有 int 对象 2，指向它的变量是 b，在传递给 ChangeInt 函数时，按传值的方式复制了变量 b，a 和 b 都指向了同一个 Int 对象，在 a=10 时，则新生成一个 int 值对象 10，并让 a 指向它。
"""


# 传可变对象实例
def change_me(mylist):
    mylist.append([1, 2, 3, 4])
    print("函数内取值: ", mylist)
    return


mylist = [10, 20, 30]
change_me(mylist)
print("函数外取值: ", mylist)


# 汉诺塔
def move(disk, n, m):
    print("把 %d 号圆盘从 %s 移动到 %s" % (0, disk, n, m))


def hanoi(n, a, b, c):
    if n == 1:
        print("把 %d 号圆盘从 %s 移动到 %s" % (n, a, c))
    else:
        hanoi(n - 1, a, c, b)   # 递归，把A塔上编号1~n-1的圆盘移到B上，以C为辅助塔
        print("把 %d 号圆盘从 %s 移动到 %s" % (n, a, c))       # 把A塔上编号为n的圆盘移到C上
        hanoi(n - 1, b, a, c)   # 递归，把B塔上编号1~n-1的圆盘移到C上，以A为辅助塔


hanoi(5, 'A', 'B', 'C')

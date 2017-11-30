class MyClass:
    """一个简单的类实例"""
    i = 125

    # 构造方法
    def __init__(self, realpart, imagpart):
        self.data = []
        self.r = realpart
        self.ip = imagpart

    def f(self):
        return 'hello world'

# 实例化类
x = MyClass(3.0, -4.5)

# 访问类的属性和方法
print("MyClass 类的属性 i 为：", x.i)
print("MyClass 类的方法 f 输出为：", x.f())
print(x.r, x.i)


# self代表类的实例，而非类
# self 不是 python 关键字，我们把他换成 sf 也是可以正常执行的:
class Test:
    def prt(sf):
        print(sf)
        print(sf.__class__)


t = Test()
t.prt()

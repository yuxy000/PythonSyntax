"""
读和写文件
open() 将会返回一个 file 对象，基本语法格式如下:
open(filename, mode)
filename：filename 变量是一个包含了你要访问的文件名称的字符串值。
mode：mode决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。
不同模式打开文件的完全列表：
模式	描述
r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
r+	打开一个文件用于读写。文件指针将会放在文件的开头。
rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
w	打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
w+	打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
"""

# 文件对象的方法
"""
f.read()
为了读取一个文件的内容，调用 f.read(size), 这将读取一定数目的数据, 然后作为字符串或字节对象返回。
size 是一个可选的数字类型的参数。 当 size 被忽略了或者为负, 那么该文件的所有内容都将被读取并且返回。
"""
# 打开一个文件
f = open('./tmp/foo.txt', "r")
str3 = f.read()
print(str3)
# 关闭打开的文件
f.close()

"""
f.readline() 会从文件中读取单独的一行。换行符为 '\n'。f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行。
"""
f = open('./tmp/foo.txt', "r")
str2 = f.readline()
print(str2)
# 关闭打开的文件
f.close()

"""
f.readlines() 将返回该文件中包含的所有行。
如果设置可选参数 sizehint, 则读取指定长度的字节, 并且将这些字节按行分割。
"""
f = open('./tmp/foo.txt', "r")
str1 = f.readlines()
print(str1)
# 关闭打开的文件
f.close()

# 迭代一个文件对象然后读取每行
f = open('./tmp/foo.txt', "r")
for line in f:
    print(line, end=" ")
# 关闭打开的文件
f.close()
print("")

# f.write() 将 string 写入到文件中, 然后返回写入的字符数。
# 打开一个文件
f = open("./tmp/foo_1.txt", "w", encoding="utf8")
str4 = "Python 是一个非常好的语言。\n是的，的确非常好!!\n".encode("UTF-8").decode("UTF-8", 'strict')
num = f.write(str4)
print(num)
# 关闭打开的文件
f.close()

# 如果要写入一些不是字符串的东西, 那么将需要先进行转换
# 打开一个文件
f = open("./tmp/foo1.txt", "w")
value = ('www.runoob.com', 14)
s = str(value)
f.write(s)
print(f.tell())
# 关闭打开的文件
f.close()

# f.tell() 返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数。

"""
f.seek()
如果要改变文件当前的位置, 可以使用 f.seek(offset, from_what) 函数。
from_what 的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾，例如：
    seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符
    seek(x,1) ： 表示从当前位置往后移动x个字符
    seek(-x,2)：表示从文件的结尾往前移动x个字符
"""
f = open('./tmp/foo1.txt', 'rb+')
num = f.write(b'0123456789abcdef')
print(num)

print(f.seek(5))    # 移动到文件的第六个字节
print(f.read(1))
print(f.seek(-3, 2))     # 移动到文件的倒数第三字节
print(f.read(1))


"""
f.close()
在文本文件中 (那些打开文件的模式下没有 b 的), 只会相对于文件起始位置进行定位。
当你处理完一个文件后, 调用 f.close() 来关闭文件并释放系统的资源，如果尝试再调用该文件，则会抛出异常。
>>> f.close()
>>> f.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
ValueError: I/O operation on closed file
<pre>
<p>
当处理一个文件对象时, 使用 with 关键字是非常好的方式。在结束后, 它会帮你正确的关闭文件。 而且写起来也比 try - finally 语句块要简短:</p>
<pre>
>>> with open('/tmp/foo.txt', 'r') as f:
...     read_data = f.read()
>>> f.closed
True
文件对象还有其他方法, 如 isatty() 和 trucate(), 但这些通常比较少用。
"""
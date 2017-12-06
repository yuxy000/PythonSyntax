n = 100
sum = 0
counter = 1

while counter <= n:
    sum += counter
    counter += 1
print("1 到 %d 之和为: %d" % (n, sum))


# 无限循环
"""
var = 1
while var == 1:
    num = int(input("输入一个数值："))
    print("你输入的数字是: ", num)
print("Good bye!")
"""
"""
你可以使用 CTRL+C 来退出当前的无限循环。
无限循环在服务器上客户端的实时请求非常有用。
"""

# while 循环使用 else 语句 在 while … else 在条件语句为 false 时执行 else 的语句块
count = 0
while count < 5:
   print(count, " 小于 5")
   count = count + 1
else:
   print(count, " 大于或等于 5")

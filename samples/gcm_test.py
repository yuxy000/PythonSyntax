# _*_ coding: utf-8 _*_

"""
---------------------------------
@Time     : 2017/12/5 13:41
@Author   : yuxy
@File     : gcm_test.py
@Project  : PythonSyntax
----------------------------------
"""

"""
求最大公约数
"""


def gcm(x, y):
    # 获取最小值
    if x > y:
        smaller = y
    else:
        smaller = x

    for i in range(1, smaller + 1):
        if(x % i == 0) and (y % i == 0):
            gcm = i

    return gcm


n1 = int(input("输入第一个数字："))
n2 = int(input("输入第二个数字："))
print(n1, "和", n2, "的最大公约数为", gcm(n1, n2))

# 其他算法
"""
-------------------------------------------------------
1.

可按以下思路减少循环次数：
1. 当最小值为最大公约数时，直接返回；
2. 当最小值不为最大公约数时，最大公约数不会大于最小值的1/2；
3. 求最大公约数理应从大到小循环递减求最大。
实例：
def gcd(a, b):
    if b > a:
        a, b = b, a   # b为最小值
    if a % b == 0:
        return b      # 判断b是否为最大公约数
    for i in range(b//2+1, 1, -1):    # 倒序求最大公约数更合理
        if b % i == 0 and a % i == 0:
            return i
    return 0

while(True):
    a = int(input("Input 'a':"))
    b = int(input("Input 'b':"))
    print(gcd(a, b))
    
---------------------------------------------------------------
2.

def gcd(x, y): # very fast
   return x if y == 0 else gcd(y, x%y)

print(gcd(378, 5940))  # result: 54
----------------------------------------------------------------    
3.
两个数的最大公约数可以使用 欧几里得算法实现。即两个数的最大公约数等于其中较小的那个数和两数相除余数的最大公约数。
def gcd(a, b):
  if a == 0:
    a, b = b, a
  while b != 0:
    a, b = b, a % b
  return a

print(gcd(54, 24))
-----------------------------------------------------------------
"""
#!/usr/bin/python3

import os
from http.cookiejar import Cookie

print("Content-type: text-html")
print()

print("""
<html>
<head>
    <meta charset="utf-8">
    <title>菜鸟教程(runoob.com)</title>
</head>
<body>
    <h1>读取cookie信息</h1>
""")
print(os.environ)
if 'HTTP_COOKIE' in os.environ:
    print('HTTP_COOKIE')
    cookie_string = os.environ.get('HTTP_COOKIE')
    print(cookie_string)
    c = Cookie.SimpleCookie()
    c.load(cookie_string)

    try:
        data = c['name'].value
        print("cookie data: "+data+"<br>")
    except KeyError:
        print("cookie 没有设置或者已过去<br>")

print("""
</body>
</html>
""")

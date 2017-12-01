#!/usr/bin/python3
"""
使用GET方法传输数据
GET方法发送编码后的用户信息到服务端，数据信息包含在请求页面的URL上，以"?"号分割, 如下所示：
http://www.test.com/cgi-bin/hello.py?key1=value1&key2=value2 有关 GET 请求的其他一些注释：
    GET 请求可被缓存
    GET 请求保留在浏览器历史记录中
    GET 请求可被收藏为书签
    GET 请求不应在处理敏感数据时使用
    GET 请求有长度限制
    GET 请求只应当用于取回数据
"""

# CGI处理模块

import cgi, cgitb

# 创建 FieldStorage 的实例化
form = cgi.FieldStorage()

# 获取数据
site_name = form.getvalue('name')
site_url = form.getvalue('url')

if form.getvalue('google'):
    google_flag = '是'
else:
    google_flag = '否'

if form.getvalue('runoob'):
    runoob_flag = '是'
else:
    runoob_flag = '否'

if form.getvalue('site'):
    site = form.getvalue('site')
else:
    site = '提交的数据为空'

if form.getvalue('textcontent'):
    text_content = form.getvalue('textcontent')
else:
    text_content = "没有内容"

if form.getvalue('dropdown'):
    dropdown_value = form.getvalue('dropdown')
else:
    dropdown_value = "没有内容"

print("Content-type:text/html")
print()
print("<html>")
print("<head>")
print("<meta charset=\"utf-8\">")
print("<title>菜鸟教程 CGI 测试实例</title>")
print("</head>")
print("<body>")
print("<h2>%s官网：%s</h2>" % (site_name, site_url))
print("<h2>Checkbox</h2>")
print("<h2> 菜鸟教程是否选择了 : %s</h2>" % runoob_flag)
print("<h2> Google 是否选择了 : %s</h2>" % google_flag)
print("<h2>Radio</h2>")
print("选中的网站是 %s" % site)
print("<h2>TextArea</h2>")
print("<h2> 输入的内容是：%s</h2>" % text_content)
print("<h2>Select</h2>")
print("<h2> 选中的选项是：%s</h2>" % dropdown_value)
print("</body>")
print("</html>")

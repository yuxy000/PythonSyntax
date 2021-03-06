#!/usr/bin/python3
import cgi
import os

form = cgi.FieldStorage()

fileitem = form['filename']

# 检测文件是否上传
if fileitem.filename:
    # 设置文件路径
    fn = os.path.basename(fileitem.filename)
    open("../tmp/" + fn, 'wb').write(fileitem.file.read)

    message = '文件 "' + fn + '" 上传成功'
else:
    message = '文件没有上传'

print("""\
Content-Type: text/html\n
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>
   <p>%s</p>
</body>
</html>
""" % (message,))

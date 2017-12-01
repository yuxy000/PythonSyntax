"""
cookie的语法
http cookie的发送是通过http头部来实现的，他早于文件的传递，头部set-cookie的语法如下：
Set-cookie:name=name;expires=date;path=path;domain=domain;secure
name=name: 需要设置cookie的值(name不能使用";"和","号),有多个name值时用 ";" 分隔，例如：name1=name1;name2=name2;name3=name3。
expires=date: cookie的有效期限,格式： expires="Wdy,DD-Mon-YYYY HH:MM:SS"
path=path: 设置cookie支持的路径,如果path是一个路径，则cookie对这个目录下的所有文件及子目录生效，例如： path="/cgi-bin/"，如果path是一个文件，则cookie指对这个文件生效，例如：path="/cgi-bin/cookie.cgi"。
domain=domain: 对cookie生效的域名，例如：domain="www.runoob.com"
secure: 如果给出此标志，表示cookie只能通过SSL协议的https服务器来传递。
cookie的接收是通过设置环境变量HTTP_COOKIE来实现的，CGI程序可以通过检索该变量获取cookie信息。
"""
# Cookie设置
# Cookie的设置非常简单，cookie会在http头部单独发送。
print('Content-Type: text/html')
print('Set-Cookie: name="菜鸟教程";expires=Wed, 28 Aug 2016 18:30:00 GMT')
print()
print("""
<html>
  <head>
    <meta charset="utf-8">
    <title>菜鸟教程(runoob.com)</title>
  </head>
    <body>
        <h1>Cookie set OK!</h1>
    </body>
</html>
""")

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
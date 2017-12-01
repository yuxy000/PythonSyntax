#!/usr/bin/python3

import socket
import sys

# 创建 socket 对象
server_socket = socket.socket()

# 获取本地主机名
# host = socket.gethostname()

port = 9999

# 绑定端口
server_socket.bind(('127.0.0.1', port))

# 设置最大连接数
server_socket.listen(5)


while True:
    # 建立客户端连接
    conn, addr = server_socket.accept()

    print("连接地址： %s" % str(addr))

    msg = '欢迎访问菜鸟教程！' + "\r\n"
    conn.send(msg.encode('utf-8'))
    conn.close()

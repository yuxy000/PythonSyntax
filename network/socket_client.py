#!/usr/bin/python3

# 导入 socket、sys 模块
import socket
import sys

# 创建 socket 对象
s = socket.socket()

# 获取本地主机名
host = socket.gethostname()

# 设置端口好
port = 9999

# 连接服务，指定主机和端口
s.connect(('127.0.0.1', port))

# 接收小于 1024 字节的数据
msg = s.recv(1024)

s.close()

print(msg.decode('utf-8'))


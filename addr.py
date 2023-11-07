import socket

# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取 socket 的地址族 (AF_INET)
addr_family = s.family

if addr_family == socket.AF_INET:
    print("The address family is AF_INET")
else:
    print("The address family is not AF_INET")
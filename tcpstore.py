import os
import torch
import torch.distributed as dist
import socket


def run():
    # 创建一个TCPStore对象
    # 使用IPv4地址，例如'127.0.0.1'代表localhost
    # 选择一个未被使用的端口，例如'23456'
    # 设置is_master为True，表示这是主节点
    print(f"{torch.__version__=}")
    print(f"{socket.getaddrinfo(None, 23456)=}")
    print(f"{socket.getaddrinfo('', 12345, flags=socket.AI_PASSIVE|socket.AI_NUMERICSERV)=}")
    os.environ["GLOO_SOCKET_IFNAME"] = "eth0"
    #tcp_store = dist.TCPStore('127.0.0.1', 23456, is_master=True)

    # 你可以使用TCPStore对象来设置和获取键值对
    #tcp_store.set("key", "value")
    #print("The value of 'key' is: ", tcp_store.get("key"))

if __name__ == "__main__":
    run()
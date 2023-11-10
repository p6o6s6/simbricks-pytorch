import torch.distributed as dist

def run():
    # 创建一个TCPStore对象
    # 使用IPv6地址，例如'::1'代表localhost
    # 选择一个未被使用的端口，例如'23456'
    # 设置is_master为True，表示这是主节点
    tcp_store = dist.TCPStore('::1', 23456, is_master=True)

    # 你可以使用TCPStore对象来设置和获取键值对
    tcp_store.set("key", "value")
    print("The value of 'key' is: ", tcp_store.get("key"))

if __name__ == "__main__":
    run()
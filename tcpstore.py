import torch.distributed as dist
from datetime import timedelta
import socket

port = 12345
ip = "172.0.0.1"
ip = "xxxx:yyyy:zzzz::"
client_store = dist.TCPStore(ip, port, 2, False, timedelta(seconds=30))
print("initialized")
print(client_store.get("first_key"))
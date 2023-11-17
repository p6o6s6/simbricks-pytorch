import torch.distributed as dist
from torch.multiprocessing import Process
import torch

def worker(rank, size, tcp_store):
    print(f"The value of 'key' in worker {rank} is: {tcp_store.get('key')}")

def run(rank, size):
    tcp_store = dist.TCPStore("10.0.0.1", 12345, size, False)
    dist.init_process_group(
        "gloo",
        rank=rank,
        store=tcp_store,
        world_size=size)
    worker(rank, size, tcp_store)

def main():
    size = 2
    run(1, size)

if __name__ == "__main__":
    main()
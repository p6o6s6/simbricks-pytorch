import torch
import torch.distributed as dist
import socket
from multiprocessing import Process

def find_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))
        return s.getsockname()[1]

def main(rank, world, port):
    # Specify the initialization method and the port
    init_method = 'tcp://localhost:' + str(port)

    # Initialize the distributed environment.
    dist.init_process_group(
        backend='gloo',
        init_method=init_method,
        rank=rank,
        world_size=world
    )

    # Create a tensor with value `rank`.
    tensor = torch.ones(1) * rank

    # AllReduce operation.
    dist.all_reduce(tensor, op=dist.ReduceOp.SUM)

    print('Rank ', rank, ' has data ', tensor[0])

def run_demo(demo_fn, world_size):
    port = find_free_port()
    processes = []
    for rank in range(world_size):
        p = Process(target=demo_fn, args=(rank, world_size, port))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

# For example, if you have 4 GPUs.
run_demo(main, 1)
import os
import torch
import torch.distributed as dist

def main():
    # 获取当前进程的rank和总的进程数量
    rank = int(os.getenv('RANK', '0'))
    world_size = int(os.getenv('WORLD_SIZE', '1'))

    # 初始化进程组
    dist.init_process_group("gloo", rank=rank, world_size=world_size)

    # 创建一个在当前设备上的Tensor，并初始化它
    tensor = torch.ones(4) * rank
    print(f'Before allreduce: Rank {rank} has {tensor}')

    # 使用all_reduce函数
    dist.all_reduce(tensor, op=dist.ReduceOp.SUM)

    print(f'After allreduce: Rank {rank} has {tensor}')

if __name__ == "__main__":
    main()
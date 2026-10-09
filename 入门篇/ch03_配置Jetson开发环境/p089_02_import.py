# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第3章 配置Jetson开发环境 · 印刷第089页 (PDF第99页)
# 上下文: 下面测试PyTorch，使其在GPU 上完成操作，可参考如下代码。 ／ 图3-13PyTorch 验证GPU 加速是否可用

# PyTorch测试代码

import torch

# 检查是否有可用的GPU，如果有则使用第一个GPU
if torch.cuda.is_available():
    print('CUDA available. Using GPU.')
    device = torch.device("cuda:0")  # 指定使用第一个GPU
else:
    print('No GPU found. Using CPU instead.')
    device = torch.device("cpu")  # 如果没有GPU，则使用CPU

# 创建一个张量并将其移动到GPU
x = torch.randn(3, 3).to(device)

# 打印张量及其所在的设备
print("PyTorch Tensor on GPU/CPU:")
print(x)
print("Device name:", x.device)

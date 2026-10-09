# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第4章 使用Jetson看世界 · 印刷第146-147页 (PDF第156页, PDF第157页)
# 上下文: ResNet-34 模型。读者可以参考4.3.1 节中的模型代码示例，来查看当前模型结构。 ／ 现在来定义神经网络模型，这里使用了ResNet-18 模型。在这

import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import models

# 设备配置
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
# 使用ResNet-18模型
weights = models.ResNet18_Weights.DEFAULT
model = models.resnet18(weights=weights)
num_ftrs = model.fc.in_features
model.fc = nn.Linear(num_ftrs, 2)  # 2类（猫和狗）

print(f"Using device: {device}")

model = model.to(device)

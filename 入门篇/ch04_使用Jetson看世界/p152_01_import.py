# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第4章 使用Jetson看世界 · 印刷第152页 (PDF第162页)
# 上下文: 首先加载模型，参考如下代码。 ／ 图4-15猫狗分类（ResNet）正误预测图片集

import torch
import torchvision.models as models

# 选择设备
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# 定义模型
model = models.resnet18(weights='DEFAULT')  # 不加载预训练权重
num_ftrs = model.fc.in_features
model.fc = torch.nn.Linear(num_ftrs, 2)  # 2类（猫和狗）

# 将模型移动到设备
model.to(device)

# 加载模型权重
model_path = './resnet_cat_dog_classifier.pth'  # 模型权重文件的路径
model.load_state_dict(torch.load(model_path, map_location=device))  # 加载模型权重到设备

# 将模型设置为评估模式
model.eval()

# 创建一个示例输入并将其移动到设备
dummy_input = torch.randn(1, 3, 224, 224).to(device)

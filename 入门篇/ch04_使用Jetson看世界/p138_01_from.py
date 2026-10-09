# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第4章 使用Jetson看世界 · 印刷第138页 (PDF第148页)
# 上下文: 现在执行以下代码查看网络模型信息。

# 导入torchinfo
from torchinfo import summary

# 显示模型结构
summary(net, input_size=(64, 1, 28, 28))

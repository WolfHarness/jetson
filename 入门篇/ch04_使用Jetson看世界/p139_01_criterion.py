# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第4章 使用Jetson看世界 · 印刷第139页 (PDF第149页)
# 上下文: 使得模型的预测结果更加准确。

# Step 6: 定义损失函数和优化器
criterion = nn.CrossEntropyLoss()  # 定义交叉熵损失函数
optimizer = optim.SGD(net.parameters(), lr=0.01, momentum=0.9)  # 定义随机梯度下降优化器

# 创建日志文件
log_file = open("training_log.txt", "w")

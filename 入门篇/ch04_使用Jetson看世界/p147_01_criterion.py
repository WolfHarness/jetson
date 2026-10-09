# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第4章 使用Jetson看世界 · 印刷第147页 (PDF第157页)
# 上下文: 优化性能。 ／ 和优化器（optimizer）是关键组件，它们分别负责衡量模型预测的准确性和更新模型参数以

# 损失函数和优化器
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)

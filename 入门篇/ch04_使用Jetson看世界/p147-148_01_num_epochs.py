# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第4章 使用Jetson看世界 · 印刷第147-148页 (PDF第157页, PDF第158页)
# 上下文: 我们将训练轮数（epoch）设为10 次，并尽可能在GPU 上完成训练。 ／ 3. 训练模型

# 训练过程设置
num_epochs = 10  # 设置训练的总轮数

# 训练循环
for epoch in range(num_epochs):
    model.train()  # 设置模型为训练模式
    running_loss = 0.0  # 初始化本轮训练的累计损失

    # 遍历训练数据集
    for inputs, labels in train_loader:
        inputs, labels = inputs.to(device), labels.to(device)  # 将输入数据和标签移动到指定设备（GPU或CPU）

        optimizer.zero_grad()  # 清零之前的梯度
        outputs = model(inputs)  # 将输入数据传入模型进行前向传播，得到预测结果
        loss = criterion(outputs, labels)  # 计算预测结果与真实标签之间的损失
        loss.backward()  # 进行反向传播，计算梯度
        optimizer.step()  # 更新模型参数

        running_loss += loss.item() * inputs.size(0)  # 累加本批次的损失，乘以批次大小以获得总损失

    epoch_loss = running_loss / len(train_dataset)  # 计算每轮训练的平均损失
print(f'Epoch {epoch+1}/{num_epochs}, Loss: {epoch_loss:.4f}')  # 输出当前轮次的训练损失

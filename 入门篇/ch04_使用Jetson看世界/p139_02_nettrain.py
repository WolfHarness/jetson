# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第4章 使用Jetson看世界 · 印刷第139页 (PDF第149页)
# 上下文: 现在使用GPU 训练模型，共训练10 个epoch（训练轮数）。 ／ 7. 训练模型

# Step 7: 训练模型
net.train() # 切换训练模式

for epoch in range(10):  # 训练总轮数为10
    running_loss = 0.0
    for i, data in enumerate(trainloader, 0):
        inputs, labels = data[0].to(device), data[1].to(device)  # 将数据移动到GPU

        # 梯度清零
        optimizer.zero_grad()

        # 前向传播
        outputs = net(inputs)

        # 计算损失
        loss = criterion(outputs, labels)

        # 反向传播
        loss.backward()

        # 更新参数
        optimizer.step()

        # 打印统计信息
        running_loss += loss.item()
        if i % 100 == 99:  # 每100个小批量打印一次
            log_message = f'[Epoch {epoch + 1}, Mini-batch {i + 1}] loss: {running_loss / 100:.3f}\n'
            print(log_message)
            log_file.write(log_message)
            running_loss = 0.0

# 写入训练结束的标记并关闭日志文件
log_file.write('Finished Training\n')
log_file.close()

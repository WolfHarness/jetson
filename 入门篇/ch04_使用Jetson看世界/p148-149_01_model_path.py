# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第4章 使用Jetson看世界 · 印刷第148-149页 (PDF第158页, PDF第159页)
# 上下文: 加载刚才保存好的模型，开启评估模式。 ／ 5. 评估模型

# 加载训练好的模型权重
model_path = './resnet_cat_dog_classifier.pth'  # 模型权重文件的路径
model.load_state_dict(torch.load(model_path))  # 加载模型权重
model.eval()  # 将模型设置为评估模式（禁用 dropout 和 batch normalization）

# 初始化正确分类的计数器
running_corrects = 0

# 遍历验证集中的所有批次
for inputs, labels in val_loader:
    inputs, labels = inputs.to(device), labels.to(device)  # 将输入数据和标签转移到 GPU（如果有的话）
    outputs = model(inputs)  # 获取模型预测的输出
    _, preds = torch.max(outputs, 1)  # 获取预测的类别标签（预测值中概率最大的索引）
    running_corrects += torch.sum(preds == labels.data)  # 计算预测正确的样本数

# 计算模型在验证集上的准确率
accuracy = running_corrects.double() / len(val_dataset)  # 准确率 = 正确分类数 / 总样本数
print(f'Validation Accuracy: {accuracy:.4f}')  # 输出验证集上的准确率，保留四位小数

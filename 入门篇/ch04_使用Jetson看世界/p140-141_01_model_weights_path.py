# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第4章 使用Jetson看世界 · 印刷第140-141页 (PDF第150页, PDF第151页)
# 上下文: 经过上述过程，我们已经获得了模型，下面进行评估。 ／ 9. 评估模型

# Step 9: 评估模型
# 加载模型
model_weights_path = 'final_model_weights.pth'  # 权重文件路径

# 检查权重文件是否存在
if os.path.exists(model_weights_path):
    print(f'Loading model weights from {model_weights_path}')
    net.load_state_dict(torch.load(model_weights_path))  # 如果权重文件存在，则加载权重
else:
    print('Model weights not found. Initializing new model.')  # 如果权重文件不存在，则只初始化模型

net.eval() # 切换到评估模式

correct = 0
total = 0
all_labels = []
all_preds = []
all_images = []
with torch.no_grad():
    for data in testloader:
        images, labels = data[0].to(device), data[1].to(device)  # 将数据移动到GPU
        outputs = net(images)
        _, predicted = torch.max(outputs.data, 1)  # 获取预测结果
        total += labels.size(0)  # 累计总样本数
        correct += (predicted == labels).sum().item()  # 累计正确预测数
        all_labels.extend(labels.cpu().numpy())  # 将标签移回CPU并转换为numpy数组
        all_preds.extend(predicted.cpu().numpy())  # 将预测结果移回CPU并转换为numpy数组
        all_images.extend(images.cpu().numpy())  # 将图像数据移回CPU并转换为numpy数组

# 计算准确率
accuracy = 100 * correct / total
accuracy_message = f'Accuracy of the network on the 10000 test images: {accuracy}%\n'
print(accuracy_message)

with open("training_log.txt","a") as log_file:
    log_file.write(accuracy_message)

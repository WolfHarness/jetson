# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第4章 使用Jetson看世界 · 印刷第148页 (PDF第158页)
# 上下文: 可将该模型保存下来，以便后续使用。 ／ 上述代码执行结果损失值降到了0.0020，说明模型在训练数据上的表现已经非常出色。

# 保存训练好的模型
model_path = './resnet_cat_dog_classifier.pth'
torch.save(model.state_dict(), model_path)
print(f'Model saved to {model_path}')

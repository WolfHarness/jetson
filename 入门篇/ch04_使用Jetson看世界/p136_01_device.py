# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第4章 使用Jetson看世界 · 印刷第136页 (PDF第146页)
# 上下文: 代码启用GPU 设备。 ／ 按照第3 章内容完成开发环境配置后，使用PyTorch 时可以开启GPU 加速，执行如下

# Step 3: 开启GPU加速
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f'Using device: {device}')

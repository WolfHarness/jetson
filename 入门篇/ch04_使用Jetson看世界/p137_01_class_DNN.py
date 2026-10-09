# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第4章 使用Jetson看世界 · 印刷第137页 (PDF第147页)
# 上下文: 在这个实例中，使用了多层神经网络DNN，共构建了3 个隐藏层，并使用GPU 加速。 ／ 5. 定义神经网络模型

# Step 5: 定义神经网络模型
class DNN(nn.Module):
    def __init__(self):
        super(DNN, self).__init__()
        self.fc1 = nn.Linear(28 * 28, 256)  # 定义第1个隐藏层
        self.fc2 = nn.Linear(256, 128)      # 定义第2个隐藏层
        self.fc3 = nn.Linear(128, 64)       # 定义第3个隐藏层
        self.fc4 = nn.Linear(64, 10)        # 定义输出层

    def forward(self, x):
        x = x.view(-1, 28 * 28)  # 将图像展平成一维向量
 # 使用ReLU激活函数
        x = torch.relu(self.fc1(x))  # 第1层激活
        x = torch.relu(self.fc2(x))  # 第2层激活
        x = torch.relu(self.fc3(x))  # 第3层激活
        x = self.fc4(x)  # 输出层
        return x

net = DNN().to(device)  # 将模型移动到GPU

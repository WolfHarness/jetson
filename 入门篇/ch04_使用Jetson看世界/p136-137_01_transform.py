# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第4章 使用Jetson看世界 · 印刷第136-137页 (PDF第146页, PDF第147页)
# 上下文: 过以下代码构建训练数据集和测试数据集。 ／ PyTorch 和 TensorFlow 都内置了 MNIST 数据集，方便用户进行实验和测试。可以通

# Step 4: 加载MNIST数据集
# 定义数据变换
transform = transforms.Compose([
    transforms.ToTensor(),  # 将图像转换为Tensor
    transforms.Normalize((0.5,), (0.5,))  # 对图像进行归一化处理
])

# 检查数据集是否已经存在
if not os.path.exists('./data/MNIST'):
    os.makedirs('./data/MNIST')  # 如果数据集目录不存在，则创建

# 下载并加载训练数据集
trainset = torchvision.datasets.MNIST(root='./data', train=True, download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=64, shuffle=True)
    # 创建训练数据加载器

# 下载并加载测试数据集
testset = torchvision.datasets.MNIST(root='./data', train=False, download=True, transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=64, shuffle=False)
    # 创建测试数据加载器

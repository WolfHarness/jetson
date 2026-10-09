# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第4章 使用Jetson看世界 · 印刷第145-146页 (PDF第155页, PDF第156页)
# 上下文: 下代码完成数据预处理。 ／ 理。同时，需要将图片数据分组，一部分用于训练，另一部分用于验证。本实例将使用如

# 数据预处理

import os
from PIL import Image, UnidentifiedImageError
from torchvision import datasets, transforms
from torch.utils.data import DataLoader, random_split

# 检查并移除损坏的文件
def is_valid_image(filepath):
    try:
        with Image.open(filepath) as img:
            img.verify()
        return True
    except (IOError, SyntaxError) as e:
        return False

def clean_dataset(data_dir):
    categories = ['Cat','Dog']
    for category in categories:
        folder = os.path.join(data_dir,'PetImages', category)
        for filename in os.listdir(folder):
            filepath = os.path.join(folder, filename)
            if not is_valid_image(filepath):
                print(f'Removing invalid file: {filepath}')
                os.remove(filepath)

# 自定义数据集类，处理和跳过损坏的图像
class CleanImageFolder(datasets.ImageFolder):
    def __init__(self, root, transform=None):
        super().__init__(root, transform)
        self.samples = [(path, label) for path, label in self.samples if is_valid_image(path)]

    def __getitem__(self, index):
        path, target = self.samples[index]
        try:
            sample = self.loader(path)
            if self.transform is not None:
                sample = self.transform(sample)
            return sample, target
        except UnidentifiedImageError:
            print(f'Skipping corrupted file: {path}')
            return self.__getitem__((index + 1) % len(self.samples))

# 定义数据增强和预处理
transform = transforms.Compose([
    transforms.Resize((224, 224)),  # 调整图像大小
    transforms.ToTensor(),          # 转换为Tensor
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])  # 正则化
])

# 数据集路径
data_dir = './kagglecatsanddogs_5340'

# 清理数据集
clean_dataset(data_dir)

# 加载数据集
dataset=CleanImageFolder(os.path.join(data_dir,'PetImages'), transform=transform)

# 将数据集分为训练集和验证集
train_size = int(0.8 * len(dataset))
val_size = len(dataset) - train_size
train_dataset, val_dataset = random_split(dataset, [train_size, val_size])

# 创建数据加载器
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=32, shuffle=False)

# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第4章 使用Jetson看世界 · 印刷第149-150页 (PDF第159页, PDF第160页)
# 上下文: 先来构建用于展示图片的函数，对图片进行裁剪。 ／ 最后，来对结果进行一个抽样，验证模型训练效果。

import matplotlib.pyplot as plt
import numpy as np
import torch
from torchvision import transforms
from PIL import Image
import random

# 用于展示图像的函数
def imshow(ax, img, title=None):
    img = img / 2 + 0.5  # 反标准化
    npimg = img.numpy()
    npimg = np.clip(npimg, 0, 1)  # 将图像数据剪裁到 [0, 1] 范围内
    ax.imshow(np.transpose(npimg, (1, 2, 0)))
    ax.set_axis_off()  # 去掉坐标轴
    if title is not None:
        ax.set_title(title, fontsize=10, color='red')
# 随机抽样指定数量的图像
def get_random_samples(images, labels, preds, num_samples):
    num_samples = min(num_samples, len(images))  # 确保样本数量不超过实际数量
    indices = random.sample(range(len(images)), num_samples)
    sampled_images = [images[i] for i in indices]
    sampled_labels = [labels[i] for i in indices]
    sampled_preds = [preds[i] for i in indices]
    return sampled_images, sampled_labels, sampled_preds

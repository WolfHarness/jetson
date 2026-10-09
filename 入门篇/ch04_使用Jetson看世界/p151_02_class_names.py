# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第4章 使用Jetson看世界 · 印刷第151页 (PDF第161页)
# 上下文: 现在，执行正误图片展示。 ／ 最后，构建一个函数用于图片展示。

# 包含类标签名称的列表
class_names = ['Cat', 'Dog']

# 调用函数展示正误预测图像集合
plot_prediction_collections(model, val_loader, class_names, num_samples=3)

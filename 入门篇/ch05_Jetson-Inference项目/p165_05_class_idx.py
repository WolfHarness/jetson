# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第5章 Jetson-Inference项目 · 印刷第165页 (PDF第175页)
# 上下文: 行分类，并将结果输出。 ／ 也可以在执行命令时，根据表5-4 所示使用其他预训练网络模型。接下来，对图像进

# 对图像进行分类
class_idx, confidence = net.Classify(img)

# 获取分类结果的描述
class_desc = net.GetClassDesc(class_idx)

# 输出结果
print("图像被识别为'{:s}'（类别 #{:d}），置信度为 {:f}%".format(class_desc, class_idx, confidence * 100))

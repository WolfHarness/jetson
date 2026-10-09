# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第5章 Jetson-Inference项目 · 印刷第165页 (PDF第175页)
# 上下文: 现在，加载图像文件以及网络。 ／ 接下来对参数进行解析，并为网络参数设置默认值。

# 加载图像（到共享的CPU/GPU内存中）
img = jetson_utils.loadImage(args.filename)

# 加载识别网络
net = jetson_inference.imageNet(args.network)

# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第5章 Jetson-Inference项目 · 印刷第171页 (PDF第181页)
# 上下文: 接下来，配置网络模型和输入输出流。 ／ 因为直接指定了摄像头作为图像输入源，所以这里省去了参数获取实现。

# 加载检测网络
net = jetson_inference.detectNet("ssd-mobilenet-v2", threshold=0.5)

# 配置视频输入（摄像头）和输出（显示屏）
camera = jetson_utils.videoSource("csi://0")  # 使用CSI摄像头
display = jetson_utils.videoOutput("display://0")  # 显示在屏幕上

# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第5章 Jetson-Inference项目 · 印刷第161页 (PDF第171页)
# 上下文: 在正式使用Jetson-Inference 前，可以使用工具检查摄像头。 ／ 建一个 OpenGL 显示窗口，除非指定了 --headless 参数。

# 查看摄像头图像
cd jetson-inference

# 查看USB摄像头
./video-viewer v4l2:///dev/video0

# 查看MIPI CSI摄像头
./video-viewer csi://0

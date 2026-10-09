# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第5章 Jetson-Inference项目 · 印刷第161页 (PDF第171页)
# 上下文: 也可以将摄像头获得的视频数据进行存储。 ／ 这时，Jetson-Inference 会调起对应的摄像头，并在显示器上输出画面。

# 查看摄像头图像
cd jetson-inference

# 将MIPI CSI摄像头转储为MP4格式的文件
./video-viewer csi://0 output.mp4

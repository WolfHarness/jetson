# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第4章 使用Jetson看世界 · 印刷第129页 (PDF第139页)
# 上下文: 最后，我们在另一个终端中接受RTP 服务，并将视频数据呈现在桌面。 ／ 上述CSI 摄像头RTP 服务命令字参数与USB 摄像头部分别无二致，这里不再复述。

gst-launch-1.0 -v udpsrc port=5000 ! application/x-rtp, payload=96 ! rtph264depay ! avdec_h264 ! videoconvert ! autovideosink

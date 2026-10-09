# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第4章 使用Jetson看世界 · 印刷第130页 (PDF第140页)
# 上下文: 最后，我们在另一个终端中接受RTSP 服务，并将视频数据渲染。 ／ 上述命令关键参数与USB 摄像头RTSP 服务基本一致，这里不再复述。

gst-launch-1.0 -v udpsrc port=8554 ! application/x-rtp, payload=96 ! rtph264depay ! avdec_h264 ! videoconvert ! autovideosink

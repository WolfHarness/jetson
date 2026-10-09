# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第4章 使用Jetson看世界 · 印刷第129页 (PDF第139页)
# 上下文: 首先，为USB 摄像头构建一个RTSP 实时视频流服务。 ／ 2. 基于RTSP 构建实时视频流服务

gst-launch-1.0 -v v4l2src device=/dev/video2 ! \
    video/x-raw, width=640, height=480 ! \
    videoconvert ! \
    x264enc pass=quant ! \
    rtph264pay ! \
    udpsink host=127.0.0.1 port=8554 sync=false async=false

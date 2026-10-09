# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第4章 使用Jetson看世界 · 印刷第128页 (PDF第138页)
# 上下文: 格式并通过网络传输。 ／ USB 摄像头需要使用V4L2，然后使用rtph264pay 将来自 USB 摄像头的数据流打包为RTP

gst-launch-1.0 -v v4l2src device=/dev/video2 !  \
    video/x-raw, width=640, height=480, framerate=30/1 ! \
    videoconvert ! x264enc ! rtph264pay ! udpsink host=127.0.0.1 port=5000

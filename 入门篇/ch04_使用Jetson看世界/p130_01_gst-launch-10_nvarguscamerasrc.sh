# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第4章 使用Jetson看世界 · 印刷第130页 (PDF第140页)
# 上下文: 接下来，如法炮制，为CSI 摄像头构建RTSP 服务。 ／ 迟处理。

gst-launch-1.0 -v nvarguscamerasrc sensor-id=0 ! \
    'video/x-raw(memory:NVMM), width=640, height=480, format=(string)NV12, framerate=(fraction)30/1' ! \
    nvvidconv ! 'video/x-raw, width=640, height=480, format=(string)BGRx' ! \
    videoconvert ! x264enc pass=quant ! \
    rtph264pay ! \
    udpsink host=127.0.0.1 port=8554 sync=false async=false

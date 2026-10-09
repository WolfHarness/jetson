# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第4章 使用Jetson看世界 · 印刷第129页 (PDF第139页)

gst-launch-1.0 nvarguscamerasrc sensor-id=0 ! \
    'video/x-raw(memory:NVMM), width=640, height=480, format=(string)NV12, framerate=(fraction)30/1' ! \
    nvvidconv ! 'video/x-raw, width=640, height=480, format=(string)BGRx' ! \
    videoconvert ! x264enc ! rtph264pay ! udpsink host=127.0.0.1 port=5000

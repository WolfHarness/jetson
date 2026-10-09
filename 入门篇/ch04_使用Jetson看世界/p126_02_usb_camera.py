# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第4章 使用Jetson看世界 · 印刷第126页 (PDF第136页)
# 上下文: 最后，以此调用上述两个函数，调用USB 摄像头。 ／ 接下来，构建capture_usb_frames 函数，从摄像头逐帧读取，并将其画面展示出来。

# 初始化 USB 摄像头并捕获视频帧
usb_camera = open_usb_camera(camera_index=0, width=640, height=480, frame_rate=30)
capture_usb_frames(usb_camera)

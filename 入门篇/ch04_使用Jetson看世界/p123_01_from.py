# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第4章 使用Jetson看世界 · 印刷第123页 (PDF第133页)
# 上下文: 首先，引入JetCam 库，并初始化摄像头对象。 ／ “jetcam/notebooks/usb_camera/usb_camera.ipynb”文件，逐步操作

from jetcam.usb_camera import USBCamera

# 初始化摄像头
camera = USBCamera(width=224, height=224, capture_width=640, capture_height=480, capture_device=0)

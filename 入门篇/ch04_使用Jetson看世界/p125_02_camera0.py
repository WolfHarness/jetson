# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第4章 使用Jetson看世界 · 印刷第125页 (PDF第135页)
# 上下文: 或者同时初始化2 个CSI 摄像头设备，可以参考如下代码。 ／ 这里默认对“ /dev/video0”设备进行初始化。如果想要初始化其他CSI 摄像头设备，

camera0 = CSICamera(capture_device=0, width=224, height=224)
camera1 = CSICamera(capture_device=1, width=224, height=224)

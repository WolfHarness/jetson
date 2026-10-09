# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第4章 使用Jetson看世界 · 印刷第125页 (PDF第135页)
# 上下文: 引入JetCam 操作CSI 摄像头的库，并初始化CSI 摄像头。 ／ 以参考“jetcam/notebooks/csi_camera/csi_camera.i

from jetcam.csi_camera import CSICamera
camera = CSICamera(width=224, height=224)

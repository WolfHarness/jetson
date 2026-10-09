# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第4章 使用Jetson看世界 · 印刷第124页 (PDF第134页)
# 上下文: 实现。 ／ 如果想要在Python 代码中调用CSI 摄像头设备，可以参考JetCam 的csi_camera.py 的

# csi_camera.py 使用GStreamer命令调用CSI摄像头

    def _gst_str(self):
        return 'nvarguscamerasrc sensor-id=%d ! video/x-raw(memory:NVMM), width=%d, height=%d, format=(string)NV12, framerate=(fraction)%d/1 ! nvvidconv ! video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! videoconvert ! appsink' % (
                self.capture_device, self.capture_width, self.capture_height, self.capture_fps, self.width, self.height)

# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第4章 使用Jetson看世界 · 印刷第127页 (PDF第137页)
# 上下文: 最后，依次调用上述两个函数，完成CSI 摄像头调用。 ／ 接下来，构建capture_csi_frames 函数，用于展示CSI 摄像头获得视频数据。

# 示例：初始化 CSI 摄像头并捕获视频帧
csi_camera = open_csi_camera(sensor_id=0, width=640, height=480, frame_rate=30)
capture_csi_frames(csi_camera)

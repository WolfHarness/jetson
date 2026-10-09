# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第4章 使用Jetson看世界 · 印刷第126-127页 (PDF第136页, PDF第137页)
# 上下文: 数中完成命令字构建，并初始化CSI 摄像头。 ／ 使用OpenCV 操作CSI 摄像头，需要借助GStreamer 管道命令，在open_csi_camera 

import cv2

def open_csi_camera(sensor_id=0, width=640, height=480, frame_rate=30):
    """
    使用 OpenCV 初始化 CSI 摄像头。
    :param sensor_id: CSI 摄像头的传感器 ID
    :param width: 摄像头的宽度（分辨率）
    :param height: 摄像头的高度（分辨率）
    :param frame_rate: 摄像头的帧率
    :return: 摄像头对象
    """
    # GStreamer 管道字符串
    gstreamer_pipeline = (
    'nvarguscamerasrc sensor-id={} ! ' # 使用 NVIDIA Argus 相机源，指定传感器 ID
    'video/x-raw(memory:NVMM), width={}, height={}, format=(string)NV12, framerate=(fraction){}/1 ! ' # 设置视频原始格式为 NV12，指定分辨率和帧率，数据保存在 GPU 内存 (NVMM) 中 
    'nvvidconv!video/x-raw,width={},height={},format=(string)BGRx!'#使  用 nvvidconv将视频格式转换为BGRx，指定输出分辨率 
    'videoconvert ! appsink' # 使用 videoconvert 进行额外的格式转换，最后将数据输出到 appsink 
    ).format(sensor_id, width, height, frame_rate, width, height)
    # 创建 VideoCapture 对象
    cap = cv2.VideoCapture(gstreamer_pipeline, cv2.CAP_GSTREAMER)

    if not cap.isOpened():
        print("无法打开摄像头")  # 如果摄像头无法打开，打印错误信息
        return None
    return cap

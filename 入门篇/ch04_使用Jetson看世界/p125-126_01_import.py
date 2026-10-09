# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第4章 使用Jetson看世界 · 印刷第125-126页 (PDF第135页, PDF第136页)
# 上下文: 对象，并为摄像头设置分辨率和帧率。 ／ 在引入OpenCV 库后，构建open_usb_camera 这个函数，在函数内创建 VideoCapture

import cv2

def open_usb_camera(camera_index=0, width=640, height=480, frame_rate=30):
    """
    使用 OpenCV 初始化 USB 摄像头

    :param camera_index: USB 摄像头的索引，通常是 0 或 1
    :param width: 摄像头的宽度（分辨率）
    :param height: 摄像头的高度（分辨率）
    :param frame_rate: 摄像头的帧率
    :return: 摄像头对象
    """
    # 创建 VideoCapture 对象
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        print("无法打开摄像头")  # 如果摄像头无法打开，打印错误信息
        return None
    # 设置摄像头的分辨率和帧率
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    cap.set(cv2.CAP_PROP_FPS, frame_rate)
    return cap

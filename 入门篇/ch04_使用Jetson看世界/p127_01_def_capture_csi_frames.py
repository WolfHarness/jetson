# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第4章 使用Jetson看世界 · 印刷第127页 (PDF第137页)
# 上下文: 接下来，构建capture_csi_frames 函数，用于展示CSI 摄像头获得视频数据。 ／ VideoCapture 对象时与USB 摄像头有所不同，使用

def capture_csi_frames(camera):
    """
    从 CSI 摄像头捕获视频帧并显示。
    :param camera: 摄像头对象
    """
    if camera is None:
        return
    while True:
        ret, frame = camera.read()  # 从摄像头读取一帧
        if not ret:
            break  # 如果读取失败，则退出循环
        # 显示捕获的帧
        cv2.imshow('CSI Camera', frame)

        # 如果按下<q>键，则退出循环
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 释放摄像头并关闭 OpenCV 窗口
    camera.release()
    cv2.destroyAllWindows()

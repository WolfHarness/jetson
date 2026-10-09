# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第4章 使用Jetson看世界 · 印刷第126页 (PDF第136页)
# 上下文: 接下来，构建capture_usb_frames 函数，从摄像头逐帧读取，并将其画面展示出来。

def capture_usb_frames(camera):
    """
    从 USB 摄像头捕获视频帧并显示。
    :param camera: 摄像头对象
    """
    if camera is None:
        return

    while True:
        ret, frame = camera.read()  # 从摄像头读取一帧
        if not ret:
            break  # 如果读取失败，则退出循环
        # 显示捕获的帧
        cv2.imshow('USB Camera', frame)
        # 如果按下<q>键，则退出循环
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # 释放摄像头并关闭 OpenCV 窗口
    camera.release()
    cv2.destroyAllWindows()

# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第5章 Jetson-Inference项目 · 印刷第172页 (PDF第182页)

while display.IsStreaming():
    # 捕获图像
    img = camera.Capture()

    if img is None:
        continue

    # 进行目标检测
    detections = net.Detect(img)

    # 显示检测结果
    display.Render(img)
    display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))

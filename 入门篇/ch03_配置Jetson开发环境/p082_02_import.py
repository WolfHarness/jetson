# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第3章 配置Jetson开发环境 · 印刷第082页 (PDF第92页)
# 上下文: 可以通过如下代码来查看GPU 设备详情： ／ 图3-8OpenCV 开启GPU 加速（Python 版本测试）

# 查看支持CUDA的OpenCV的详细信息

import cv2

# 检查CUDA设备
device_count = cv2.cuda.getCudaEnabledDeviceCount()

if device_count > 0:
    print("OpenCV with CUDA: Yes")
    for i in range(device_count):
        print("\n--- CUDA Device {} ---".format(i))
        cv2.cuda.printShortCudaDeviceInfo(i)
else:
    print("OpenCV with CUDA: No")

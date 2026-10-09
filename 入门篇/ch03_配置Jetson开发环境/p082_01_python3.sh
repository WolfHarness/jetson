# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第3章 配置Jetson开发环境 · 印刷第082页 (PDF第92页)
# 上下文: 下面验证 OpenCV Python 版本是否支持GPU 加速，参考如下命令进行简要测试。 ／ （2）OpenCV Python 版本测试

# 验证OpenCV Python版本是否支持CUDA
python3 -c "import cv2; print('OpenCV with CUDA: ', cv2.cuda.getCudaEnabledDeviceCount() > 0)"

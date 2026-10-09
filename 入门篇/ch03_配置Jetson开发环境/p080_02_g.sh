# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第3章 配置Jetson开发环境 · 印刷第080页 (PDF第90页)
# 上下文: 细信息，验证OpenCV 可以使用GPU 加速。 ／ 然后，编译并执行测试操作，可参考以下命令对上述代码进行编译，获得GPU 设备详

# 编译
g++ -o opencv_cuda_check opencv_cuda_check.cpp \
    `pkg-config --cflags --libs opencv4` \
    -I/usr/include/opencv4 \
    -I/usr/local/include \
    -L/usr/local/cuda/lib64 \
    -lopencv_core -lopencv_highgui -lopencv_cudaarithm -lopencv_cudaimgproc

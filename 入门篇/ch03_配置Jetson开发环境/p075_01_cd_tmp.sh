# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第3章 配置Jetson开发环境 · 印刷第075页 (PDF第85页)
# 上下文: 具体执行过程参考以下命令。 ／ 在“ /tmp”目录下构建编译目录，并用git 获取OpenCV 和OpenCV-Contrib 两个包，

# 准备软件包
cd /tmp
mkdir build_opencv
cd build_opencv

# OpenCV版本
OPENCV_VERSION=4.9.0

# 克隆
git clone --depth 1 --branch ${OPENCV_VERSION} https://github.com/opencv/opencv.git
git clone --depth 1 --branch ${OPENCV_VERSION} https://github.com/opencv/opencv_contrib.git

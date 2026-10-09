# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第3章 配置Jetson开发环境 · 印刷第75-76页 (PDF第85页, PDF第86页)
# 上下文: 自行调整相关参数（CUDA_ARCH 和CUDNN_VERSION）。 ／ Jetson Orin Nano 设备编译OpenCV 命令如下，其他Jetson 

# 准备makefile

cd /tmp/build_opencv/opencv
mkdir build
cd build

# CUDA架构，可选5.3,6.2,7.2,8.7
# 由JTOP可知, 当前Jetson Orin Nano的CUDA架构版本为8.7
CUDA_ARCH=8.7

# 由JTOP可知, 当前Jetson Orin Nano的cuDNN版本为8.6
CUDNN_VERSION=8.6

# 生成makefile
cmake \
    -D BUILD_EXAMPLES=OFF \
    -D BUILD_opencv_python2=OFF \
    -D BUILD_opencv_python3=ON \
    -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D PYTHON_DEFAULT_EXECUTABLE=$(which python3) \
    -D PYTHON3_INCLUDE_DIR=$(python3 -c "from distutils.sysconfig import get_python_inc; print(get_python_inc())") \ 
    -D PYTHON3_PACKAGES_PATH=$HOME/.local/lib/python$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")/site-packages \ 
    -D CUDA_ARCH_BIN=${CUDA_ARCH} \
    -D CUDA_ARCH_PTX= \
    -D CUDA_FAST_MATH=ON \
    -D CUDNN_VERSION=${CUDNN_VERSION} \
    -D EIGEN_INCLUDE_PATH=/usr/include/eigen3 \
    -D ENABLE_NEON=ON \
    -D OPENCV_DNN_CUDA=ON \
    -D OPENCV_ENABLE_NONFREE=ON \
    -D OPENCV_EXTRA_MODULES_PATH=/tmp/build_opencv/opencv_contrib/modules \
    -D OPENCV_GENERATE_PKGCONFIG=ON \
    -D WITH_CUBLAS=ON \
    -D WITH_CUDA=ON \
    -D WITH_CUDNN=ON \
    -D WITH_GSTREAMER=ON \
    -D WITH_LIBV4L=ON \
    -D WITH_OPENGL=ON \
    -D BUILD_PERF_TESTS=OFF \
    -D BUILD_TESTS=OFF \
    …

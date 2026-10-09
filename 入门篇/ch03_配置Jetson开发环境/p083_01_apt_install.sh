# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第3章 配置Jetson开发环境 · 印刷第083页 (PDF第93页)
# 上下文: 在安装TensorFlow 前对现有Python 环境依赖包版本做如下处理。 ／ 1. 安装TensorFlow

sudo apt install -y \
    libhdf5-serial-dev \
    hdf5-tools \
    libhdf5-dev \
    zlib1g-dev \
    zip \
    libjpeg8-dev \
    liblapack-dev \
    libblas-dev \
    gfortran

# 清理软件
sudo apt autoremove -y

# 安装依赖包
python -m pip install h5py onnx

# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第3章 配置Jetson开发环境 · 印刷第087页 (PDF第97页)
# 上下文: 安装TorchVision 时注意与PyTorch 版本匹配，可参考如下命令完成手动编译安装。 ／ 图3-12TorchVision 包引用警告

# 编译安装TorchVision

sudo apt install -y \
 libjpeg-dev \
 zlib1g-dev \
 libpython3-dev \
 libavcodec-dev \
 libavformat-dev \
 libswscale-dev

# 克隆
git clone --branch v0.16.0 https://github.com/pytorch/vision torchvision && cd torchvision

# 安装TorchVision
export BUILD_VERSION=0.16.0
export FORCE_CUDA=1
export FORCE_MPS=1
export TORCH_CUDA_ARCH_LIST="8.7"

# 为当前用户安装
python3 setup.py install --user

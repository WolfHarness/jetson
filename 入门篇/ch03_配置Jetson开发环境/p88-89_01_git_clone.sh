# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第3章 配置Jetson开发环境 · 印刷第88-89页 (PDF第98页, PDF第99页)
# 上下文: 编译。 ／ 如果版本符合编译环境要求，可以参考TorchVision 的编译过程来完成TorchAudio 的

# 克隆并安装 TorchAudio
git clone --branch v2.1.0 https://github.com/pytorch/audio torchaudio
cd torchaudio

# 配置系统参数
export USE_CUDA=1
export CUDA_HOME=/usr/local/cuda
export TORCH_CUDA_ARCH_LIST="8.7"  # Jetson Orin GPU架构
export CC=/usr/bin/gcc-9
export CXX=/usr/bin/g++-9
python3 setup.py clean

# 打包成whl文件
python3 setup.py bdist_wheel

# 安装TorchAudio
cd dist && python3 -m pip install *.whl

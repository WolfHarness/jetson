# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第3章 配置Jetson开发环境 · 印刷第086页 (PDF第96页)
# 上下文: 安装PyTorch 可参考如下命令。 ／ （1）安装PyTorch

# 安装前置依赖包
sudo apt install -y libopenblas-dev

python3 -m pip install onnx

# 下载安装包
cd ~/Downloads
wget --no-check-certificate https://developer.download.nvidia.cn/compute/redist/jp/v512/pytorch/torch-2.1.0a0+41361538.nv23.06-cp38-cp38-linux_aarch64.whl

# 安装PyTorch
python3 -m pip install --verbose --no-cache-dir torch-2.1.0a0+41361538.nv23.06-cp38-cp38-linux_aarch64.whl

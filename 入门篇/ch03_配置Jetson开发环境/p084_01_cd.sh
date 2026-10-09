# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第3章 配置Jetson开发环境 · 印刷第084页 (PDF第94页)
# 上下文: 完成h5py 编译后，TensorFlow 安装就没有任何悬念了，参考以下命令执行安装即可。

# 下载安装包
cd ~/Downloads
wget --no-check-certificate https://developer.download.nvidia.cn/compute/redist/jp/v512/tensorflow/tensorflow-2.12.0+nv23.06-cp38-cp38-linux_aarch64.whl

# 安装TensorFlow
python3 -m pip install --verbose tensorflow-2.12.0+nv23.06-cp38-cp38-linux_aarch64.whl

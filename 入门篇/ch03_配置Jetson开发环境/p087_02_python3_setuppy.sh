# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第3章 配置Jetson开发环境 · 印刷第087页 (PDF第97页)
# 上下文: TorchVision 打包成“*.whl”文件，便于日后使用。 ／ TorchVision 编译过程需要花费一些时间，请读者耐心等待。也可以使用如下命令将

# 打包成whl文件
python3 setup.py bdist_wheel
# 安装TorchVision
cd dist && python3 -m pip install *.whl

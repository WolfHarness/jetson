# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第5章 Jetson-Inference项目 · 印刷第157页 (PDF第167页)
# 上下文: 步骤３编译安装。现在可以执行编译操作，完成安装任务了。 ／ 在这个环节中，可以直接选择“Skip”跳过安装，之后执行以下命令重新选择。

# 使用CPU全核编译
make -j$(nproc)
sudo make install
sudo ldconfig

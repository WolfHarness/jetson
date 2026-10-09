# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第3章 配置Jetson开发环境 · 印刷第076页 (PDF第86页)
# 上下文: makefile 编译成功后，建议关闭其他程序，使用CPU 全核编译。 ／ OpenCV 版本。

# 使用$(nproc)获取CPU核数并编译
make -j$(nproc)

# 安装
sudo make install

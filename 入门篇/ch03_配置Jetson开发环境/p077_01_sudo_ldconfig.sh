# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第3章 配置Jetson开发环境 · 印刷第077页 (PDF第87页)
# 上下文: 通过编译安装的OpenCV 通常需要手动加载“.so”文件，可以按照如下命令手动加载。 ／ Python 正常运行。

# 更新系统缓存
sudo ldconfig

# 追加包依赖路径
echo 'export LD_LIBRARY_PATH=/usr/local/lib/:$LD_LIBRARY_PATH' >> ~/.bashrc
echo 'export PATH=$PATH:$HOME/.local/bin'>> ~/.bashrc

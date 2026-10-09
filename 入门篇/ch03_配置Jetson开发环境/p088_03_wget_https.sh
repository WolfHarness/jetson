# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第3章 配置Jetson开发环境 · 印刷第088页 (PDF第98页)
# 上下文: 这种情况，可以使用如下命令升级CMake 版本。 ／ 在具体编译时，可能会遇到CMake 版本过低而导致无法编译的问题，具体如下。

# 本地编译CMake
wget https://github.com/Kitware/CMake/releases/download/v3.26.4/cmake-3.26.4.tar.gz
tar -xvf cmake-3.26.4.tar.gz
cd cmake-3.26.4
./bootstrap
make -j4
sudo make install

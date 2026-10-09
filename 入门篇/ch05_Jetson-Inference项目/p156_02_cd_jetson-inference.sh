# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第5章 Jetson-Inference项目 · 印刷第156页 (PDF第166页)
# 上下文: 如果编译过程出现异常，请执行以下命令。 ／ Cmake。

# 更新子模块
cd jetson-inference
git submodule update --init

# 清理旧的构建目录
rm -rf build
mkdir -p build
cd build

# 重新配置
cmake ../

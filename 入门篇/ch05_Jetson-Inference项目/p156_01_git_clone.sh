# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第5章 Jetson-Inference项目 · 印刷第156页 (PDF第166页)
# 上下文: Cmake。 ／ 步骤2克隆并配置Cmake。切换到用户主目录下，克隆Jetson-Inference，并配置

# 克隆Jetson-Inference
git clone --recursive https://github.com/dusty-nv/jetson-inference
# 进入Jetson-Inference主目录，构建编译目录，并使用Cmake配置
cd jetson-inference
mkdir build
cd build
cmake ../

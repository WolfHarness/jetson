# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第5章 Jetson-Inference项目 · 印刷第179页 (PDF第189页)
# 上下文: 参考以下命令，使用摄像头获取图像做手势姿态估计。 ／ 解手部的动态变化和静态姿势。

cd jetson-inference/build/aarch64/bin
./posenet --network=resnet18-hand

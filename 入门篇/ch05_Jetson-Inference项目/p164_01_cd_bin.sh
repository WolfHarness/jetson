# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第5章 Jetson-Inference项目 · 印刷第164页 (PDF第174页)
# 上下文: AlexNet 网络模型等，如下文命令所示。 ／ 除了使用默认摄像头数据和默认网络模型，也可以使用RTSP 流作为输入源，或使用

cd jetson-inference/build/aarch64/bin
./imagenet rtsp://192.168.0.30:1234 --network=alexnet

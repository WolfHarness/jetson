# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第5章 Jetson-Inference项目 · 印刷第185页 (PDF第195页)
# 上下文: 现在将摄像头作为输入源，实时进行背景替换，参考如下命令。 ／ 处理，就可以完成背景去除，整个过程完全自动化。

cd jetson-inference/build/aarch64/bin
./backgroundnet --replace=images/coral.jpg

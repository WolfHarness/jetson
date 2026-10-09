# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第5章 Jetson-Inference项目 · 印刷第175页 (PDF第185页)
# 上下文: 使用以下命令调用Jetson-Inference 对多人图片做语义分割 推理。 ／  --filter-mode：可选，标志接受point 或linear 采

cd jetson-inference/build/aarch64/bin
./segnet --network=fcn-resnet18-mhp-512x320 images/humans_0.jpg images/test/output.jpg

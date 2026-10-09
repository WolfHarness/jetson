# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第5章 Jetson-Inference项目 · 印刷第185页 (PDF第195页)
# 上下文: Jetson-Inference 提供的背景去除推理简单易用，参考如下命令，对图片背景进行替换。 ／  --replace：可选，替换背景图片。

cd jetson-inference/build/aarch64/bin

# 去除图片背景
./backgroundnet.py images/bird_0.jpg images/test/bird_mask.png

# 替换图片背景
./backgroundnet.py --replace=images/snow.jpg images/bird_0.jpg images/test/bird_replace.jpg 

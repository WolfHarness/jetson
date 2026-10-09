# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第5章 Jetson-Inference项目 · 印刷第171页 (PDF第181页)
# 上下文:  --labels：可选，标签，与自定义模型相对应。 ／  --model：可选，自定义模型，支持caffemodel、UFF 和ONNX 模型。

cd jetson-inference/build/aarch64/bin
./detectnet --model=resnet_cat_dog_model.onnx --labels= labels.txt

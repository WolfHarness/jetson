# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第5章 Jetson-Inference项目 · 印刷第182页 (PDF第192页)
# 上下文: 在Jetson-Inference 工作目录构建一个video 目录并建立软链接，方便我们后续操作。 ／ 过学习和探索新的真实动作类别来鼓励对动作识别的进一步研

cd jetson-inference/build/aarch64/bin
# 构建视频存储目录
mkdir video && cd video
# 构建软链接
ln -s ~/jetson-inference/data/videos ~/jetson-inference/build/aarch64/bin/videos

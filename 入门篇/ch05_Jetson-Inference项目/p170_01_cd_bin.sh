# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第5章 Jetson-Inference项目 · 印刷第170页 (PDF第180页)
# 上下文: Jetson-Inference 自带的图片库进行人脸检测，并将结果标记在图片上。 ／ 我们先来使用专门进行人脸识别任务的模型—TAO FaceDetect。执

cd jetson-inference/build/aarch64/bin
./detectnet images/humans_5.jpg images/test/humans_5.jpg --network=facenet

# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第5章 Jetson-Inference项目 · 印刷第170页 (PDF第180页)
# 上下文: PeopleNet 对比测试，参考以下命令更换网络模型。 ／ 这显然不符合我们的预期，TAO FaceDetect 模型对于侧脸识别不尽如人意，改用TAO

cd jetson-inference/build/aarch64/bin
./detectnet images/humans_5.jpg images/test/humans_5.jpg --network=peoplenet

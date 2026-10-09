# 出处: 《NVIDIA Jetson AI硬件开发实战：入门篇》第4章 使用Jetson看世界 · 印刷第121页 (PDF第131页)
# 上下文: 下命令调用USB 摄像头。 ／ 有了gst-launch-1.0，调用USB 摄像头获取画面就要比前文的操作简便多了，可参考如

# 使用gst-launch-1.0调用USB摄像头
gst-launch-1.0 v4l2src device=/dev/video2 ! videoconvert ! autovideosink
